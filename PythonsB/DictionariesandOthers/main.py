user={
    "Name":'Adolf Kittler',
    "User_Name":"HitlerCar69",
    "Password":"KillRats@1945",
    "Age":7,
    "is_Verified":True
}
print(user["User_Name"])
print(user["Name"])
#print(user["name"])//will show error
print(user.get("Birthdate"))
print(user.get("Birthdate","Jan 1,1980"))
print(user.get("Birthdate"))
user["Name"]="Adolf Kettlee"
print(user["Name"])
user["Birthdate"]="Jan 1,1980"
print(user["Birthdate"])

number=input("Number: ")
digit_mapping={
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
output=""
for ch in number:
    output+=digit_mapping.get(ch,"!")+" "
print(output)

message=input(">")
words=message.split(' ')
print(words)