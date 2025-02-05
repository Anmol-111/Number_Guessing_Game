import tkinter as tk
from PIL import Image, ImageTk


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

    window.mainloop()

if __name__ == "__main__":
    main_page()