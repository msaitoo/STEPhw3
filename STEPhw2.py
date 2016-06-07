import numpy, sys, time, matplotlib.pyplot as pyplot

if (len(sys.argv) != 2):
    print "usage: python %s N" % sys.argv[0]
    sys.exit()

n = int(sys.argv[1])
a = numpy.zeros((n,n)) # Matrix A
b = numpy.zeros((n,n)) # Matrix B
c = numpy.zeros((n,n)) # Matrix C

#Initialise the matrices to some values.
for i in xrange(n):
    for j in xrange(n):
        a[i,j] = i * n + j
        b[i,j] = j * n + j
        c[i,j] = 0

begin = time.time()

for i in range(n):
    for j in range(n):
        elements = numpy.zeros(n)
        for k in range(n):
            elements[k] = a[i,k]*b[k,j]
        c[i,j] = sum(elements)

end = time.time()
print "time: %.6f sec" % (end - begin)

