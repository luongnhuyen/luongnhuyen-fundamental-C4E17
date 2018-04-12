Mass = int(input("Your mass (kg): "))
Height = int(input("Your height (m): "))
BMI = int(Mass/(Height*height))

If BMI < 16 :
  Print("Severely underweight")
elif BMI < 18.5 :
  Print("Underweight")
elif BMI < 25 :
  Print("Normal")
elif BMI < 30 :
  Print("Overweight")
else:
  Print("Obese")
