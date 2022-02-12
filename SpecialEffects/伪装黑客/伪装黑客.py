import random
import os
from time import sleep

os.system('color 4')
index = 0
while True:
    print(random.randrange(0,3),end='')
    if index % 100 == 0:
        sleep(0.01)
        print()
    index += 1