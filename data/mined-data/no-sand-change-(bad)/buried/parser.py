import os
import numpy as np

is_first = True
with open('all.dat', 'w') as dst:
    for file in os.listdir():
        if '.py' in file or 'all' in file:
            continue
        print('writing ' + file + ' in all.dat')
        with open(file, 'r') as src:
            rows = []
            while True:
                line = src.readline()
                if line == '':
                    break
                if line[0] == '%':
                    continue
                first = 0 if is_first else 1
                row = line.split(',')[first:-1]
                rows.append(row)
            t = np.array(rows)
            for row in t.transpose():
                dst.write(','.join(row) + '\n')
            is_first = False
print('El Psy Congroo.')
