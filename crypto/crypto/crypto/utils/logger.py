from os.path import exists
import os
from datetime import datetime

def sprint(*argv):
    print("\n")
    print("="*20)
    print("\n")
    
    rprint = ""
    for i in argv:
        rprint += ''.join(i)
        
    print(rprint, end=" ")
    log(rprint, sprint_log=True)
    
    print("\n")
    print("="*20)
    print("\n")
    print("\n")


def log(*argv, sprint_log = False):
    
    folder = "logs"
    master_log = folder + '/' + 'master.log'
    today_log = folder + '/' + str(datetime.today().strftime('%Y-%m-%d')) + '.log'
    
    if not exists(folder):
        os.mkdir(folder)
        
    if not exists(master_log):
        with open(master_log, 'w'): pass
        
    if not exists(today_log):
        with open(today_log, 'w'): pass
    
    flog = format_log(argv, sprint_log)

    write_to_file(master_log, flog)
    write_to_file(today_log, flog)

def write_to_file(file, str):
    file = open(file, 'a')
    file.write(str)
    file.close()
    
def format_log(argv, sprint_log):
    rlog = ""
    flog = ""
    
    if sprint_log:
        for i in argv:
            rlog += ''.join(i)
        flog = str(datetime.now().replace(microsecond=0)) + ": " + rlog + '\n'
        return flog
    else:
        for i in argv:
            rlog += str(i)
        flog = "(print) " + ''.join(datetime.now().replace(microsecond=0)) + ": " + rlog + '\n'
        return flog
    