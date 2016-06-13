import sys

def readNumber(line, index):
    number = 0
    while index < len(line) and line[index].isdigit():
        number = number * 10 + int(line[index])
        index += 1
    if index < len(line) and line[index] == '.':
        index += 1
        keta = 0.1
        while index < len(line) and line[index].isdigit():
            number += int(line[index]) * keta
            keta *= 0.1
            index += 1
    token = {'type': 'NUMBER', 'number': number}
    return token, index


def readPlus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1


def readMinus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1


def readMultiply(line, index):
    token = {'type': 'MULTIPLY'}
    return token, index + 1


def readDivide(line, index):
    token = {'type': 'DIVIDE'}
    return token, index + 1


def tokenize(line):
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
        else:
            print 'Invalid character found: ' + line[index]
            sys.exit()
        tokens.append(token)
    return tokens


def priority1(tokens):
    index = 0
    while index < len(tokens):
        if tokens[index]['type'] == 'MULTIPLY':
            a = tokens[index - 1]['number'] * tokens[index + 1]['number']
            tokens[index] = {'type': 'NUMBER', 'number': a}
            try:
                tokens[index - 1] = tokens[index - 2]
                tokens[index + 1] = tokens[index + 2]
                index = index + 1
            except IndexError:
                tokens[index - 1] = {'type': 'PLUS'}
                tokens[index + 1] = {'type': 'PLUS'}
                index = index + 1
        elif tokens[index]['type'] == 'DIVIDE':
            a = tokens[index - 1]['number'] / tokens[index + 1]['number']
            tokens[index] = {'type': 'NUMBER', 'number': a}
            try:
                tokens[index - 1] = tokens[index - 2]
                tokens[index + 1] = tokens[index + 2]
                index = index + 1
            except IndexError:
                tokens[index - 1] = {'type': 'PLUS'}
                tokens[index + 1] = {'type': 'PLUS'}
                index = index + 1
        else:
            index = index + 1
    return tokens


def evaluate(tokens):
    answer = 0
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    index = 1
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                print 'Invalid syntax'
        index += 1
    return answer


while True:
    print '> ',
    line = raw_input()
    tokens = tokenize(line)
    priority = priority1(tokens)
    #print priority
    answer = evaluate(priority)
    print "answer = %f\n" % answer