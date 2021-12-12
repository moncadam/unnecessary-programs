import re
import tkinter
from unicodedata import normalize

window = tkinter.Tk()
window.geometry("300x150")
window.title("Is Palindrome?")

top = tkinter.Label(window, text="Comprobar si frase es palindromo\n(Sin contar acentos, mayusculas, espacios ni numeros)")
phrase = tkinter.Entry(window)
result = tkinter.Label(window, text="Aqui se muestra si es Palindromo o no...")

def IsPalindrome():
    str = phrase.get()
    str = re.sub(
        r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
        normalize( "NFD", str), 0, re.I
    )
    str = normalize( 'NFC', str)
    formatted_str = re.sub(r"[^a-zA-ZñÑ]","",str).lower()

    if formatted_str[::-1] == formatted_str:
        result["text"] = formatted_str + " - Es Palindromo"
    else:
        result["text"] = formatted_str + " - No es Palindromo"


exe = tkinter.Button(window, text="Comprobar", command=IsPalindrome)

top.pack()
phrase.pack()
exe.pack()
result.pack()

window.mainloop()