import re
from Stack import *

mul = re.compile(r"(.*?)((\d*(\.\d+)?)[*](-?\d*(\.\d+)?))")
div = re.compile(r"(.*?)((\d*(\.\d+)?)/(-?\d*(\.\d+)?))")
add = re.compile(r"(.*?)((\d*(\.\d+)?)[+](-?\d*(\.\d+)?))")
sub = re.compile(r"(.*?)((\d+(\.?\d+)?)\-(\d+(\.?\d+)?))")
mod = re.compile(r"(.*?)((\d*(\.\d+)?)\^(-?\d*(\.\d+)?))")

def parseFloat(string: str) -> int:
    string = string.replace('−', '-')
    if string.isdigit():
       return int(string)
    else:
        try:
            return float(string)
        except ValueError:
            return None

def cleaningString(string: str):
    rawString = string.replace(" ", "")
    rawString = rawString.replace("\n", "")
    rawString = rawString.replace("\t", "")
    rawString = rawString.replace(",", "")
    rawString = rawString.replace("=", "")
    rawString = rawString.replace("×", "*")
    rawString = rawString.replace("÷", "/")
    return rawString

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
    rawString = string

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
            index2 = rawString.find('-', 1) if not rawString.find('-', 1) == -1 else 2147483647
            if index1 < index2 or (rawString[0] == '-' and not index1 == 2147483647):
                operation = '+'
            else:
                operation = '-'

        if '^' == operation:
            groups = re.match(mod, rawString)
            number1 = parseFloat(groups.group(3))
            number2 = parseFloat(groups.group(5))
            minus = ""
            result = number1 ** number2
            #За это спасибо Александру Попенову
            if number1 < 0 and number2 < 0:
                minus = "-"
            if number1 < 0 and number2 % 2 == 0:
                result = -result
            #За это спасибо Александру Попенову
            rawString = re.sub(mod, r"\g<1>" + minus + str(result), rawString, count=1)
            rawString = re.sub(r"--", "+", rawString)
        elif '*' == operation:
            groups = re.match(mul, rawString)
            number1 = parseFloat(groups.group(3))
            number2 = parseFloat(groups.group(5))

            index = rawString.find(f"{str(number1)}*{str(number2)}")
            if index == 1 and rawString[0] == '-':
                number1 = number1 * -1
                rawString = rawString.replace("-", "", 1)

            result = number1 * number2
            rawString = re.sub(mul, r"\g<1>" + str(result), rawString, count=1)
            rawString = re.sub(r"--", "+", rawString)
        elif '/' == operation:
            groups = re.match(div, rawString)
            number1 = parseFloat(groups.group(3))
            number2 = parseFloat(groups.group(5))

            index = rawString.find(f"{str(number1)}/{str(number2)}")
            if index == 1 and rawString[0] == '-':
                number1 = number1 * -1
                rawString = rawString.replace("-", "", 1)

            result = number1 / number2
            rawString = re.sub(div, r"\g<1>" + str(result), rawString, count=1)
            rawString = re.sub(r"--", "+", rawString)
        elif '+' == operation:
            groups = re.match(add, rawString)
            number1 = parseFloat(groups.group(3))
            number2 = parseFloat(groups.group(5))

            index = rawString.find(f"{str(number1)}+{str(number2)}")
            if index == 1 and rawString[0] == '-':
                number1 = number1 * -1
                rawString = rawString.replace("-", "", 1)

            result = number1 + number2
            rawString = re.sub(add, r"\g<1>" + str(result), rawString, count=1)
            rawString = re.sub(r"--", "+", rawString)
        elif '-' == operation:
            groups = re.match(sub, rawString)
            number1 = parseFloat(groups.group(3))
            number2 = parseFloat(groups.group(5))

            index = rawString.find(f"{str(number1)}-{str(number2)}")
            if index == 1 and rawString[0] == '-':
                number1 = number1 * -1
                rawString = rawString.replace("-", "", 1)

            result = number1 - number2
            rawString = re.sub(sub, r"\g<1>" + str(result), rawString, count=1)
            rawString = re.sub(r"--", "+", rawString)
        if not parseFloat(rawString) == None:
            break
    return parseFloat(rawString)

def parse(string: str):
    try:
        rawString = cleaningString(string)
        
        if not validate(rawString):
            return None
        
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
        if parseFloat(rawString):
            return parseFloat(rawString)
        else:
            return getResult(rawString)
    except Exception as ex:
        print(ex)
        return None

if __name__ == "__main__":
    #print(parse("-5 + 3"))
    print(parse("( ( 56   ^   2   +   44 )   ^   2   -   ( 25   ×   2 )   ^   2 )   ÷   2 ="))
    print("5054950")
