'''
Trojan Horses
April 17, 2023
Fuzzing methods and values
'''

# imports
from scanner import getItemFromSecret
from scanner import getYAMLFiles
from graphtaint import constructHelmString
from parser import checkIfValidHelm
from parser import readYAMLAsStr

def fuzzValues():
    result = ''

    # scanner.py constructHelmString integer
    #result = constructHelmString(0)
    # scanner.py getYAMLFiles None object
    #result = getYAMLFiles(None)
    # scanner.py getItemFromSecret boolean and None values
    #result = getItemFromSecret(True, None)
    # parser.py checkIfValidHelm integer
    #result = checkIfValidHelm(500)
    # parser.py readYAMLAsStr integer
    #result = readYAMLAsStr(500)

    print(result)
    print('='*100)

def simpleFuzzer():
    fuzzValues()

if __name__=='__main__':
    simpleFuzzer()