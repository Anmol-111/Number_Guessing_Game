import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import Bussiness_Entities.Game_Entites as Bent
import Bussiness_Access_Layer.Game_Logics as Bal

obj_ent = Bent.C_Entites()
obj_bal = Bal.C_Game_Logics()

def play_game():
    window = tk.Toplevel()
    window.title("Number Guessing Game")
    image = Image.open("C:\\Users\\Anmol\\Desktop\\istockphoto-1429079387-612x612.jpg")
    image = image.resize((800, 500), )
    bg_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(window, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.image = bg_image
    lbl_game_name = tk.Label(window, text="Number Guessing Game", font=("Roboto", 22, "bold"), fg="white",
                             bg="midnight blue", bd=5)
    lbl_game_name.place(x=240, y=30)

    messagebox.showinfo(
        message="Welcome to the game! You have 7 chances to guess the correct number.")

    guess_counter = 7
    my_guess = None  # Initializing the guess variable

    lbl_value = tk.Label(window, text="Enter your guess: ", font=("Roboto", 18, "bold"), fg="white",
                         bg="midnight blue", bd=5)
    lbl_value.place(x=60, y=200)

    en_value = tk.Entry(window, width=25, font=("Roboto", 18, "bold"))
    en_value.place(x=350, y=200)

    # Function to handle the logic of checking the guess
    def check_value():
        nonlocal guess_counter, my_guess

        my_guess = en_value.get()  # Get the user input
        try:
            my_guess = int(my_guess)  # Ensure the guess is an integer
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number.")
            return

        obj_ent.set_guess_number(my_guess)
        data = obj_bal.game_logic(obj_ent)

        if data == "equal":
            messagebox.showinfo(
                message=f"WON! The number is {obj_ent.get_random_number()} and you guessed it correctly!")
            result1 = "Won"
            obj_ent.set_result(result1)
            obj_bal.insertion_DB(obj_ent)
            window.quit()  # Exit the game loop if guessed correctly

        elif data == "low":
            messagebox.showinfo(message="Your guess is too low. Try a higher number.")
        elif data == "high":
            messagebox.showinfo(message="Your guess is too high. Try a lower number.")
        elif data == "Out of higher bound":
            messagebox.showinfo(message="Your guess is above the upper bound.")
        elif data == "Out of lower bound":
            messagebox.showinfo(message="Your guess is below the lower bound.")

        guess_counter -= 1  # Decrease guess counter after each attempt
        en_value.delete(0, tk.END)

        # Check if out of guesses
        if guess_counter == 0 and data != "equal":
            messagebox.showinfo(
                message=f"Out of attempts! The number was {obj_ent.get_random_number()}. Better luck next time!")
            result2 = "Lost"
            obj_ent.set_result(result2)
            obj_bal.insertion_DB(obj_ent)
            window.quit()  # End the game if no guesses left

    button1 = tk.Button(window, text="GO", width=25, font=("Roboto", 18, "bold"), bg="aquamarine", command=check_value,
                        bd=5)
    button1.place(x=210, y=300)
    window.mainloop()

def play():
    window = tk.Toplevel()
    window.title("Number Guessing Game")
    image = Image.open("C:\\Users\\Anmol\\Desktop\\istockphoto-1429079387-612x612.jpg")
    image = image.resize((800, 500), )
    bg_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(window, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.image = bg_image
    lbl_game_name = tk.Label(window, text="Number Guessing Game", font=("Roboto", 22, "bold"), fg="white",
                             bg="midnight blue", bd=5)
    lbl_game_name.place(x=240, y=30)

    lbl_name = tk.Label(window, text="Enter Your Name:", font=("Roboto", 18, "bold"), fg="white",
                             bg="midnight blue", bd=5)
    lbl_age = tk.Label(window, text="Enter Your Age:", font=("Roboto", 18, "bold"), fg="white",
                             bg="midnight blue", bd=5)
    lbl_lower_bound = tk.Label(window, text="Enter the Lower Bound:", font=("Roboto", 18, "bold"), fg="white",
                             bg="midnight blue", bd=5)
    lbl_upper_bound = tk.Label(window, text="Enter the Upper Bound:", font=("Roboto", 18, "bold"), fg="white",
                               bg="midnight blue", bd=5)

    en_name = tk.Entry(window, width= 25, font=("Roboto", 18, "bold"))
    en_age = tk.Entry(window, width= 25, font=("Roboto", 18, "bold"))
    en_upper_bound = tk.Entry(window, width= 25, font=("Roboto", 18, "bold"))
    en_lower_bound = tk.Entry(window, width=25, font=("Roboto", 18, "bold"))

    def submit_info():
        name = en_name.get()
        age = en_age.get()
        lower_bound = en_lower_bound.get()
        upper_bound = en_upper_bound.get()
        obj_ent.set_name(name)
        obj_ent.set_age(age)
        obj_ent.set_lower_bound(lower_bound)
        obj_ent.set_upper_bound(upper_bound)
        random_no = obj_bal.random_number_generation(obj_ent)
        obj_ent.set_random_number(random_no)
        play_game()

    button1 = tk.Button(window, text="GO", width=25, font=("Roboto", 18, "bold"), command=submit_info, bg="aquamarine", bd=5)

    lbl_name.place(x=60, y=150)
    en_name.place(x=350, y=150)
    lbl_age.place(x=60, y=200)
    en_age.place(x=350, y=200)
    lbl_lower_bound.place(x=60, y=250)
    en_lower_bound.place(x=350, y=250)
    lbl_upper_bound.place(x=60, y=300)
    en_upper_bound.place(x=350, y=300)
    button1.place(x=210, y=350)

    window.mainloop()

def game_history():
    window = tk.Toplevel()
    window.title("Number Guessing Game")
    image = Image.open("C:\\Users\\Anmol\\Desktop\\istockphoto-1429079387-612x612.jpg")
    image = image.resize((800, 500), )
    bg_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(window, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.image = bg_image
    lbl_game_name = tk.Label(window, text="Number Guessing Game", font=("Roboto", 22, "bold"), fg="white",
                             bg="midnight blue", bd=5)
    lbl_game_name.place(x=240, y=30)
    Listbox = tk.Listbox(window, height=8, width=50, font=("Roboto", 15, "bold"))
    Listbox.place(x=50, y=50)

    data = obj_bal.history_DB()
    if data is None:
        messagebox.showerror(message="No History....Play the Game Now.")
    else:
        for value in data:
            Listbox.insert(tk.END, value)
    window.mainloop()

def game_exit():
    if messagebox.askyesno(message="Do you want to exit from the game?"):
        window.quit()

def main_page():
    global window
    window = tk.Tk()
    window.title("Number Guessing Game")
    image = Image.open("C:\\Users\\Anmol\\Desktop\\istockphoto-1429079387-612x612.jpg")
    image = image.resize((800, 500), )
    bg_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(window, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.image = bg_image
    lbl_game_name =  tk.Label(window, text="Number Guessing Game", font=("Roboto", 22, "bold"), fg="white", bg="midnight blue", bd=5)
    lbl_game_name.place(x=240, y=30)
    button1 = tk.Button(window, text="PLAY", width=25, font=("Roboto", 18, "bold"),command=play, bg="aquamarine", bd=5)
    button2 = tk.Button(window, text="HISTORY", width=25, font=("Roboto", 18, "bold"), command=game_history, bg="aquamarine", bd=5)
    button3 = tk.Button(window, text="EXIT", width=25, font=("Roboto", 18, "bold"), command=game_exit, bg="aquamarine", bd=5)
    button1.place(x=220, y=150)
    button2.place(x=220, y=230)
    button3.place(x=220, y=310)
    window.mainloop()

if __name__ == "__main__":
    main_page()