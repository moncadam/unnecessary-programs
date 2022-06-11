import tkinter as tk
from PIL import Image, ImageTk
from random import randint

win = tk.Tk()
win.title("Piedra, Papel o Tijera")
win.geometry("700x400")

stone_img = Image.open("stone.png")
stone_img = stone_img.resize((200,200), Image.Resampling.LANCZOS)
stone_img = ImageTk.PhotoImage(stone_img)

scissors_img = Image.open("scissors.png")
scissors_img = scissors_img.resize((200,200), Image.Resampling.LANCZOS)
scissors_img = ImageTk.PhotoImage(scissors_img)

paper_img = Image.open("paper.webp")
paper_img = paper_img.resize((200,200), Image.Resampling.LANCZOS)
paper_img = ImageTk.PhotoImage(paper_img)

count = [0,0]
top = tk.Label(text="Seleccione su objeto")
stone = tk.Button(text="", image=stone_img, command=lambda: CpuXUser(1))
scissors = tk.Button(text="", image=scissors_img, command=lambda: CpuXUser(3))
paper = tk.Button(text="", image=paper_img, command=lambda: CpuXUser(2))
result = tk.Label(text="Aqui se muestra el resultado")
counter = tk.Label(text="0 vs 0")

elements = {1: "Piedra", 2: "Papel", 3: "Tijera"}

def CpuXUser(inp):
    info = []
    cpuinp = randint(1,3)

    if inp == 1 and cpuinp == 3 or inp == 2 and cpuinp == 1 or inp == 3 and cpuinp == 2:
        info.append(["El jugador ganó.",elements[inp], elements[cpuinp], 1])
    elif inp == cpuinp:
        info.append(["Fue un empate.",elements[inp], elements[cpuinp], 2])
    else:
        info.append(["El jugador perdío.", elements[inp], elements[cpuinp], 0])

    result["text"] = info[0][0]
    top["text"] = f"El jugador lanzó {info[0][1]} y la maquina lanzó {info[0][2]}"
    if info[0][3] == 1:
        count[0] += 1
        counter["text"] = f"{count[0]} vs {count[1]}"
    elif info[0][3] == 0:
        count[1] += 1
        counter["text"] = f"{count[0]} vs {count[1]}" 

top.pack()
stone.place(relx=0.05, rely=0.5, anchor="w")
scissors.place(relx=0.95, rely=0.5,anchor="e")
paper.place(relx=0.5, rely=0.5,anchor='center')
result.pack()
result.config(font = ('Verdana', 24))
counter.pack(side=tk.BOTTOM, pady=12)
counter.config(font = ('Verdana', 16))

win.mainloop()