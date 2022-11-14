import random

user_name = input("What is your name ? ")
life = 5


print(f"Welcome to plus minus game {user_name}")

number_win = random.randrange(1, 49)

while True:
    user_number = int(input("What's the number ? "))
    if user_number == number_win:
        print("Congratulations your are win 🎉")
        break
    elif user_number > number_win:
        print("Is hight")
        life = life - 1
        print(f"rest life {life}")
        if life == 0:
            print("GAME OVER!!! 😔")
            break
        
    elif user_number < number_win:
        print("Is small")
        life = life - 1
        print(f"rest life {life}")
        if life == 0:
            print("GAME OVER!!! 😔")
            break
    else:
        print("incorrect value")
        
