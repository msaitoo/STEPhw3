import numpy, sys, time, matplotlib.pyplot as pyplot

if (len(sys.argv) != 2):
    print "usage: python %s N" % sys.argv[0]
    sys.exit()

def initiate(z):
    '''
    Initiates square matrices to be multiplied.
            z = dimension
    '''
    a = numpy.zeros((z,z))     # Matrix A
    b = numpy.zeros((z,z))     # Matrix B
    c = numpy.zeros((z,z))     # Matrix C (result of multiplication)
    
    for i in xrange(z):        #Initialise the matrices to some values.
        for j in xrange(z):
            a[i,j] = i * z + j
            b[i,j] = j * z + i
            c[i,j] = 0
    return (a,b,c)

def matrix(q):
    '''
    Multiplies two square matrices.
            q = dimension
    Gives:
            c = Resultant matrix
            t = time taken for calculation
    '''
    a, b, c = initiate(q)[0], initiate(q)[1], initiate(q)[2]
    begin = time.time()                      #Initial time
    for i in range(q):
        for j in range(q):
            elements = numpy.zeros(q)
            for k in range(q):               #Sigma summation
                elements[k] = a[i,k]*b[k,j]
            c[i,j] = sum(elements)           #Elements in c
    end = time.time()                        #End time
    t = end - begin                          #Get time difference in time
    return (c,t)

#Result of multiplication
n = int(sys.argv[1])
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
def graph(x):
    x = x+1
    pyplot.figure(); ax = pyplot.subplot()
    X, Y = numpy.zeros(x), numpy.zeros(x)
    for y in range(x):
        t = matrix(y)[1]
        X[y], Y[y] = y, t
    ax.plot(X,Y)
    ax.set_xlabel('$\mathrm{Dimension (N)}$', fontsize=20)
    ax.set_ylabel('$\mathrm{Time}$', fontsize=20)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    #ax.set_title('Matrix multiplication: process time', fontsize=20)
    return pyplot.show()