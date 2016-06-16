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

def readPower(line, index):
    "Identifies powers on a number."
    token = {'type': 'POWER'}
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
        elif line[index] == '^':
            (token, index) = readPower(line, index)
        else:
            print 'Invalid character found: ' + line[index]
            sys.exit()
        tokens.append(token)
    return tokens


def Power(tokens):
    "Power calculations."
    index = 0
    while index < len(tokens)-1:
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index + 1]['type']   == 'POWER':
                tokens[index]['number'] = tokens[index]['number']**tokens[index + 2]['number']
                tokens[index + 1] = {'type': 'PLUS'}
                tokens[index + 2] = {'type': 'PLUS'}
        index += 1
    return tokens


def PlusAndMinus(tokens):
    "Addition and subtraction calculations."
    tokens.insert(0, {'type': 'PLUS'})                         #Insert a dummy '+' token
    answer = 0
    index  = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type']   == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            #else:
                #print 'Invalid syntax'
        index += 1
    return answer


def MultiplyAndDivide(tokens):
    "Multiplication and division calculations."
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'MULTIPLY':
                result = tokens[index - 2]['number'] * tokens[index]['number']
                tokens[index - 2] = {'type': 'NUMBER', 'number': result}
                tokens[index - 1] = {'type': 'PLUS'}
                tokens[index]     = {'type': 'PLUS'}
                index += 1
            if tokens[index - 1]['type'] == 'DIVIDE':
                result = tokens[index - 2]['number'] / tokens[index]['number']
                tokens[index - 2] = {'type': 'NUMBER', 'number': result}
                tokens[index - 1] = {'type': 'PLUS'}
                tokens[index]     = {'type': 'PLUS'}
                index += 1
        index += 1
    return tokens


def parenthesisINDEX(tokens):
    "Returns lists of indices of start and end of parenthesis."
    index      = 0
    start, end = [], []                                         #List indices of ( and )
    while index < len(tokens):
        if tokens[index]['type'] == 'START':
            start.append(index)
            index += 1
        elif tokens[index]['type'] == 'END':
            end.append(index)
            index += 1
        else:
            index += 1
    return (start, end)

def parenthesis(tokens):
    "Calculates inside of a parenthesis and gets rid of parenthesis."
    start, end = parenthesisINDEX(tokens)[0], parenthesisINDEX(tokens)[1]
    if len(start) != len(end):
        print "Invalid use of parenthesis."
        sys.exit()
    if len(start) == 0:                                         #No parenthesis
        tokens = tokens
    else:
        while len(start) >= 1:                                  #Until no ()
            if start[-1]   <= end[0]:                           #((( ))) form
                op, cl = start[-1], end[0]
            elif start[-1] >= end[0]:                           #( )*( ) form
                op, cl = start[0], end[0]
            tok     = tokens[(op+1):cl]
            kakewari   = MultiplyAndDivide(tok)
            tasihiki   = PlusAndMinus(kakewari)
            inside     = {'type': 'NUMBER', 'number': tasihiki}
            tokens[op] = inside                                 #Replace with answer
            del tokens[(op+1):(cl+1)]                           #Delete used tokens
            (start, end) = parenthesisINDEX(tokens)             #Re-index ()
    return tokens


def evaluate(tokens):
    kakko      = parenthesis(tokens)                            #Get rid of parenthesis
    simplified = MultiplyAndDivide(kakko)                       #Get rid of * and /
    return PlusAndMinus(simplified)


while True:
    print '> ',
    line       = raw_input()
    tokens     = tokenize(line)
    answer     = evaluate(tokens)
    print "answer = %f\n" % answer