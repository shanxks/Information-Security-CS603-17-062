a=input("Enter the ciphertext: ")
ka=int(input("Enter the first key: "))
kb=int(input("Enter the second key: "))
result=''
for i in range(len(a)):
    if (a[i].isupper()):
        result+=chr((ord(a[i])-65)-kb)/ka)%26 + 65)
    else:
        result+=chr((ord(a[i])-97)-kb)/ka)%26 + 97)
print("The plaintext is: "+result)
