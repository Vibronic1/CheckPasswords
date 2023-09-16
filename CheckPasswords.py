import re
import sys


if len (sys.argv) == 2:
        f= open(sys.argv[1],'r')
if len (sys.argv) < 3:
    print ("Ошибка. Слишком мало параметров.")
    sys.exit (1)

if len (sys.argv) > 3:
    print ("Ошибка. Слишком много параметров.")
    sys.exit (1)

param_name = sys.argv[1]
param_value = sys.argv[2]

if (param_name == "--File" or
        param_name == "-f"):
    f = open(param_value,'r')
else:
    print ("Ошибка. Неизвестный параметр '{}'".format (param_name) )
    sys.exit (1)

for line in f:
    if (re.search('[!@#$%&]',line)!= None and len(line)>8 and re.search('a-z',line)!= None and re.search('A-Z',line)!= None and re.search('0-9',line)!= None):
        print (line)
    else
        print ("pass is too weak")
