# looking at how condition works

# simple conditional ex 1
a = 2
if a <  5:
    print ('a < 5')
else:
    print('a >= 5 ')

# nested conditional ex 1

a = 10

if a < 5:
    print('a < 5')
else:
    if a < 10:
        print('5 <= a < 10')
    else:
        print('a => 10')
# equivalent of switch and case in other language is elif

a = 17

if a < 5:
    print('N')
elif a < 10:
    print('K')
elif a < 15:
    print('E')
elif a < 20:
    print('M')

# converting regular if else statement to tenary

#sample if
a = 25 

if a < 5:
    b = 'a < 5'
else:
    b = 'a >= 5'
print(b)

#convert to tenary operator
b = 'a < 5' if a < 5 else 'a >= 5'


