import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import Bussiness_Entities.Game_Entites as Bent
import Bussiness_Access_Layer.Game_Logics as Bal

obj_ent = Bent.C_Entites()
obj_bal = Bal.C_Game_Logics()


def show_main_window():
    main_window.deiconify()

def show_last_window():
    window.deiconify()

def hide_current_window(window):
    window.withdraw()


def play_game():  # Destroy the last window
    global window1
    window1 = tk.Toplevel()
    window1.title("Number Guessing Game")
    image = Image.open("istockphoto-1429079387-612x612.jpg")
    image = image.resize((800, 500), )
    bg_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(window1, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.image = bg_image
    lbl_game_name = tk.Label(window1, text="Number Guessing Game", font=("Roboto", 22, "bold"), fg="white",
                             bg="midnight blue", bd=5, relief="solid", pady=5, padx=5)
    lbl_game_name.place(x=240, y=30)

    guess_counter = 7
    my_guess = None

    lbl_value = tk.Label(window1, text=f"Enter your guess{guess_counter - 8}: ", font=("Roboto", 18, "bold"), fg="white",
                         bg="midnight blue", bd=5)
    lbl_value.place(x=60, y=200)

    en_value = tk.Entry(window1, width=25, font=("Roboto", 18, "bold"))
    en_value.place(x=350, y=200)

    tk.Label(window1,
             text="Welcome to the game! You have 7 chances to guess the correct number.", font=("Roboto", 15, "bold"),
             fg="white", bg="midnight blue", bd=5, relief="solid", pady=5,
             padx=5).place(x=50, y=90)

    tk.Label(window1,
             text=f"Lower Bound: {obj_ent.get_lower_bound()} Upper Bound: {obj_ent.get_upper_bound()}", font=("Roboto", 15, "bold"),
             fg="white", bg="midnight blue", bd=5, relief="solid", pady=5,
             padx=5).place(x=250, y=130)

    def check_value():
        nonlocal guess_counter, my_guess
        my_guess = en_value.get()
        try:
            my_guess = int(my_guess)
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number.")
            return

        obj_ent.set_guess_number(my_guess)
        data = obj_bal.game_logic(obj_ent)

        if data == "equal":
            tk.Label(window1,
                     text=f"WON! The number is {obj_ent.get_random_number()} and you guessed it correctly!",
                     font=("Roboto", 20, "bold"), fg="white", bg="midnight blue", bd=10).place(x=60, y=300)
            result1 = "Won"
            obj_ent.set_result(result1)
            obj_bal.insertion_DB(obj_ent)
            window.quit()
        elif data == "low":
            tk.Label(window1,
                     text="Your guess is too low. Try a higher number.", font=("Roboto", 18, "bold"), fg="white",
                     bg="red", bd=5).place(x=150, y=400)
        elif data == "high":
            tk.Label(window1,
                     text="Your guess is too high. Try a lower number.", font=("Roboto", 18, "bold"), fg="white",
                     bg="red", bd=5).place(x=150, y=400)
        elif data == "Out of higher bound":
            tk.Label(window1,
                     text="Your guess is above the upper bound.", font=("Roboto", 18, "bold"), fg="white",
                     bg="red", bd=5).place(x=150, y=400)
        elif data == "Out of lower bound":
            tk.Label(window1,
                     text="Your guess is below the lower bound.", font=("Roboto", 18, "bold"), fg="white",
                     bg="red", bd=5).place(x=80, y=400)

        guess_counter -= 1
        en_value.delete(0, tk.END)

        if guess_counter == 0 and data != "equal":
            messagebox.showinfo(
                message=f"Out of attempts! The number was {obj_ent.get_random_number()}. Better luck next time!")
            result2 = "Lost"
            obj_ent.set_result(result2)
            obj_bal.insertion_DB(obj_ent)
            window1.quit()

    button1 = tk.Button(window1, text="GO", width=25, font=("Roboto", 18, "bold"), bg="aquamarine", command=check_value,
                        bd=5)
    Back_button = tk.Button(window1, text="BACK", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window1), show_last_window()], bg="orange", bd=5)
    Home_button = tk.Button(window1, text="HOME", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window1), show_main_window()], bg="orange", bd=5)
    Exit_button = tk.Button(window1, text="EXIT", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [window1.destroy(), window.destroy(), main_window.destroy()], bg="orange", bd=5)
    Back_button.place(x=10, y=450)
    Home_button.place(x=352, y=450)
    Exit_button.place(x=660, y=450)
    button1.place(x=210, y=300)
    window1.mainloop()


def play():  # Destroy the last window
    global window
    window = tk.Toplevel()
    window.title("Number Guessing Game")
    image = Image.open("istockphoto-1429079387-612x612.jpg")
    image = image.resize((800, 500), )
    bg_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(window, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.image = bg_image
    lbl_game_name = tk.Label(window, text="Number Guessing Game", font=("Roboto", 22, "bold"), fg="white",
                             bg="midnight blue", bd=5, relief="solid", pady=5, padx=5)
    lbl_game_name.place(x=240, y=30)

    lbl_name = tk.Label(window, text="Enter Your Name:", font=("Roboto", 18, "bold"), fg="white",
                        bg="midnight blue", bd=5)
    lbl_age = tk.Label(window, text="Enter Your Age:", font=("Roboto", 18, "bold"), fg="white",
                       bg="midnight blue", bd=5)
    lbl_lower_bound = tk.Label(window, text="Enter the Lower Bound:", font=("Roboto", 18, "bold"), fg="white",
                               bg="midnight blue", bd=5)
    lbl_upper_bound = tk.Label(window, text="Enter the Upper Bound:", font=("Roboto", 18, "bold"), fg="white",
                               bg="midnight blue", bd=5)

    en_name = tk.Entry(window, width=25, font=("Roboto", 18, "bold"))
    en_age = tk.Entry(window, width=25, font=("Roboto", 18, "bold"))
    en_upper_bound = tk.Entry(window, width=25, font=("Roboto", 18, "bold"))
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

    button1 = tk.Button(window, text="GO", width=25, font=("Roboto", 18, "bold"), command=lambda: [hide_current_window(window), submit_info()], bg="aquamarine",
                        bd=5)
    Home_button = tk.Button(window, text="HOME", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window), show_main_window()], bg="orange", bd=5)
    Exit_button = tk.Button(window, text="EXIT", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [window.destroy(), main_window.destroy()], bg="orange", bd=5)
    Home_button.place(x=10, y=450)
    Exit_button.place(x=660, y=450)
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


def game_history():  # Destroy the last window
    global window
    window = tk.Toplevel()
    window.title("Number Guessing Game")
    image = Image.open("istockphoto-1429079387-612x612.jpg")
    image = image.resize((800, 500), )
    bg_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(window, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.image = bg_image
    lbl_game_name = tk.Label(window, text="Number Guessing Game", font=("Roboto", 22, "bold"), fg="white",
                             bg="midnight blue", bd=5, relief="solid", pady=5, padx=5)
    lbl_game_name.place(x=240, y=30)
    Listbox = tk.Listbox(window, height=12, width=63, font=("Roboto", 15, "bold"))
    scrollbar = tk.Scrollbar(window)
    Listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=Listbox.yview)
    Home_button = tk.Button(window, text="HOME", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [hide_current_window(window), show_main_window()], bg="orange", bd=5)
    Exit_button = tk.Button(window, text="EXIT", width=10, font=("Roboto", 15, "bold"),
                            command=lambda: [window.destroy(), main_window.destroy()], bg="orange", bd=5)
    Home_button.place(x=10, y=450)
    Exit_button.place(x=660, y=450)
    Listbox.place(x=50, y=110)
    scrollbar.place(x=730, y=110, height=304)

    data = obj_bal.history_DB()
    if data is None:
        messagebox.showerror(message="No History....Play the Game Now.")
    else:
        for counter in data:
            Listbox.insert(tk.END, f"Player Name:{counter[0]}, Age:{counter[1]}, Random Number:{counter[2]}, Result:{counter[3]}")
    window.mainloop()


def game_exit():
    if messagebox.askyesno(message="Do you want to exit from the game?"):
        main_window.quit()


def main_page():
    global main_window
    main_window = tk.Tk()
    main_window.title("Number Guessing Game")
    image = Image.open("istockphoto-1429079387-612x612.jpg")
    image = image.resize((800, 500), )
    bg_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(main_window, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.image = bg_image
    lbl_game_name = tk.Label(main_window, text="Number Guessing Game", font=("Roboto", 22, "bold"), fg="white",
                             bg="midnight blue", bd=5, relief="solid", pady=5, padx=5)
    lbl_game_name.place(x=240, y=30)
    button1 = tk.Button(main_window, text="PLAY", width=25, font=("Roboto", 18, "bold"), command=lambda: [hide_current_window(main_window), play()], bg="aquamarine", bd=5)
    button2 = tk.Button(main_window, text="HISTORY", width=25, font=("Roboto", 18, "bold"), command=lambda: [hide_current_window(main_window),game_history()],
                        bg="aquamarine", bd=5)
    button3 = tk.Button(main_window, text="EXIT", width=25, font=("Roboto", 18, "bold"), command=game_exit, bg="aquamarine",
                        bd=5)
    button1.place(x=220, y=150)
    button2.place(x=220, y=230)
    button3.place(x=220, y=310)
    main_window.mainloop()


if __name__ == "__main__":
    main_page()
