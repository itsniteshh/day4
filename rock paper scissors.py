import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
img = [rock, paper, scissors]
user_choice = int(input("choose your input: 0 for rock, 1 for paper and 2 for scissor:\n "))

if user_choice == 0:
  print(f"You chose: Rock = {img[0]}")
elif user_choice == 1:
  print(f"You chose: Papers = {img[1]}")
elif user_choice == 2:
  print(f"You chose: scissors = {img[2]}")



choices = [ 
  '''rock =
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
,
'''papers =
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
,
'''scissors = 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
]

computer_choice = random.choice(choices)
print(f"computer chose: {computer_choice}")

#debug below part in my own way later

"""computer_choice = random.randint(0,2)
if computer_choice == 0:
  print(f"computer chose: {computer_choice}")


print(f"computer chose: {computer_choice}")

if user_choice == 0 and computer_choice == 2:
  print("You win")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice == computer_choice:
  print("Match drawn")
elif user_choice == 2 and computer_choice == 0:
  print("You lose")
elif user_choice == 1 and computer_choice == 2:
  print("You win")"""