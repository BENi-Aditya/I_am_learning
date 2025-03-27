import random
# Rock

Rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
Paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
Scissor = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

user_choice = int(input(""" Choose Rock / Paper / Scissor \n
Rock = 1
Paper = 2
Scissor = 3\n """))


if user_choice == 1:
    print(Rock)
elif user_choice == 2:
    print(Paper)
else:
    print(Scissor)
    
                  
comp_choice = random.randint(1, 3)

if comp_choice == 1:
    print(Rock)
elif comp_choice == 2:
    print(Paper)
else:
    print(Scissor)


if user_choice == 2:
    if comp_choice == 1:
        print("Draw")
    elif comp_choice == 2:
        print("Computer Wins 😭 ")
    else:
        print("You Win 🤙🏻 ")

elif user_choice == 3:
    if comp_choice == 1:
        print("Computer Wins 😭 ")
    elif comp_choice == 2:
        print("You Win 🤙🏻 ")
    else:
        print("Draw")
        

# import random
# a = ["""    _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)""", 
#      """     _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)""", 
#      """    _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)"""]
# u = int(input("Rock(1) Paper(2) Scissor(3): ")) - 1; c = random.randint(0, 2)
# print(a[u], a[c], sep="\n"); print("Draw" if u == c else "You win 🤙🏻" if (u - c) % 3 == 1 else "Computer wins 😭")
