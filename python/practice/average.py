print("hello")
total = 0
count = 0
user_input= input("type number which you want to calculate the average(type q to quit): ")
while user_input != "q":
    num = float(user_input)
    total += num
    count = count + 1
    user_input =input("type number which you want to calculate the average(type q to quit): ")
if count == 0:
    result =0
else:
    result =  total / count
print ("average: " + str(result))
    

