
print("Hello Okita")
print("*"*10)
print("\n?"*10+" "*10+"\?"*10 )
intvar=10#int
floatvar=20.98#float
strvar=" Okita"#string
strvar2="Sougo"
boolvar=True#boolean
#charvar='d'
listvar=[1,2,3,4] #ordered,mutable list
tuplevar=(5,6,7,8) #ordered,immutable
setvar={9,10,11,12 } #unorderd,mutable,unique
frozensetvar=frozenset([13,14,15,16]) #immutable,unorderd set,frozenset() is a constructor
dictionaryvar= {'key1': 'value1', 'key2': 'value2'} #un-orderd key value pairs,unique keys(must)
nonevar=None #special value null,default

value=100
value=200
print(value*4)
print(intvar+6)
print(floatvar/3)
print(strvar2+strvar+" Sougo"*3)
print(listvar)
print(tuplevar)
print(setvar)
print(frozensetvar)
print(dictionaryvar)
print(nonevar)

name=str(input("Enter your name"))
age=int(input("Enter your age"))
ID=float(input("enter your float id"))
cond=bool(input("Are you dumb?(True/False)"))
#print(name+"\n"+age+"\n"+ID+"\n"+cond)
print(f"{name}\n{age}\n{ID}\n{cond}")


