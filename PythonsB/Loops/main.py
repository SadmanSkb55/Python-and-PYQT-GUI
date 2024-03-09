i=1
while i<=10:
    print(i//2)
    i+=1
    if i==5:
        print(i)
        break
print("GG")
i=1
while i<=10:
    print('^'*i  )
    i+=1

for item in 'Sougo':
    print(item)
for item in ['A',"Axz",'GG']:
    print(item)
for i in range(10):
    print(i)
for i in range(5,100,2):
    print(i)
prices=[10,20,40]
total=0
for price in prices:
    total+=price
print(f'Total: {total}')

for x in range(5):
     for y in range (5):
         print(f'x:{x} y:{y}')
num=[5,2,5,3,5,4]
for c in num:
    output=''
    for cx in range(c):
        output+='x'
    print(output)