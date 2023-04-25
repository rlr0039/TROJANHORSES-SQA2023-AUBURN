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
    value = ''
    value1 = ''
    value2 = ''
    for i in range(5):
        try:
            if i == 0:
                methodTest = 'scanner.py constructHelmString integer'
                value = 0
                result = constructHelmString(value)
            if i ==1:
                methodTest = 'scanner.py getYAMLFiles None object'
                value = None
                result = getYAMLFiles(value)
            if i == 2:
                methodTest = 'scanner.py getItemFromSecret boolean and None values'
                value1 = True
                value2 = None
                result = getItemFromSecret(value1, value2)
            if i == 3:
                methodTest = 'parser.py checkIfValidHelm integer'
                value = 500
                result = checkIfValidHelm(value)
            if i == 4:
                methodTest = 'parser.py readYAMLAsStr integer'
                value = 500
                result = readYAMLAsStr(value)
        except Exception as temp:
            print('Fuzzing: ' + methodTest)
            print('\nFuzz values:')
            if i != 2:
                print(value)
            if i == 2:
                print(value1)
                print(value2)
            print('\nResult:')
            print(temp)
            print('='*100)
            print('\n')

def simpleFuzzer():
    fuzzValues()

if __name__=='__main__':
    simpleFuzzer()
