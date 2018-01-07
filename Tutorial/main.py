import os
cwd = os.getcwd() #make sure your file is in that working directory
import numpy as np
import pandas as pd
mydata = pd.read_csv('ALL_MERGE_CLEAN.csv', delimiter=',')
ver_multi = (
    (0,1,2,3,4,5,6,7,8,9),
    (1,2,3,4,0,6,7,8,9,5),
    (2,3,4,0,1,7,8,9,5,6),
    (3,4,0,1,2,8,9,5,6,7),
    (4,0,1,2,3,9,5,6,7,8),
    (5,9,8,7,6,0,4,3,2,1),
    (6,5,9,8,7,1,0,4,3,2),
    (7,6,5,9,8,2,1,0,4,3),
    (8,7,6,5,9,3,2,1,0,4),
    (9,8,7,6,5,4,3,2,1,0))
ver_perm = (
    (0,1,2,3,4,5,6,7,8,9),
    (1,5,7,6,2,8,3,0,9,4),
    (5,8,0,3,7,9,6,1,4,2),
    (8,9,1,6,0,4,3,5,2,7),
    (9,4,5,3,1,2,6,8,7,0),
    (4,2,8,6,5,7,3,9,0,1),
    (2,7,9,3,8,0,6,4,1,5),
    (7,0,4,6,9,1,3,2,5,8))
ver_inv = (0,4,3,2,1,5,6,7,8,9)
def calcsum(number):
    """Generates a Verhoeff checksum digit"""
    c = 0
    for i, item in enumerate(reversed(str(number))):
        c = ver_multi[c][ver_perm[(i+1)%8][int(item)]]
    return ver_inv[c]
def checksum(number):
    """Produces a Verhoeff digit and returns number followed with the checksum digit"""
    c = 0
    for i, item in enumerate(reversed(str(number))):
        c = ver_multi[c][ver_perm[i % 8][int(item)]]
    return c

def generateVerhoeff(number):
    """Generates the Verhoeff checksum digit after the original number"""
    return "%s%s" % (number, calcsum(number))

def validateVerhoeff(number):
    """This code validates Verhoeff checksummed number, where the last one is the check digit"""
    return checksum(number) == 0

mydata["Result"] = ""
print(validateVerhoeff(203247362983))

for i in (range(len(mydata))):
    """Per coding law, we set the 0 as the code that is verified as CORRECT, and 1 as those are wrong, and 2 as coding error (user refused)"""
    if mydata.loc[i,'biometricid'] < 100000000000:
        mydata.loc[i,'Result'] = 2
    elif validateVerhoeff(mydata.loc[i, 'biometricid']) == True:
        mydata.loc[i, 'Result'] = 0
    else:
        mydata.loc[i,'Result'] = 1
print(mydata)
mydata.to_csv('idresult.csv', sep=',', encoding='utf-8')