import math
a=input("Enter the plaintext: ")
ka=int(input("Enter the first key: "))
kb=int(input("Enter the second key: "))
result=''
for i in range(len(a)):
    if (a[i].isupper()):
        result+=chr((ka*(ord(a[i])-65)+kb)%26 +65)
    else:
        result+=chr((ka*(ord(a[i])-97)+kb)%26 +97)
print("The ciphertext is: "+result)
