a = int(input("Your mass (kg): "))
b = int(input("Your height (cm): "))
BMI = a/(b/100*b/100)
print("BMI:",BMI)
if BMI < 16 :
  print("Severely underweight")
elif BMI < 18.5 :
  print("Underweight")
elif BMI < 25 :
  print("Normal")
elif BMI < 30 :
  print("Overweight")
else:
  print("Obese")
