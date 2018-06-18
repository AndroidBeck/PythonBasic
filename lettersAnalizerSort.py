# -*- coding: cp1251 -*-
__author__ = 'Evdokimov'

letters_ru = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
letters_en = 'abcdefghijklmnopqrstuvwxyz'

filename1 = "D:\py\caseinalowercaseletters.txt"
filename2 = "D:\py\Симулянты.txt"

letters = letters_ru
filename = filename2

with open(filename, "r") as f:
    text = f.read()

dic = {}
for c in letters:
    dic[c] = 0
dic[0] = 0

all_sum = 0
letters_sum = 0
for c in text.lower():
    if c in letters:
        dic[c] += 1
        letters_sum += 1
    else:
        dic[0] += 1
    all_sum += 1

# Sorting
sorted_letters = sorted(dic, key=lambda k: dic[k], reverse=True)
# print ', '.join(sorted_letters)

print(sorted_letters)

for c in sorted_letters:
    if c != 0:
        percentage = float(dic[c]) / letters_sum * 100
        print("{0} : {1} ({2}%)".format(c, dic[c], round(percentage, 2)))

print ('LetterSumm: ' + str(letters_sum))
print('---\nnone: {0}'.format(dic[0]))
print ('Summ: ' + str(all_sum))
