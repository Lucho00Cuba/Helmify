# own's
from .exceptions import CommandExecutionError
# third party's
import subprocess
from os import environ as os_environ
import json


class Helm:
    def __init__(
        self,
        helm='helm',
        kubeconfig=os_environ.get('KUBECONFIG', "~/.kube/config"),
        namespace='default',
        chart_dir='',
        raise_ex_on_err=False,
        output='json',
        debug=False
    ):
        # init
        self.helm = helm
        self.kubeconfig = kubeconfig
        self.namespace = namespace
        self.chart_dir = chart_dir
        self.raise_ex_on_err = raise_ex_on_err
        self.output = output
        self.debug = debug

    def __run_command(self, command):
        try:
            result = subprocess.run(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=True,
                text=True,
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as err:
            raise CommandExecutionError(err.returncode, err.stderr.strip())

    def __make_command(self, stream_command: list, template: list, **kwargs):

        def dict_to_dot_string(d, parent_key='', sep='.'):
            items = []
            for k, v in d.items():
                new_key = f"{parent_key}{sep}{k}" if parent_key else k
                if isinstance(v, dict):
                    items.extend(
                        dict_to_dot_string(
                            v, new_key, sep=sep).items()
                        )
                else:
                    items.append((new_key, v))
            return dict(items)

        def make_type(data_type, data_value):
            if data_type == 'args':
                stream_command.append(f"--{item['name']}")
            stream_command.append(data_value)

        for item in template:
            if item['name'] in kwargs:
                # kwargs value
                if isinstance(kwargs[item['name']], dict):
                    result = dict_to_dot_string(kwargs[item['name']])
                    item['name'] = 'set'
                    make_type(
                        data_type='args',
                        data_value=",".join(
                            [f"{key}={value}" for key, value in result.items()]
                        )
                    )
                else:
                    make_type(
                        data_type=item['type'],
                        data_value=kwargs[item['name']]
                    )
            else:
                # default value
                try:
                    make_type(
                        data_type=item['type'],
                        data_value=getattr(self, item['name'])
                    )
                except AttributeError:
                    pass
        if self.debug:
            print(f"CMD: {' '.join(stream_command)}")
        self.command = stream_command
        return stream_command

    def list(self, namespace: str, **kwargs):
        # make command
        command = [self.helm, '--namespace', namespace, 'list']
        template = [
            {'name': 'output', 'type': 'args'},
            {'name': 'kubeconfig', 'type': 'args'}
        ]
        if 'output' in kwargs and kwargs['output'].lower() != 'json':
            execution = self.__run_command(
                self.__make_command(
                    stream_command=command,
                    template=template,
                    **kwargs
                )
            )
            # print(f"""{execution}""")
            return True
        elif ('output' in kwargs and kwargs['output'].lower() == 'json'
              or self.output == 'json'):
            execution = eval(self.__run_command(
                self.__make_command(
                    stream_command=command,
                    template=template,
                    **kwargs)
                )
            )
            return json.dumps(execution, indent=2)

    def status(self, namespace: str, release: str, **kwargs):
        # make command
        command = [self.helm, '--namespace', namespace, 'status', release]
        template = [
            {'name': 'output', 'type': 'args'},
            {'name': 'kubeconfig', 'type': 'args'}
        ]

        if 'output' in kwargs and kwargs['output'].lower() != 'json':
            execution = self.__run_command(
                self.__make_command(
                    stream_command=command,
                    template=template,
                    **kwargs
                )
            )
            # print(f"""{execution}""")
            return execution
        elif ('output' in kwargs and kwargs['output'].lower() == 'json'
              or self.output == 'json'):
            execution = eval(self.__run_command(
                self.__make_command(
                    stream_command=command,
                    template=template,
                    **kwargs
                )
            ))
            return json.dumps(execution, indent=2)

    def repo_list(self, **kwargs):
        command = [self.helm, 'repo', 'list']
        template = [
            {'name': 'output', 'type': 'args'},
            {'name': 'kubeconfig', 'type': 'args'}
        ]
        if 'output' in kwargs and kwargs['output'].lower() != 'json':
            execution = self.__run_command(
                self.__make_command(
                    stream_command=command,
                    template=template,
                    **kwargs
                )
            )
            # print(f"""{execution}""")
            return execution
        elif ('output' in kwargs and kwargs['output'].lower() == 'json'
              or self.output == 'json'):
            execution = eval(self.__run_command(
                self.__make_command(
                    stream_command=command,
                    template=template,
                    **kwargs
                )
            ))
            return json.dumps(execution, indent=2)

    def repo_add(self, name: str, url: str, **kwargs):
        command = [self.helm, 'repo', 'add', name, url]
        template = [
            {'name': 'kubeconfig', 'type': 'args'},
            {'name': 'username', 'type': 'args'},
            {'name': 'password', 'type': 'args'}
        ]
        execution = self.__run_command(
            self.__make_command(
                stream_command=command,
                template=template,
                **kwargs
            )
        )
        return {"message": execution}

    def repo_remove(self, name: str, **kwargs):

        command = [self.helm, 'repo', 'remove', name]
        template = [
            {'name': 'kubeconfig', 'type': 'args'}
        ]
        execution = self.__run_command(
            self.__make_command(
                stream_command=command,
                template=template,
                **kwargs
            )
        )
        return {"message": execution}

    def repo_update(self, **kwargs):

        command = [self.helm, 'repo', 'update']
        template = [
            {'name': 'kubeconfig', 'type': 'args'}
        ]
        execution = self.__run_command(
            self.__make_command(
                stream_command=command,
                template=template,
                **kwargs
            )
        )
        return {"message": execution}

    def search(self, versions=False, **kwargs):
        if versions:
            command = [self.helm, 'search', 'repo', '--versions']
        else:
            command = [self.helm, 'search', 'repo']
        template = [
            {'name': 'kubeconfig', 'type': 'args'},
            {'name': 'output', 'type': 'args'},
            {'name': 'keyword', 'type': 'param'},
            {'name': 'version', 'type': 'args'}
        ]
        if 'output' in kwargs and kwargs['output'].lower() != 'json':
            execution = self.__run_command(
                self.__make_command(
                    stream_command=command,
                    template=template,
                    **kwargs
                )
            )
            # print(f"""{execution}""")
            return execution

        elif ('output' in kwargs and kwargs['output'].lower() == 'json'
              or self.output == 'json'):
            execution = eval(self.__run_command(
                self.__make_command(
                    stream_command=command,
                    template=template,
                    **kwargs
                )
            ))
            return json.dumps(execution, indent=2)

    def template(self, chart: str, release='test', **kwargs):

        command = [self.helm, 'template', release, chart]
        template = [
            {'name': 'kubeconfig', 'type': 'args'},
            {'name': 'version', 'type': 'args'},
            {'name': 'values', 'type': 'args'}
        ]
        execution = self.__run_command(
            self.__make_command(
                stream_command=command,
                template=template,
                **kwargs
            )
        )
        return execution

    def install(self, namespace: str, release: str, chart: str, **kwargs):

        command = [
            self.helm,
            '--namespace',
            namespace,
            'install',
            release,
            chart
        ]
        template = [
            {'name': 'kubeconfig', 'type': 'args'},
            {'name': 'values', 'type': 'args'}
        ]
        execution = self.__run_command(
            self.__make_command(
                stream_command=command,
                template=template,
                **kwargs
            )
        )
        return execution

    def uninstall(self, namespace: str, release: str, **kwargs):

        command = [self.helm, '--namespace', namespace, 'uninstall', release]
        template = [
            {'name': 'kubeconfig', 'type': 'args'}
        ]
        execution = self.__run_command(
            self.__make_command(
                stream_command=command,
                template=template,
                **kwargs
            )
        )
        return execution
