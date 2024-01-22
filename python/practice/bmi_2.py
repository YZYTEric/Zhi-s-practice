def calculate_BMI(weight, height):
    BMI = weight / height **2
    if BMI <= 18.5:
        category = ("thin")
        print(f"you belong to: {category}")
    elif BMI <= 25:
        category = ("normal")
        print(f"you belong to: {category}")
    else:
        category = ("fat")
        print (f"you belong to: {category}")
    return BMI

calculate_BMI(60,1.83)