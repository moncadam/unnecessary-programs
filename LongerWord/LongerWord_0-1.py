import re
import tkinter

window = tkinter.Tk()
window.geometry("250x130")
window.title("Longer Word")

top = tkinter.Label(window, text="Este programa halla la palabra mas larga\n de una frase que ingrese el usuario")
word = tkinter.Entry(window)
longer_word = tkinter.Label(window, text="Aqui se muestra la palabras mas larga\n sin contar simbolos especiales...")

def LongerWord():
    input= word.get()
    longer_phrase = re.sub(r"[^a-zA-Z ]","",input)
    longer_list = longer_phrase.split()
    longer = max(longer_list, key=len)
    longer_word["text"]=longer

button = tkinter.Button(window, text="Hallar", command=LongerWord)

top.pack()
word.pack()
button.pack()
longer_word.pack()

window.mainloop()