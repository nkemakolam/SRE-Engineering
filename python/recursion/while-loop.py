# while loop keeps executing until the contion is false
i = 0
while i < 5:
    print(i)
    i +=1
# here we need the code to execute once before the condition like in the order programming language where you have do while
# use case 1 1
j = input('what is your name ')

while True:
    print('nkemakolam')
    if len(j)< 5:
        print(j)
        break
# use case 2
min_length = 2
name = input("please enter you name: ")

while not ( len(name) >= min_length and name.isprintable() and name.isalpha()):
    name = input("pleae enter your name: ")
print ("hello, {0}".format(name))

# use case  2 refactored
min_length = 2

while True: 
    name = input("pleae enter your name: ")
    if len(name) >= min_length and name.isprintable() and name.isalpha():
        break
   
print ("hello, {0}".format(name))

# use case 3 is continue  key word

a = 0 

while a < 10:
    a += 1
    if a % 2 == 0:
        continue
    print(a)

#use case 5 the else of the while loop

l = [1,2,3]
val = 10
found = False
idx = 0
while idx < len(l):
    if l[idx] == val:
        found = True
        break
    idx += 1
if not found:
    l.append(val)
print (l)
  
#use case 5 the else of the while loop refoactor
m = [1,2,3,10]
val = 10
idx = 0
while idx < len(m):
    if m[idx] == val:
        break
    idx += 1
else:
    m.append(val)
print (m)

#break and continuous and the try Statement

# in the try...except...finally , finally continoues even if the except runs
# Demo for try
a = 10
b = 1
try:
    a/b 
except ZeroDivisionError:
    print('dividion by zero') 
finally:
    print("alway execute")

#let use while loop to run  break and  finally

a = 0
b = 2

while a < 4 :
    print('--------------------')
    a += 1
    b -= 1
    try:
        a/b
    except ZeroDivisionError:
      print("{0}, {1} - division by 0".format(a,b))
      continue
    finally:
        print("{0}, {1} - these always execute".format(a,b)) 

    print("{0}, {1} - main loop".format(a,b))
  

