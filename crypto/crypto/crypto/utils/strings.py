def erase_line_jump(arr):
    
    for i in range(len(arr)):
        arr[i] = arr[i].strip("\n")
        
    return arr

