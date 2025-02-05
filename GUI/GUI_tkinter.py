import tkinter as tk
from PIL import Image, ImageTk

def play():
    window = tk.Toplevel()
    window.title("Number Guessing Game")
    image = Image.open("C:\\Users\\Anmol\\Desktop\\istockphoto-1227598160-612x612.jpg")
    image = image.resize((800, 500), )
    bg_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(window, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.image = bg_image
    lbl_game_name = tk.Label(window, text="Number Guessing Game", font=("Roboto", 22, "bold"), fg="white",
                             bg="midnight blue", bd=5)
    lbl_game_name.place(x=240, y=30)
    window.mainloop()
'''
def game_history():
    window = tk.Toplevel()
    window.title("Number Guessing Game")
    image = Image.open("C:\\Users\\Anmol\\Desktop\\istockphoto-1227598160-612x612.jpg")
    image = image.resize((800, 500), )
    bg_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(window, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.image = bg_image
    lbl_game_name = tk.Label(window, text="Number Guessing Game", font=("Roboto", 22, "bold"), fg="white",
                             bg="midnight blue", bd=5)
    lbl_game_name.place(x=240, y=30)
    window.mainloop()

def game_exit():
    window = tk.Toplevel()
    window.title("Number Guessing Game")
    image = Image.open("C:\\Users\\Anmol\\Desktop\\istockphoto-1227598160-612x612.jpg")
    image = image.resize((800, 500), )
    bg_image = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(window, width=image.width, height=image.height)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    canvas.image = bg_image
    lbl_game_name = tk.Label(window, text="Number Guessing Game", font=("Roboto", 22, "bold"), fg="white",
                             bg="midnight blue", bd=5)
    lbl_game_name.place(x=240, y=30)
    window.mainloop()
'''
def main_page():
    global window
    window = tk.Tk()
    window.title("Number Guessing Game")
    image = Image.open("C:\\Users\\Anmol\\Desktop\\istockphoto-1227598160-612x612.jpg")
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