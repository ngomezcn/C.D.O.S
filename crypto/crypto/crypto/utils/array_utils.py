from operator import truediv
from tokenize import String
from crypto.utils.logger import log

def erase_line_jump(arr):
    
    for i in range(len(arr)):
        arr[i] = arr[i].strip("\n")
        
    return arr

def is_over_a_day(str):
    if str != '1 day':
        if 'hour' in str:
            return True

    return False