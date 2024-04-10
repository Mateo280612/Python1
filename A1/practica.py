names = ['Mateo','Pepe','Juan','Jose','Tomas']
for i in names:
    print(i)

numbers = []
for i in range(500,1001):
    numbers.append(i)


numbers_2 = [i for i in range(500,1001)]


names2 = [ i.upper() for i in names]
numbers4 = []
print(names2)

#for i in names:
 #   numbers4.append(i.upper())

#print(numbers4)

#Tupla
names5 = ('Jose','Carlos')

person = {'name' : 'Josue','age':27}
for i in person:
    print(i,person[i])