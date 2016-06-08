import numpy, sys, time, matplotlib.pyplot as pyplot

if (len(sys.argv) != 2):
    print "usage: python %s N" % sys.argv[0]
    sys.exit()

n = int(sys.argv[1])
def initiate(n):
    a = numpy.zeros((n,n)) # Matrix A
    b = numpy.zeros((n,n)) # Matrix B
    c = numpy.zeros((n,n)) # Matrix C
    
    #Initialise the matrices to some values.
    for i in xrange(n):
        for j in xrange(n):
            a[i,j] = i * n + j
            b[i,j] = j * n + i
            c[i,j] = 0
    return (a,b,c)
a = initiate(n)[0]
b = initiate(n)[1]
c = initiate(n)[2]

def matrix(n):
    begin = time.time()
    for i in range(n):
        for j in range(n):
            elements = numpy.zeros(n)
            for k in range(n):
                elements[k] = a[i,k]*b[k,j]
            c[i,j] = sum(elements)
    end = time.time()
    t = end - begin
    return (c,t)
c = matrix(n)[0]

print "time: %.6f sec" % (matrix(n)[1])

total = 0
for i in xrange(n):
    for j in xrange(n):
        #print c[i,j]
        total += c[i,j]
print "sum: %.6f" % total

#############################################################

pyplot.figure()
pyplot.title("Relationship between N and process time")
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