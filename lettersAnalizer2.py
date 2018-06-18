# -*- coding: cp1251 -*-
__author__ = 'Evdokimov'

letters_ru = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
letters_en = 'abcdefghijklmnopqrstuvwxyz'

filename1 = "D:\py\caseinalowercaseletters.txt"
filename2 = "D:\py\Симулянты.txt"

letters = letters_en
filename = filename1

# Tryig to open file
try:
    filename = input("Enter a filename (use commas):\n")
    f = open(filename, "r")
    print "File opened for reading.."
except:
    print "Error occured in process of opening file: "
    raise StandardError

# Trying to get correct input
lang = str("")
try:
    lang = input("Enter text language: 0 - russian, english otherwise:\n")
    if lang == 0:
        letters = letters_ru
except:
    letters = letters_en
    print "Default ", lang
finally:
    print "Using alphabet: ", letters

dic = {}
for c in letters:
    dic[c] = 0
dic[0] = 0

all_sum = 0
letters_sum = 0

for line in f:
    for c in line.lower():
        if c in letters:
            dic[c] += 1
            letters_sum += 1
        else:
            dic[0] += 1
        all_sum += 1

# Tryig to close file
try:
    f.close()
    print "File closed."
except:
    print "Error occured while closing file.."
    raise StandardError

if letters_sum != 0:
    # Sorting
    sorted_letters = sorted(dic, key=lambda k: dic[k], reverse=True)
    print(sorted_letters)

    for c in sorted_letters:
        if c != 0:
            percentage = float(dic[c]) / letters_sum * 100
            print("{0} : {1} ({2}%)".format(c, dic[c], round(percentage, 2)))

    print ('LetterSumm: ' + str(letters_sum))
    print('---\nnone: {0}'.format(dic[0]))
    print ('Summ: ' + str(all_sum))

else:
    print("No such letters as {0} in the text: {1}".format(letters, filename))
