import sys

def readNumber(line, index):
    "Identifies numbers in an equation."
    number = 0
    while index < len(line) and line[index].isdigit():
        number  = number * 10 + int(line[index])
        index  += 1
    if index    < len(line) and line[index] == '.':
        index  += 1
        keta    = 0.1
        while index < len(line) and line[index].isdigit():
            number += int(line[index]) * keta
            keta   *= 0.1
            index  += 1
    token = {'type': 'NUMBER', 'number': number}
    return token, index

def readPlus(line, index):
    "Identifies addition signs."
    token = {'type': 'PLUS'}
    return token, index + 1

def readMinus(line, index):
    "Identifies subtraction signs."
    token = {'type': 'MINUS'}
    return token, index + 1

def readMultiply(line, index):
    "Identifies multiplication signs."
    token = {'type': 'MULTIPLY'}
    return token, index + 1

def readDivide(line, index):
    "Identifies division signs."
    token = {'type': 'DIVIDE'}
    return token, index + 1

def readStartParenthesis(line, index):
    "Identifies start of a parenthesis."
    token = {'type': 'START'}
    return token, index + 1

def readEndParenthesis(line, index):
    "Identifies end of a parenthesis."
    token = {'type': 'END'}
    return token, index + 1


def tokenize(line):
    "Make tokens of an equation given."
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = readNumber(line, index)
        elif line[index] == '+':
            (token, index) = readPlus(line, index)
        elif line[index] == '-':
            (token, index) = readMinus(line, index)
        elif line[index] == '*':
            (token, index) = readMultiply(line, index)
        elif line[index] == '/':
            (token, index) = readDivide(line, index)
        elif line[index] == '(':
            (token, index) = readStartParenthesis(line, index)
        elif line[index] == ')':
            (token, index) = readEndParenthesis(line, index)
        else:
            print 'Invalid character found: ' + line[index]
            sys.exit()
        tokens.append(token)
    return tokens
    

def evaluate1(tokens):
    "Multiplication and division calculations."
    tokens.insert(0, {'type': 'PLUS'}) #Insert a dummy '+' token
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'MULTIPLY':
                a = tokens[index - 2]['number'] * tokens[index]['number']
                tokens[index] = {'type': 'NUMBER', 'number': a}
                tokens[index - 1] = tokens[index - 3]
                tokens[index - 2] = tokens[index - 3]
                index += 1
            if tokens[index - 1]['type'] == 'DIVIDE':
                a = tokens[index - 2]['number'] / tokens[index]['number']
                tokens[index] = {'type': 'NUMBER', 'number': a}
                tokens[index - 1] = tokens[index - 3]
                tokens[index - 2] = tokens[index - 3]
                index += 1
        index += 1
    return tokens


def evaluate2(tokens):
    "Addition and subtraction calculations."
    answer = 0
    index  = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type']   == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                print 'Invalid syntax'
        index += 1
    return answer


def parenthesisINDEX(tokens):
    "Returns positions of open and close parenthesis."
    index = 0
    s, e = [], []
    while index < len(tokens):
        if tokens[index]['type'] == 'START':
            s.append(index)
            index += 1
        if tokens[index]['type'] == 'END':
            e.append(index)
            index += 1
        else:
            index += 1
    return (s, e)
    
def parenthesis(tokens):
    "Calculates inside of a parenthesis and gets rid of parenthesis."
    s, e = parenthesisINDEX(tokens)[0], parenthesisINDEX(tokens)[1]
    if len(s) == 0:             #No parenthesis
        tokens = tokens
    else:
        while len(s) >= 1:
            a, b  = s[-1], e[0]
            tok   = tokens[(a+1):b]
            calc1 = evaluate1(tok)
            calc2 = evaluate2(calc1)
            new   = {'type': 'NUMBER', 'number': calc2}
            
            tokens[a] = new
            del tokens[(a+1):(b+1)]
            (s, e)    = parenthesisINDEX(tokens)
    return tokens


while True:
    print '> ',
    line       = raw_input()
    tokens     = tokenize(line)
    #print tokens
    priority   = parenthesis(tokens)
    #print priority
    simplified = evaluate1(tokens)
    #print simplified
    answer     = evaluate2(tokens)
    print "answer = %f\n" % answer