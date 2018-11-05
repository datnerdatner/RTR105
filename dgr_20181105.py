fruit='banana'
print(len(fruit))
x=len(fruit)
print(x)
index = 0
while index<len(fruit):
    letter=fruit[index]
    print(index, letter)
    index = index+1
for letter in fruit:
    print(letter)
word='banana'
count=0
for letter in word:
    if letter=='a':
        count=count+1
print(count)
s='Monty Python'
print(s[0:4])
print(s[6:7])
print(s[6:20])
print(s[4:])
a='Hello'
b=a+'There'
print(b)
c=a+' '+'There'
print(c)
'n' in fruit
'm' in fruit
if 'a' in fruit:
    print('Found it!')
if word=='banana':
    print('All right')
if word<'banana':
    print('Your word,'+word+', comes before banana')
elif word>'banana':
    print('Your word'+word+'comes after banana')
else:
    print('all right, bananas')
greet='Hello Bob'
zap=greet.lower()
print(zap)
pos=fruit.find('na')
print(pos)
nnn=greet.upper()
print(nnn)
nstr=greet.replace('Bob','Jane')
print(nstr)
line='Please have a nice day'
line.startswith('Please')
