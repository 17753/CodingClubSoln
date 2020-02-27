import sys 
words = []
num = 0 
loop = True
#def validation():
#   try:
#        num = int(input())
#        return validation()
#    except  ValueError:
#        num = int(input("invalid input please enter an input: "))
#    return validation()
num = int(input("please enter the number of words in the list: "))
#validation()
while loop:
    if num == 0:
        loop = false
        print("thank you!")
        sys.exit()
    elif 2 < num < 100:
        loop = False
        for i in range(0,num,1):
            word = str(input("please input word number " + str(i+1))) 
            words.append(word)
    else:
        num = int(input("invalid input please enter an input: "))
    
words = sorted(words)
print(words[0])
                


        
