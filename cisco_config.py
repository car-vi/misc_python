import paramiko
import sys
import time



def proc (host, usr, pwd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=usr, password=pwd, look_for_keys=False, allow_agent=False)
    stdin,stdout,stderr = ssh.exec_command(command)
    print (stdout.read())
    print ("%s") % (host)
    #filename = ('%s' % (host))
    #sys.stdout = open(filename, 'wb')
    time.sleep(5)




usr = "admin"
pwd = "paramiko"
command = "show startup-config"

today = time.strftime('%Y%m%d')


iplist = 'hosts.txt'
#with open(iplist, 'r') as fp:
#    line = fp.readline()
#    while line:
#        host = ('{}'.format(line.strip()))
#        line = fp.readline()
        #print (host)
#        proc(host, usr, pwd)


with open(iplist,'r') as fp:
    host = [line.strip() for line in fp]
    host = ('{}'.format(line.strip()))
    #host = str(host)
    proc(host,usr,pwd)
       
