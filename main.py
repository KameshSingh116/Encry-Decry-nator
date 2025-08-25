#This is gonna be a project to make an encryptor-decrypptor
import random
import getpass
print("Welcoome to the Encryptor-Decrypptor")
password=getpass.getpass("Enter your password :")
print("Encrypting....")
hashy=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
             'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
             '0','1','2','3','4','5','6','7','8','9']
token=['1','2','3','4','5','6','7','8','9','0']

print("Your password is encrypted!")
print("The encrypted hash value is :")
x=""
for i in range(0,26):
    x +=random.choice(hashy)
print(x)

print("\nYour access token was saved with its coorresponding hash value",end="")
y=''
for i in range(0,5):
    y +=random.choice(token)
    with open('tokens.txt','w') as f:
       f.write(f"Encrypted Hash: {x}\n")
       f.write(f"Access Token: {y}")


want=input("Doo you want to see the password?:(y/n)")
if(want=='y'):
    toky=input('Enter the access token:')
    if(toky==y):
        print("Your password is:")
        print(password)
    else:
        print("Wrong access token!")
        with open('tokens.txt','w') as f:
            f.write("")

else:
    exit()

