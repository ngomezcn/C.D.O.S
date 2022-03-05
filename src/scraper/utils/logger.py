from os.path import exists
import os
from datetime import datetime

def sprint(*argv):
    
    rprint = ""
    for i in argv:
        #rprint += ''.join(i).strip("\n")+" "
        pass
    
    print("="*len(rprint))
    log(rprint, sprint_log=True)
    print(rprint)
    print("="*len(rprint))


def log(*argv, sprint_log = False):
    return None
    
    root_folder = "logs"
    
    master_file = root_folder + '/' + 'master.log'
    today_file = root_folder + '/' + str(datetime.today().strftime('%Y-%m-%d')) + '.log'

    if not exists(root_folder):
        os.mkdir(root_folder)
        
    if not exists(master_file):
        with open(master_file, 'w'): pass
        
    if not exists(today_file):
        with open(today_file, 'w'): pass
    
    flog = format_log(argv, sprint_log)

    write_to_file(master_file, flog)
    write_to_file(today_file, flog)

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
    