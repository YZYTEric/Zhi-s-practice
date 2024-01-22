while True:
    a = input("a, have you ever stolen anything? ")
    b = input("b, have you ever stolen anything? ")
    if a == "yes" and b == "yes":
        print("a and b are guity!")
    elif a =="yes" and b == "no":
        print("a is a honest person, b needs more punish.")
    elif a =="no" and b =="yes":
        print(" a needs more punish, b is a honest person.")
    elif a =="no" and b =="no":
        print("a and b both are liers, they need more punish!")
        break
    else:
        print("you only can answer yes or no!")