import subprocess

from datetime import datetime

x = datetime.now()

print(x.strftime("%H")) 

while int(x.strftime("%H")) != 4: 
    x = datetime.now()

print(f'It is now 4o Clock')

command = 'start steam.exe'

run = subprocess.call(command, shell=True)

print('Download starting...')