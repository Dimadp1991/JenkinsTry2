import os
import sys
import threading
import time
import paramiko
import getpass
from scp import SCPClient


# my ubuntu ip 10.0.0.10

class HostDataPrinter(threading.Thread):
    def __init__(self, h_url, h_fp, username, password):
        self.host_url = h_url
        self.host_fp = h_fp
        self.host_username = username
        self.host_password = password
        threading.Thread.__init__(self)  # super class
        self.threadID = threading.current_thread().ident

    def run(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.host_url, 22, self.host_username, self.host_password)

        my_code = ''
        with open('code_to_run.py', 'r') as program:
            my_code = program.read()

        with SCPClient(ssh.get_transport()) as scp:
            scp.put('code_to_run.py', 'code_to_run2.py')
            scp.get('code_to_run2.py')
        stdin, stdout, stderr = ssh.exec_command('python3 code_to_run2.py ' + self.host_fp)
        lines = stdout.readlines()
        print('Thread Id is: ' + str(self.threadID))
        for line in lines:
            print(line)

        ssh.exec_command('rm code_to_run2.py')


def main():
    # host_url = input("Please Enter a valid Host Url: ")
    # host_fp = input("Please Valid file Path: ")
    # host_username = input("Please Enter UserName: ")
    # host_password = getpass.getpass(prompt='Password: ', stream=None)
    # my_host = HostDataPrinter(host_url, host_fp, host_username, host_password)
    my_host = HostDataPrinter('10.0.0.10', '/etc', 'dimadp', 'dimadp')
    my_host.start()
    my_host.join()


if __name__ == "__main__":
    main()
