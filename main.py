# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


total = weight / (height ** 2)

if total < 18.5:
  print("Slightly underweight")
elif total < 25:
  print("normal weight")