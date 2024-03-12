def greetuser():
    print("Hello User")
def greetuser2(name):
    print(f'Hello {name}')

def greetuser3(name,username):
    print(f'Hello {name} of {username}')

print("Welcome")
greetuser()
greetuser2("Johnathan")
username=input("Username: ")
name=input("Name: ")
greetuser3(name,username)

#totalcalc()....u cant summon it here

def total_calc(total,vat,discount):
    print(f'Total= {total+(total*vat)-(total*discount)}')

total_calc(100,0.05,0.01)

total_calc(total=110,vat=0.15,discount=0.05)#keyword argument

def runner(num1,num2):
    return num1*num1*num2

numx=int(input("Enter a number= "))
cond=input("1.Square 2.Cube =")
if cond=='1':
     print(runner(numx,1))
elif cond=='2':
    print(runner(numx,numx))
else:
    print("Invalid")

def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😀",
        ":(": "😞",
        ":D": "😄",
        ":O": "😲",
        ";)": "😉",
        ":P": "😛",
        "<3": "❤️",
        ":|": "😐",
        ":*": "😘",
        ":/": "😕"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message=input(">")
print(emoji_converter(message))