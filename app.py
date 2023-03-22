from tkinter import *

root = Tk() #modulo que iniciará la ventana
root.title("Calculator")

display = Entry(root) # display = input
display.grid(row=1, columnspan=6, sticky= W+E) # (fila - columna - orientacion)

# NUMERIC BUTTONS
Button(root, text="1").grid(row=2, column="0") # clase(montado en root - que dirá)donde estará ubicado
Button(root, text="2").grid(row=2, column="1")
Button(root, text="3").grid(row=2, column="2")

Button(root, text="4").grid(row=3, column="0 ")
Button(root, text="5").grid(row=3, column="1")
Button(root, text="6").grid(row=3, column="2")

Button(root, text="7").grid(row=4, column="0")
Button(root, text="8").grid(row=4, column="1")
Button(root, text="9").grid(row=4, column="2")


root.mainloop()