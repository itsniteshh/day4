# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
import random

new_names = len(names)
#Write your code below this line 👇
random_name = random.randint(0, new_names -1)


if random_name == 0:
  print(f"{names[0]} you will be treating us today.")
elif random_name == 1:
  print(f"{names[1]} you will be treating us today.")
elif random_name == 2:
  print(f"{names[2]} you will be treating us today.")
else:
  print(f"{names[3]} you will be treating us today.")