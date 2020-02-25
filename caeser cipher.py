a=input("Enter the plaintext: ")
a=a.trim()
k=int(input("Enter the key: "))
result=''
for i in range(len(a)):
    if (a[i].isupper()):
        result+=chr((ord(a[i])+k-65)%26 +65)
    else:
        result+=chr((ord(a[i])+k-97)%26 +97)
        
print("The ciphertext is: "+result)
