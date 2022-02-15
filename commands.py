myName =" KrishBrilliant"
#print(myName)
age=13
#print(age)

#knowAge = int(input("Tell me your age?"))
#print(knowAge)

#if(knowAge>=18):
 #       print("you are elegible")

#elif(knowAge>=16):
 #       print("you are not elegible ")
#else:
  #      print("you are kid")        

#myFriendList = ["aaa", "bbb", "ccc"]
#print(myFriendList)


#for i in myFriendList:
  #  print(i)

#while loop is executed until the condition become satisfied
#count = 5
#while(count>=0):
        #print(count)
        #count = count -1


knowAge = input("Tell me about yourself?")
characterCount = 0
wordCount =1

for i in knowAge:
    characterCount = characterCount +1
    print(characterCount)

    if(i==' '):
        wordCount = wordCount +1

print("Number of word")
print(wordCount)
print("Number of Characters")
print(characterCount)