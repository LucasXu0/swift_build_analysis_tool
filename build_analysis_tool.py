#!/usr/bin/python
# -*- coding:utf8 -*-
import sys
import os

xcactivitylog_file_path = sys.argv[1]

# 1. unzip xcactivitylog
os.system('gunzip -c $1 > origin_build_time.log ' + xcactivitylog_file_path)

# 2. convert file ending from CR to CRLF
WINDOWS_LINE_ENDING = b'\r\n'
UNIX_LINE_ENDING = b'\r'

file_path = 'origin_build_time.log'

with open(file_path, 'rb') as open_file:
    content = open_file.read()

content = content.replace(UNIX_LINE_ENDING, WINDOWS_LINE_ENDING)

with open(file_path, 'wb') as open_file:
    open_file.write(content)

# 3. filter *.ms
os.system("grep '^\d*\.\d*ms' origin_build_time.log > build_time.log")

# 4. handle result
with open('build_time.log', 'rb') as open_file:
    total_time = 'total_time'
    times = 'times'
    file_func__time = {}

    for line in open_file.readlines():
        # 4.1 split line: time file func
        split_line = line.split('\t', 1)
        time_str = split_line[0]
        time = float(time_str.replace('ms', ''))
        file_func = split_line[1].replace('\r\n', '')
        if file_func__time.has_key(file_func): # if key exist, append time
            file_func__time[file_func][total_time] += time
            file_func__time[file_func][times].append(time)
        else: # if key not exist, new one
            file_func__time[file_func] = {
                total_time: time,
                times: [time]
            }

    # convert dic to tuple
    time_file_func_count = []
    for key, value in file_func__time.items():
        time_file_func_count.append((value[total_time], key, len(value[times]), value[times]))

    sorted_time_file_func_count = sorted(time_file_func_count, reverse=True)

    for item in sorted_time_file_func_count:
        # time + file + func + total_count + times
        print str(item[2]) + '\t' +  '%.1f' % (item[0]/item[2]) + 'ms\t' + item[1].replace('\t', '  ')

os.system('rm origin_build_time.log')
os.system('rm build_time.log')