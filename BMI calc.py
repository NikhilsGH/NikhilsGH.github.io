weight = 0
height = 0 
name = ""

def bmi():
    global weight 
    global height 
    global name
    name = input("Name: ")
    weight = int(input("weight (kg): "))
    height = float(input("height (m): "))
    thebmi = round((weight/ (height ** 2)), 2)
    if thebmi > 28: 
        return name + " you are overweight: " + str(thebmi)
    elif thebmi < 20:
        return name + " you are underweight: " + str(thebmi)
    else:
        return name + " you are healthy: " + str(thebmi)
    
print(bmi())
