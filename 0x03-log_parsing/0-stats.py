#!/usr/bin/python3
"""
This is a simple module and it only has
one function called fun_name
"""
import re

IP_PATTERN = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
DATE_PATTERN = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}'
STATUS_CODE_PATTERN = r'(200|301|400|401|403|404|405|500)'


INPUT_FORMAT = r'{} - \[{}\] "GET /projects/260 HTTP/1.1" {}? \d+'.format(IP_PATTERN, DATE_PATTERN, STATUS_CODE_PATTERN)

def getStatusAndFileSize(input_text):
    """Gets the status code and file size from input text

    Args:
        input_text (_type_): _description_

    Returns:
        _type_: _description_
    """
    if(re.match(INPUT_FORMAT, input_text)):
        status_code = re.findall(STATUS_CODE_PATTERN, input_text)
        if not status_code:
            return None

        status_code = status_code[len(status_code) - 1]

        file_size = re.findall(r'\d+', input_text)
        file_size = file_size[len(file_size) - 1]

        return { 'status_code': status_code, 'file_size': int(file_size) }

    return None

def printLogData(log_dict, total_size):
    """_summary_

    Args:
        log_dict (_type_): _description_
        total_size (_type_): _description_
    """
    print(f'File size: {total_size}')
    for k, v in log_dict.items():
        print(f'{k}: {v}')

count = 0
log_dict = {}
total_size = 0

try:
    while True:
        input_text = input()
        log_data = getStatusAndFileSize(input_text)
        if not log_data:
            continue

        status_code = log_data['status_code']
        file_size = log_data['file_size']
        if status_code not in log_dict:
            log_dict[status_code] = 1
        else:
            log_dict[status_code] = log_dict[status_code] + 1

        total_size = total_size + file_size

        log_dict = {k: log_dict[k] for k in sorted(log_dict)}

        count = count + 1
        if count % 10 == 0:
            printLogData(log_dict, total_size)


except KeyboardInterrupt:
    printLogData(log_dict, total_size)

