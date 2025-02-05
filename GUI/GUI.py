import re
import Bussiness_Entities.Game_Entites as Bent
import Bussiness_Access_Layer.Game_Logics as Bal
obj_ent = Bent.C_Entites()
obj_bal = Bal.C_Game_Logics()
choice = "yes"
while choice == "yes":
    print("\033[1m"+"\nWelcome to the Game"+"\033[0m")
    print("1. PLAY\n2. View History\n3. EXIT")

    option1 = int(input("Enter your choice(1-2): "))


    if option1 == 1:
        print("\033[1m"+"NUMBER GUESSING GAME"+"\033[0m")

        name = input("Enter you name: ")
        if re.match("^[A-Za-z]+$", name):
            obj_ent.set_name(name)
        else:
            print("Please enter the valid name(Contains only alphabets).....!!!!")
            break

        age = int(input("Enter you age: "))
        obj_ent.set_age(age)

        print("\n\033[1mHi welcome to the game, This is a number guessing game.\n"
              "You got 7 chances to guess the number. \nLet's start the game\033[0m")

        lower_bound = int(input("Enter lower bound: "))
        obj_ent.set_lower_bound(lower_bound)

        upper_bound = int(input("Enter upper bound: "))
        obj_ent.set_upper_bound(upper_bound)

        random_number = obj_bal.random_number_generation(obj_ent)
        obj_ent.set_random_number(random_number)

        guess_counter=7
        while guess_counter>0:
            my_guess = int(input("Please Enter your Guess: "))
            obj_ent.set_guess_number(my_guess)
            data = obj_bal.game_logic(obj_ent)
            if data == "equal":
                print(f"WON.....The number is {random_number} and you found it right!!.")
                result1= "Won"
                obj_ent.set_result(result1)
                break
            elif data == "low":
                print("Your guess is lower.")
            elif data == "high":
                print("Your guess is higher.")
            elif data == "Out of higher bound":
                print("Out of Upper Bound Range.")
            elif data == "Out of lower bound":
                print("Out of Lower Bound Range.")
            guess_counter -= 1
        else:
            print(f'Oops sorry, The number is {random_number} better luck next time')
            result2 = "Lost"
            obj_ent.set_result(result2)
        obj_bal.insertion_DB(obj_ent)

    elif option1 == 2:
        data = obj_bal.history_DB()
        for counter in range(len(data)):
            print(data[counter])

    elif option1 == 3:
        break

    else:
        print("Please enter the correct option(1-2)....!!")

    choice = input("Do you want to play again(yes/no)?: ").lower()

else:
    print("THANKYOU........")
