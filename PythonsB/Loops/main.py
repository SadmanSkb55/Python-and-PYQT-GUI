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

