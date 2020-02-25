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
        return result
    
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
        return result
