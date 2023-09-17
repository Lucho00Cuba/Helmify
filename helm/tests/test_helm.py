# own's
from helm import Helm
from helm.exceptions import CommandExecutionError
# third party's
import unittest
import json


class TestHelm(unittest.TestCase):

    ctx = Helm()

    def test_00_helm_instance(self):
        self.assertTrue(self.ctx)

    def test_01_helm_remove_repo(self):
        self.assertNotEqual(
            self.ctx.repo_remove(
                name='bitnami',
                url='https://charts.bitnami.com/bitnami'
            ),
            dict
        )

    def test_02_helm_add_repo(self):
        self.assertNotEqual(
            self.ctx.repo_add(
                name='bitnami',
                url='https://charts.bitnami.com/bitnami'
            ),
            dict
        )

    def test_03_helm_update_repo(self):
        self.ctx.repo_add(
            name='bitnami',
            url='https://charts.bitnami.com/bitnami'
        )
        self.assertNotEqual(
            self.ctx.repo_update(),
            ''
        )

    def test_04_helm_command_execution_error(self):
        with self.assertRaises(CommandExecutionError):
            self.ctx.list(
                namespace='ingress-nginx',
                kubeconfig='/Users/lucho/.kube/config1'
            )

    def test_05_helm_list_is_not_empty(self):
        instance = self.ctx.list(namespace='ingress-nginx')
        self.assertNotEqual(instance, '')

    def test_06_helm_list_is_empty(self):
        instance = self.ctx.list(namespace='ingress-nginx-test')
        self.assertEqual(instance, '[]')

    def test_07_helm_status_is_not_empty(self):
        instance = self.ctx.status(
            namespace='ingress-nginx',
            release='ingress-nginx'
        )
        self.assertNotEqual(instance, '')

    def test_08_helm_repo_list_is_not_empty(self):
        self.assertNotEqual(self.ctx.repo_list(), '')

    def test_09_helm_search_all(self):
        self.assertNotEqual(self.ctx.search(), '')

    def test_10_helm_search_all_versions(self):
        instance = self.ctx.search(keyword='bitnami/nginx', versions=True)
        self.assertNotEqual(instance, '')

    def test_11_helm_search_version(self):
        sversion = "9.2.19"
        instance = self.ctx.search(keyword='bitnami/nginx', version=sversion)
        dversion = json.loads(instance)[0]['version']
        self.assertEqual(
            dversion,
            sversion
        )

    def test_12_helm_template_with_map(self):
        self.assertNotEqual(
            self.ctx.template(
                chart='./charts/nginx',
                release='nginx',
                values={
                    'image': {
                        'tag': 'v1',
                        'repository': "nginx-map"
                    }
                }
            ),
            ''
        )

    def test_13_helm_template_with_file(self):
        instance = self.ctx.template(
            chart='./charts/nginx',
            release='nginx',
            values='./values.yaml'
        )
        self.assertNotEqual(instance, '')

    def test_14_helm_install(self):
        instance = self.ctx.install(
            namespace='default',
            release='my-nginx',
            chart='bitnami/nginx'
        )
        self.assertNotEqual(instance, '')

    def test_15_helm_uninstall(self):
        instance = self.ctx.uninstall(
            namespace='default',
            release='my-nginx'
        )
        self.assertNotEqual(instance, '')

    def test_16_helm_status_show_command(self):
        self.ctx.debug = True
        instance = self.ctx.status(
            namespace='ingress-nginx',
            release='ingress-nginx'
        )
        self.ctx.debug = False
        self.assertNotEqual(instance, '')

    def test_17_helm_status_table(self):
        instance = self.ctx.status(
            namespace='ingress-nginx',
            release='ingress-nginx',
            output='table'
        )
        self.assertNotEqual(instance, '')

    def test_18_helm_list_table(self):
        instance = self.ctx.list(
            namespace='ingress-nginx-test',
            output='table'
        )
        self.assertTrue(instance)

    def test_19_helm_repo_list_table(self):
        self.assertNotEqual(
            self.ctx.repo_list(
                output='table'
            ),
            ''
        )

    def test_20_helm_search_table(self):
        instance = self.ctx.search(
            keyword='bitnami/nginx',
            versions=True,
            output='table'
        )
        self.assertNotEqual(instance, '')
