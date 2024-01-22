answer = input("I am a magic cat. My name is nunu, do you need help?(need/not): ")
if answer =="need":
    number= int(input("what kinds of help do you need? 1. help you to do homework. 2. help you to cook. 3. talking with you. what's your choice: "))

    if number is 1:
        print(" no way, it's your business.")
    
    elif number is 2:
        print(" just use you phone to make a order!")
    
    elif number is 3:
        answer1 = input("what topics do you want to talk?")
        print("I dont want to talk with you, i need to learn python!!!")
    
else:
    print("great!")

print("bye,bye")