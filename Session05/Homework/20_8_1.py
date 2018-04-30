# text = input("Enter your data:").lower()
text = "ThiS is String with Upper and lower case Letters".lower()

dict={}

for i in text:
    dict[i]=dict.get(i,0)+1
alphabet=list(dict.items())
alphabet.sort()
alphabet.pop(0)

for value in alphabet:
    print(*value,end="\n")
