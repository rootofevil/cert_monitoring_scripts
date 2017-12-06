#!/bin/env python
import os, json, sys
def list_certs(dir):
    if os.path.isdir(dir):
        return os.listdir(dir)

def get_certs_in_json(list):
    json_list = []
    if list is None:
        return {'data': []}
    for domain, path in list.iteritems():
        json_list.append({'{#DOMAIN_NAME}': domain, '{#CERT_DIR}': path})
        
    data = {'data': json_list}
        
    return json.dumps(data)
    

if __name__ == "__main__":
    services = {'letsencrypt': '/etc/letsencrypt/live/', 'centos': '/etc/pki/tls/certs/domains'}
    try:
        type = sys.argv[1]
    except IndexError:
        certs = {}
        for name, path in services.iteritems():
            list = list_certs(path)
            
            if list is not None:
                a = dict.fromkeys(list)
                for i in a:
                    a[i] = path
                certs.update(a)
        print get_certs_in_json(certs)   
        exit(0)
    if type == 'letsencrypt':
        dir = services['letsencrypt']
    elif type == 'centos':
        dir = services['centos']
    else:
        exit('unknown type of service')
      
    print get_certs_in_json(list_certs(dir))

