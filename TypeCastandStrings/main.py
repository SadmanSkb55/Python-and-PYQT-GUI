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