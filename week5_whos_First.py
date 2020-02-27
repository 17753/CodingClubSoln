import sys 
words = []
num = 0 
loop = True
i = 0
first_word = []
def validation():
    try:
        num = int(input("how many words are there in the list: "))
        return num
    except ValueError:
        num = int(input("Please input an valid number: "))
num = int(input("how many words are there in the list: ")) 
while loop:
   if 2 <= num <= 100:
        loop= False
        while i !=num:
            i +=1
            word = str(input("please input word number " + str(i) + ": ")) 
            words.append(word) 
        words = sorted(words)
        first_word.append(words[0])
        if i == num:
            loop = True
            i = 0
            words = []
            num = int(input("how many words are there in the list: "))
   elif num == 0:
            print("thank you")
            break
   else:
       validation()
for i in range(len(first_word)):
    print(first_word[i])


                


        
