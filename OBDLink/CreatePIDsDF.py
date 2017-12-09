
# coding: utf-8

# In[40]:

import string
import pandas
printable = set(string.printable)
printable.remove('\n')
printable.remove('#')


# In[42]:

def CreatePIDsDF(filename):
    starttime = ''
    fuelcalcmethod = ''
    colnames = []
    rows = []

    with open(filename) as f:
        i = 0
        for line in f:
            if i == 0:
                starttime = ''.join(filter(lambda x: x in printable, line))
            if i == 1:
                fuelcalcmethod = ''.join(filter(lambda x: x in printable, line))
            if i == 2:
                colnames = [x.strip() for x in line.split(',')]
            if i > 2:
                rows.append([float(x.strip()) for x in line.split(',')])
            i = i + 1
    
    
    df = pandas.DataFrame(rows, columns=colnames)
    
    return {'StartTime': starttime,
            'FuelCalcMethod': fuelcalcmethod,
           'ts': df}


# In[ ]:



