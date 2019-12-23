

# lsit
#dict = {"country":["Brazil","Russia"],"capital":["Brasilia","Masco"],"area":[10,20],"population":[100,200]}

#import pandas as pd


#brics = pd.DataFrame(dict)
#print(brics)   

#brics.index = ["BR", "RU"]
#print(brics)   
    

#list comprehensions

sentense = "the quick brown fox jumps over the lazy dog"
words = sentense.split()
word_length=[]

for word in words:
    if word != "the":
        word_length.append(len(word))
       # print(word)
       # print(len(word))
       #print(words)
        print(word_length)
        print("=========")

# example 2
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist=[]

for x in numbers:
   if x>0:
        newlist.append(x)
        print(newlist)