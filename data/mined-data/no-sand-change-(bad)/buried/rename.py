import os
files = os.listdir()
files.sort(key=os.path.getctime)

current = '000000'
for file in files:
    if '.py' not in file:
        current = str(int(current) + 1).zfill(6)
        print(file + ' -> ' + current + '.dat')
        os.rename(file, current + '.dat')
