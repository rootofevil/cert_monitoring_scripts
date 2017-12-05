#!/bin/env python
import os, json, sys
def list_certs(dir):
    if os.path.isdir(dir):
        return os.listdir(dir)

def get_certs_in_json(list):
    json_list = []
    for domain in list:
        json_list.append({'{#DOMAIN_NAME}': domain})
        
    data = {'data': json_list}
        
    print json.dumps(data)
    
        
#def check_cert_date():
#    pass


if __name__ == "__main__":
    try:
        type = sys.argv[1]
    except IndexError:
        print "Error: Arg expected"
        exit(1)
    if type == 'letsencrypt':
        dir = "/etc/letsencrypt/live/"
    elif type == 'centos':
        dir = "/etc/pki/tls/certs/"
        exit('not implemented yet')
    else:
        exit('unknown type of service')
      
    get_certs_in_json(list_certs(dir))

