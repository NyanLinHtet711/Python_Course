kg = float(input("Enter your weight in kilograms: "))
m = float(input("Enter your height in meters: "))
BMI = kg/(m**2)

if BMI < 18.5:
    print ("Your BMI is " + "{:.2f}".format(BMI) + " ,you are underweight.")
elif BMI >= 18.5 and BMI < 25:
    print ("Your BMI is " + "{:.2f}".format(BMI) + " ,you are normal.")
elif BMI >=25 and BMI < 30:
    print ("Your BMI is " + "{:.2f}".format(BMI) + " ,you are overweight.")
elif BMI >= 30:
    print ("Your BMI is " + "{:.2f}".format(BMI) + " ,you are obese.")
