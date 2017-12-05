#!/bin/env python
import subprocess, sys
from datetime import datetime

def get_cert_exp(path):
    com = "openssl x509 -noout -enddate -in " + path
    process = subprocess.Popen(com.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    if error is None:
        date = datetime.strptime(output.split('=')[1][:-1], '%b %d %H:%M:%S %Y %Z')
        expire_in = (date - datetime.now()).days
        return expire_in

if __name__ == "__main__":
    try:
        type = sys.argv[1]
        domain = sys.argv[2]
    except IndexError:
        exit("Error: 2 Args expected")
    
    if type == 'letsencrypt':
        dir = '/etc/letsencrypt/live/' + domain + '/cert.pem'
    elif type == 'centos':
        dir = "/etc/pki/tls/certs/" + domain + '.pem'
        exit('not implemented yet')
    else:
        exit('unknown type of service')
        
    print get_cert_exp(dir)
