import tkinter as tk
import random
import pygame
from PIL import Image
from itertools import count



def animation(count):
    global anim
    im2 = im[count]

    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    anim = window.after(100, lambda :animation(count))



def play_music():
    pygame.mixer.music.load("Fallout_4_Main_Theme.mp3") 
    pygame.mixer.music.play()



def generator():
    input = int(key_input.get())

    if input == '' or input > 999 or input < 100:
        tk.messagebox.showwarning('Error 449', 'The key cannot be generated!')

    else:
        elements = [0, 0, 0, 0, 0]
        key = ""
        element_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

        # element_1
        for i in range(5):
            elements[i] += random.randint(0, 34)
            key += element_list[elements[i]] 
        key += "-"

        # element_2
        for i in range(4):
            elements[i] += (input // 100)
            if elements[i] > 35:
                elements[i] -= 10
            elif elements[i] >= 26 and (elements[i] - (input // 100)) <= 25:
                elements[i] -= 25
            key += element_list[elements[i]] 
        key += "-"

        # element_3
        for i in range(3):
            elements[i] -= ((input // 10) % 10)
            if elements[i] < 26 and (elements[i] + ((input // 10) % 10)) > 25:
                elements[i] += 10
            elif elements[i] < 0:
                elements[i] += 25
            key += element_list[elements[i]] 
        key += "-"
        

        # element_4
        for i in range(2):
            elements[i] += (input % 10)
            if elements[i] >= 35:
                elements[i] -= 10
            elif elements[i] >= 26 and (elements[i] - (input % 100)) <= 25:
                elements[i] -= 25
            key += element_list[elements[i]] 
        key_output.delete("0", tk.END)
        key_output.insert(0, key)

    

if __name__ == "__main__":
    # Create window
    window = tk.Tk()
    window.title('Key generator for Fallout 5')
    window.geometry('1200x675')
    pygame.init()

    # Add image to background
    bg_img = tk.PhotoImage(file='fallout.png')
    lbl_bg = tk.Label(window, image=bg_img)
    lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)
    play_music()

    # Add Gif animation
    info = Image.open("VaultBoy_Fallout.gif")
    frames = info.n_frames  
    im = [tk.PhotoImage(file="VaultBoy_Fallout.gif",format=f"gif -index {i}") for i in range(frames)]
    count = 0
    anim = None
    gif_label = tk.Label(window, image="")
    gif_label.place(relx=0.66, rely=0.385)
    animation(count)

    # Input
    input_label = tk.Label(window, text='Enter secret sequence (3 digits): ', font=14)
    input_label.place(relx=0.195, rely=0.23)
    key_input = tk.Entry(window, width=3, font=16)
    key_input.insert(0, '000')
    key_input.place(relx=0.45, rely=0.23)
    
    # Button for generate
    btn_guess = tk.Button(window, text='Generate KEY', font=14, width=12, command=generator)
    btn_guess.place(relx=0.195, rely=0.3)
    
    # Output
    output_label = tk.Label(window, text='Game key: ', font=14)
    output_label.place(relx=0.195, rely=0.385)
    key_output = tk.Entry(window, width=30, font=16)
    key_output.place(relx=0.29, rely=0.385)

    window.mainloop()

# I do not approve of Internet piracy, and therefore I leave an Easter egg with bad_karma for you as a reminder