# All about for loop in python how to use the for loop to create iteration
#  # c++ syntax [for (init i=0; i < 5; i++) {...} ] this does not exist in python though
# first let look at iterable in python An iterable in python is an object capable of returning values one at a time
# object in python that are iterable
   # list
   # tupple
   # strings etc
   # 
# so the for loop is some thing that allows us to iterate over iterables

# in python you can achiev the for loop using the while loop  wriet the C++ syntax above in python is 

i = 0 
while i < 5:
    print(i)
    i += 1
print("------------FOR RANGE--------------")

# but the for loop in python is use to iterate on an iterable like RANGE rg

for i in range(5):
    print(i)
print("-------------for LIST list denoated by square []-------------")
# for LIST
for i in [1,2,3,4]:
    print(i)

print("-------------for STRING-------------")
for c in 'hello':
    print(c)

print("-------------for Tupple tupple denoted by bracket()-------------")

for x in ('a','v','d',4,6):
    print(x)

print("-------------for Tupple tupple denoted by bracket() in list denoted by [] generate matrix-------------")
# how doe we handle matrix we can use teh list in combination with tupple in python to get matrix

for y in [(1,2),(4,6),('r','y')]:
    print(y)

print("-------------for Tupple tupple denoted by bracket() in list denoted by [] generate matrix-------------")
# deconstruction of the matrix
for j,k in [(1,2),(4,6),('r','y')]:
    print(j,k)

print("-------------using continue and breake -------------")

#continue
for i in range (5):
    if i == 3:
        continue
    print(i)
print ("-----------------------")
#break
for i in range (5):
    if i == 3:
        break
    print(i)

print ("-----------------------")

print("using the for  loop and the if  else statement to continue make math operation")

for i in range(1, 5):
    print(i)
    if i % 7 == 0:
        print("multiple of 7 found")
        break
    else:
        print("no multiple of 7 found")

print("--------------using the try catch block------------------")

for i in range (5):
    print("-------------")
    try:
        10/(i-3)
    except ZeroDivisionError:
        print ('divided by zero')
        continue 
    finally:
        print("always run")

# there multiple ways of iterating over iterable and  some of this iterable are indexable

     # object in python that are iterable and indexable
   # list
   # tupple
   # strings etc except for set set are iterable or dictionary with out index
   # note that dictionary has keys and values

s = 'hello'
i = 0
for c in s:
    print(i,c)
    i += 1 
    
print("--------------using the enumerat function------------------")
# we use the enumerate function which returns a tupple for  the above same code

s= 'hello'
for i,c in enumerate(s):
    print(i,c)