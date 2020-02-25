class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.k=key*10
        self.a=alphabet*2
    
    def encode(self, text):
        result=''
        a=0
        for i in text:
            if i in self.a:
                result+=self.a[self.a.index(i)+self.a.index(self.k[a])]
                a+=1
            else:
                result+= i
                a+=1
        print(result)
    
    def decode(self, text):
        result=''
        a=0
        for i in text:
            if i in self.a:
                result+=self.a[self.a.index(i)-self.a.index(self.k[a])]
                a+=1
            else:
                result+= i
                a+=1
        print(result)
abc = "abcdefghijklmnopqrstuvwxyz";
key =input("Enter the key")
text= input("Enter the message: ")
c= VigenereCipher(key,abc)
p=input("Encode(1) or decode(2)")
if p==1:
    c.encode(text)
elif p==2:
    c.decode(text)
