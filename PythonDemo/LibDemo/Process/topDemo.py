import subprocess
import os
import time

def funcLs():
    res = subprocess.check_output("ls -l", shell=True, cwd='f:/Src/CodeDemo')
    str = res.decode('utf-8')
    strs = str.split('\n')
    for s in strs:
        print(s)

if __name__ == "__main__":
    #res = subprocess.call("ls -l", shell=True)
    funcLs()
    '''
    while(True):
        func()
        print("\n\n")
        time.sleep(10)
    '''
