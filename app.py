from tkinter import *

root = Tk() #modulo que iniciará la ventana
root.title("Calculator")

display = Entry(root) # display = input
display.grid(row=1, columnspan=6, sticky= W+E) # (fila - columna - orientacion para que el botón abarquen más)

# NUMERIC 1 - 9 BUTTONS
Button(root, text="1").grid(row=2, column="0", sticky= W+E) # clase(montado en root - que dirá)donde estará ubicado
Button(root, text="2").grid(row=2, column="1", sticky= W+E)
Button(root, text="3").grid(row=2, column="2", sticky= W+E)

Button(root, text="4").grid(row=3, column="0", sticky= W+E)
Button(root, text="5").grid(row=3, column="1", sticky= W+E)
Button(root, text="6").grid(row=3, column="2", sticky= W+E)

Button(root, text="7").grid(row=4, column="0", sticky= W+E)
Button(root, text="8").grid(row=4, column="1", sticky= W+E)
Button(root, text="9").grid(row=4, column="2", sticky= W+E)

# SECONDARY BUTTONS
Button(root, text="AC").grid(row=5, column="0", sticky= W+E)
Button(root, text="0").grid(row=5, column="1", sticky= W+E)
Button(root, text="%").grid(row=5, column="2", sticky= W+E)

# ARITHMETIC OPERATIONS
Button(root, text="+").grid(row=2, column="3", sticky= W+E)
Button(root, text="-").grid(row=3, column="3", sticky= W+E)
Button(root, text="*").grid(row=4, column="3", sticky= W+E)
Button(root, text="/").grid(row=5, column="3", sticky= W+E)

# + SECONDARY BUTTONS
Button(root, text="<-").grid(row=2, column="4", sticky= W+E, columnspan=2)
Button(root, text="exp").grid(row=3, column="4", sticky= W+E)
Button(root, text="^2").grid(row=3, column="5", sticky= W+E)
Button(root, text="(").grid(row=4, column="4", sticky= W+E)
Button(root, text=")").grid(row=4, column="5", sticky= W+E)
Button(root, text="=").grid(row=5, column="4", sticky= W+E, columnspan=2)

root.mainloop()