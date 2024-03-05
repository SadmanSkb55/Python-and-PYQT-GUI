birthyear=input('birth year=')
print(type(birthyear))
nowage=2019-int(birthyear)#typecasted
print(type(nowage))
print(nowage)

weighlbs=input('Weight in pouds: ')
weighkg=float(weighlbs)*0.45
print("weight in KGs: " + str(weighkg))

stringh="Sadman's Workstation"
stringg='is not that good'
stringf='which is not for "Beginners"'
print(stringh+' '+stringg+" "+stringf)

strx='''
hi,
this is sadman.
nice to meet you

'''
print(strx)
stry='hello pepoll'
print(stry[3])
print(stry[-4])
#print(stry[37])
print(stry[0:4])
print(stry[3:])
print(stry[:6])
another=stry[:]
print(another)
print(stry[1:-1])

first="Kurt"
Last="Cobain"
message=first+' {'+Last+'} is a coder'
msg=f'{first} [{Last}] is a programmer'
print(message)
print(msg)