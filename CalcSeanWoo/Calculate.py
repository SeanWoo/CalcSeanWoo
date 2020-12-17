import re
from Stack import *

mul = re.compile(r"(.*?)((-?\d*(\.\d+)?)[*](-?\d*(\.\d+)?))")
div = re.compile(r"(.*?)((-?\d*(\.\d+)?)/(-?\d*(\.\d+)?))")
add = re.compile(r"(.*?)((-?\d*(\.\d+)?)\+(-?\d*(\.\d+)?))")
sub = re.compile(r"(.*?)((-?\d*(\.\d+)?)-(-?\d*(\.\d+)?))")
mod = re.compile(r"(.*?)((-?\d*(\.\d+)?)\^(-?\d*(\.\d+)?))")

def parseFloat(string: str) -> int:
    if string.isdigit():
       return int(string)
    else:
        try:
            return float(string)
        except ValueError:
            return None

def validate(string: str):
    stack = Stack()
    
    for s in string:
        if s == '(':
            stack.push('(')
        elif s == ')':
            if stack.size == 0:
                return False
            stack.pop()
    return stack.size == 0


def getResult(string: str):
    rawString = string.replace(" ", "")

    operation = ""

    while True:
        if '^' in rawString:
            operation = '^'
        elif '*' in rawString or '/' in rawString:
            index1 = rawString.find('*') if not rawString.find('*') == -1 else 2147483647
            index2 = rawString.find('/') if not rawString.find('/') == -1 else 2147483647
            if index1 < index2:
                operation = '*'
            else:
                operation = '/'
        else:
            index1 = rawString.find('+') if not rawString.find('+') == -1 else 2147483647
            index2 = rawString.find('-') if not rawString.find('-') == -1 else 2147483647
            if index1 < index2:
                operation = '+'
            else:
                operation = '-'

        if '^' == operation:
            groups = re.match(mod, rawString)
            number1 = parseFloat(groups.group(3))
            number2 = parseFloat(groups.group(5))
            result = number1 ** number2
            rawString = re.sub(mod, r"\g<1>" + str(result), rawString, count=1)
            rawString = re.sub(r"--", "+", rawString)
        elif '*' == operation:
            groups = re.match(mul, rawString)
            number1 = parseFloat(groups.group(3))
            number2 = parseFloat(groups.group(5))
            result = number1 * number2
            rawString = re.sub(mul, r"\g<1>" + str(result), rawString, count=1)
            rawString = re.sub(r"--", "+", rawString)
        elif '/' == operation:
            groups = re.match(div, rawString)
            number1 = parseFloat(groups.group(3))
            number2 = parseFloat(groups.group(5))
            result = number1 / number2
            rawString = re.sub(div, r"\g<1>" + str(result), rawString, count=1)
            rawString = re.sub(r"--", "+", rawString)
        elif '+' == operation:
            groups = re.match(add, rawString)
            number1 = parseFloat(groups.group(3))
            number2 = parseFloat(groups.group(5))
            result = number1 + number2
            rawString = re.sub(add, r"\g<1>" + str(result), rawString, count=1)
            rawString = re.sub(r"--", "+", rawString)
        elif '-' == operation:
            groups = re.match(sub, rawString)
            number1 = parseFloat(groups.group(3))
            number2 = parseFloat(groups.group(5))
            result = number1 - number2
            rawString = re.sub(sub, r"\g<1>" + str(result), rawString, count=1)
            rawString = re.sub(r"--", "+", rawString)
        if not parseFloat(rawString) == None:
            break
    return parseFloat(rawString)

def parse(string: str):
    try:
        rawString = string.replace(" ", "")
        rawString = string.replace(",", ".")
        if not validate(rawString):
            return None
        stack = Stack()
        
        localExpression = ""
        startIndexExpression = 0
        endIndexExpression = 0
        counter = 0
        while ')' in rawString:
            if rawString[counter] == '(':
                if not localExpression == "":
                    localExpression = ""
            elif rawString[counter] == ')':
                if not localExpression == "":
                    endIndexExpression = counter + 1
                    result = getResult(localExpression)
                    rawString = rawString[0:startIndexExpression] + str(result) + rawString[endIndexExpression:len(rawString)]
                    localExpression = ""
                    counter = 0
                    continue
            else:
                if localExpression == "":
                    startIndexExpression = counter - 1
                localExpression += rawString[counter]
                
            counter += 1
        
        return getResult(rawString)
    except:
        return None

if __name__ == "__main__":
    if parse("(1467*43+2334/2-132*2+900/455+654389-15*10-59+15037)*0+2*6,5") == 13.0: 
        print("1 test passed")
    else: 
        print("Failed")

    if parse("2^2") == 4.0: 
        print("2 test passed") 
    else: 
        print("Failed")

    if parse("2^3") == 8.0: 
        print("3 test passed") 
    else: 
        print("Failed")

    if parse("2*2^3") == 16.0: 
        print("4 test passed") 
    else: 
        print("Failed")