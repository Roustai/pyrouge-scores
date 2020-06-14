import re
import glob
import csv
import statistics as stat

#Checks system positives with gold standard
def positive_test(system, gold):
    value = 0
    for line in system:
        for i in range(len(gold)):
            if line in gold[i]:
                print(line)
                value = value + 1

    return value

#First thing we will do is to gather all of the data regarding the
mod_file_list = glob.glob('/home/alex/rouge_test/GS/*.txt')
list.sort(mod_file_list)


#Next thing to do is to open up the files 1-by-1 and get the scores
for i in range(len(mod_file_list)):
    tot_pos = 0
    pos_list = []

    system_pos = []

    #General Stats
    with open(mod_file_list[i], 'r') as t:
        text_model = t.read()

    for line in text_model.split('\n'):
        if line != '':
            if line[-1] == '1':
                tot_pos = tot_pos + 1
                pos_list.append(line.split('1')[0].strip())

    print('file: ', mod_file_list[i].strip('/home/alex/rouge_test/GS/gold_standard.A.'))
    f = open('/home/alex/place_holder/' + 'gold_standard.A.00' + str(i+1) + '.txt', 'w+')
    for items in pos_list:
        f.write(items + '\n')
