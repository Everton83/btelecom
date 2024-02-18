#!/usr/bin/python3

import os

result = os.popen('ps -ef | grep 177.153.51.75 | grep -v grep | wc -l').read()
result = int(result)

if result >= 2:
    print("url acessivel - Status 200")
else:
    os.system('systemctl restart django')
    print("url não esta acessivel")
