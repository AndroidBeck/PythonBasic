# -*- coding: cp1251 -*-

import msvcrt
import sys
import time

count = 0
start = 0

while True:
    c = msvcrt.getch()
    while not c in ' \r\n':
        if not count:
            start = time.clock()
            print '\n started'
        count += 1
        c = msvcrt.getch()
        sys.stdout.write(c)
    stop = time.clock()
    print '\n stoped'
    
    print
    print int((count + 1)/ (stop - start) * 60)
    
    count = 0






