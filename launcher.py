from helm import Helm

if __name__ == '__main__':
    ctx = Helm()

#    try:
#        data = ctx.list(namespace='ingress-nginx', kubeconfig='/Users/lucho/.kube/config1')
#    except Exception as err:
#        print(err)
#        print(ctx.command)
#
    print('')
    data = ctx.list(namespace='ingress-nginx')
    print(data)
#
#    print('')
#    data = ctx.list(namespace='ingress-nginx', output='table')
#    print(data)
#
#    print('')
#    ctx.output = 'table'
#    data = ctx.status(namespace='ingress-nginx', release='ingress-nginx', output='yaml')
#    print(data)
#
#    print('')
#    data = ctx.repo_list()
#    print(data)
#
#    print('')
#    data = ctx.repo_add(name='bitnami', url='https://charts.bitnami.com/bitnami')
#    print(data)
#
#    print('')
#    data = ctx.repo_remove(name='bitnami', url='https://charts.bitnami.com/bitnami')
#    print(data)
#
#    print('')
#    data = ctx.repo_add(name='bitnami', url='https://charts.bitnami.com/bitnami')
#    print(data)
#    ctx.repo_update()
#
#    print('')
#    data = ctx.template(release='my-nginx', chart='bitnami/nginx')
#    print(data)
#
#    print('')
#    data = ctx.search()
#    print(data)
#
#    print('')
#    data = ctx.search(keyword='bitnami/nginx', version='9.2.19')
#    print(data)
#
#    print('')
#    data = ctx.search(keyword='bitnami/nginx', versions=True)
#    print(data)
#
#    print('')
#    data = ctx.install(namespace='default', release='my-nginx', chart='bitnami/nginx')
#    print(data)
#
#    print('')
#    data = ctx.uninstall(namespace='default', release='my-nginx')
#    print(data)
#
#    print('')
#    data = ctx.template(chart='../charts/nginx', release='nginx', values='./values.yaml')
#    map_values = {
#        'image': {
#            'tag': 'v1',
#            'repository': "nginx-map"
#        }
#    }
#    data = ctx.template(chart='/Users/lucho/00/helm3/charts/nginx', release='nginx', values=map_values)
#    print(data)