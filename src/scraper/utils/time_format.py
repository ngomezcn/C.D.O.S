from scraper.utils.array_utils import dirty_str_to_int

def time_since_added_to_date(list):
    formated_list = []
    
    for value in list:
        if 'hour' in value:
            formated_list.append(dirty_str_to_int(value))
        if 'hours' in value:
            formated_list.append(dirty_str_to_int(value))
        elif 'day' in value:
            formated_list.append(dirty_str_to_int(value))
        elif 'days' in value:
            formated_list.append(dirty_str_to_int(value))
            
    return formated_list

        
