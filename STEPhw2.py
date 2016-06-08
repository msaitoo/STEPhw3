import numpy, sys, time, matplotlib.pyplot as pyplot

if (len(sys.argv) != 2):
    print "usage: python %s N" % sys.argv[0]
    sys.exit()

def initiate(n):
    '''
    Initiates matrices to be multiplied.
    n = dimension of square matrices.
    '''
    a = numpy.zeros((n,n))     # Matrix A
    b = numpy.zeros((n,n))     # Matrix B
    c = numpy.zeros((n,n))     # Matrix C (result of multiplication)
    
    for i in xrange(n):        #Initialise the matrices to some values.
        for j in xrange(n):
            a[i,j] = i * n + j
            b[i,j] = j * n + i
            c[i,j] = 0
    return (a,b,c)

#Initiate matrices with given dimension.
n       = int(sys.argv[1])
a, b, c = initiate(n)[0], initiate(n)[1], initiate(n)[2]

def matrix(n):
    '''
    Multiplies two matrices.
    n = dimension of square matrices.
    Gives:
            c = Resultant matrix
            t = time taken for calculation
    '''
    begin = time.time()                      #Initial time
    for i in range(n):
        for j in range(n):
            elements = numpy.zeros(n)
            for k in range(n):               #Sigma summation
                elements[k] = a[i,k]*b[k,j]
            c[i,j] = sum(elements)           #Elements in c
    end = time.time()                        #End time
    t = end - begin                          #Get time difference
    return (c,t)

#Result of multiplication
c = matrix(n)[0]
print "time: %.6f sec" % (matrix(n)[1])

#Sum of elements in c
total = 0
for i in xrange(n):
    for j in xrange(n):
        #print c[i,j]
        total += c[i,j]
print "sum: %.6f" % total

###########################Graphing###########################

pyplot.figure()
pyplot.title("Relationship between N and time")
pyplot.ylabel('time', fontsize = 11)
pyplot.xlabel('N')
x = 30
X, Y = numpy.zeros(x), numpy.zeros(x)

for y in range(x):
    a = initiate(y)[0]
    b = initiate(y)[1]
    c = initiate(y)[2]
    t = matrix(y)[1]
    X[y] = y
    Y[y] = t
pyplot.plot(X,Y)

pyplot.tight_layout()
pyplot.show()