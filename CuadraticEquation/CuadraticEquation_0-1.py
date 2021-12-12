import tkinter
import cmath

window = tkinter.Tk()
window.geometry("225x175")
window.title("Cuadratic Equation")

top = tkinter.Label(window, text="Ecuacion Cuadratica General\nax**2+bx+c=0")

input_a=tkinter.Entry(window)
input_b=tkinter.Entry(window)
input_c=tkinter.Entry(window)

top.pack()
input_a.pack()
input_b.pack()
input_c.pack()

ResultPositive = tkinter.Label(window,text="Aqui se muestra el resultado positivo...")
ResultNegative = tkinter.Label(window,text="Aqui se muestra el resultado negativo...")

def Result():
    a = float(input_a.get())
    b = float(input_b.get())
    c = float(input_c.get())

    rmas = (-b + cmath.sqrt(b**2-(4*a*c)))/(2*a)
    rmenos = (-b - cmath.sqrt(b**2-(4*a*c)))/(2*a)

    ResultPositive["text"]=str(rmas)
    ResultNegative["text"]=str(rmenos)

result = tkinter.Button(window, text="Resolver", command=Result)
result.pack()

ResultPositive.pack()
ResultNegative.pack()

window.mainloop()