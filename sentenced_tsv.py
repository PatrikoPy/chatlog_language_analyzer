import csv
import cld2

with open('WoWLog.tsv', 'w', newline='', encoding='utf-8-sig') as tsv_file:
    tsv_writer = csv.writer(tsv_file, delimiter='\t')
with open('WoWChatlog.txt', 'r', encoding='utf-8-sig') as file:
    for line in file:
        tsv_list = ['', '', '', '', '']
        tsv_list[0] = line[0:18].rstrip(' ')
        line = line[18:].lstrip(' ')
        if line.startswith('['):
            tsv_list[3] = line[1:line.index(']')]
            line = line[line.index(']') + 1:].lstrip(' ')
            tsv_list[1] = line[:line.index(':')]
            tsv_list[2] = (line[line.index(':'):].lstrip(': ')).rstrip('\n')
        elif 'says:' in line:
            tsv_list[3] = 'Say'
            tsv_list[1] = line.split('says:', 1)[0].strip()
            tsv_list[2] = line.split('says:', 1)[1].strip(' \n')
        elif 'yells:' in line:
            tsv_list[3] = 'Yell'
            tsv_list[1] = line.split('yells:', 1)[0].strip()
            tsv_list[2] = line.split('yells:', 1)[1].strip(' \n')
        else:
            continue
        lang_details = cld2.detect(tsv_list[2])
        tsv_list[4] = (lang_details[2][0][1])
        # tsv_list[4] = (lang_details) #pełne info o języku

        with open('WoWLog.tsv', 'a', newline='', encoding='utf-8-sig') as tsv_file:
            tsv_writer = csv.writer(tsv_file, delimiter='\t')
            tsv_writer.writerow([tsv_list[0], tsv_list[1], tsv_list[2], tsv_list[3].rstrip('\n'), tsv_list[4]])
