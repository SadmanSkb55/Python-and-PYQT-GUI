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