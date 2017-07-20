#
#print my_first_function()

#A = 3
#B = A


#L = [22, True, "Una Lista", [1 , 2]]
#print L[3]

#T = (22, True, "Una Lista", (1 , 2))
#print L[3]

#D = {"kill Bill" : "Tamarino", "Amelie" : "Jean-Pierre Jeunet"}
#print D["Amelie"]


#print int(4.3)
#print float(4.0)
#print str(4.3)
#print list((4 , 5, 2))


#print len("key")
#print type(4)
#print map(str, [1, 2, 3, 4])
#print round(6.3243, 1)
#print range(5)
#print sum([1, 2, 4])
#print sorted([5, 2, 1])
#print dir([5, 2, 1])
#print help(sorted)

class Estudiante(object):
    def __init__(self, nombre_r, edad_r):
        self.nombre = nombre_r
        self.edad = edad_r

    def hola(self):
        return "Mi nombre es %s y tengo %i" % (self.nombre, self.edad)


e = Estudiante("Julio", 24)
print e.hola()

print cmp(8, 6)

a = 5
b = 5

if(a > b):
    print "a is more big than b."
elif(a == b):
    print "a and b are the same."
else:
    print "a is more small than b."


for i in range(10):
    print i

x = 0
while x < 10:
    print x;
    x += 1
