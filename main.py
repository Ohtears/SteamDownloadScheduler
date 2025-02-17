import subprocess

import time

from datetime import datetime


x = datetime.now()

print(x.strftime("%H")) 

while int(x.strftime("%H")) != 4: # timi ke garare downlaod start bshe
    x = datetime.now()
    # print('task badi')
print(f'Saat 4 shod')

command = 'start steam.exe'


run = subprocess.call(command, shell=True)

print('download starting...')