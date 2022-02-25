from os.path import exists
import os
from datetime import datetime

def sprint(*argv):
    print("\n")
    print("="*20)
    print("\n")
    for i in argv:
        print(i, end=" ")
        
    print("\n")
    print("="*20)
    print("\n")
    print("\n")


def log(*argv):
    
    folder = "logs"
    master_log = folder + '/' + 'master_log.txt'
    today_log = folder + '/' + 'master_log.txt'
    
    if not exists(folder):
        os.mkdir(folder)
        
    if not exists(master_log):
        with open(master_log, 'w'): pass
        
    if not 
    
    #log = open('logs/log.txt', 'a')
    
    #log.write(+str+'\n')
    #log.close()
    
log()