from tkinter import *

root = Tk() #modulo que iniciará la ventana
root.title("Calculator")

i = 0

display = Entry(root) # display = input
display.grid(row=1, columnspan=6, sticky= W+E) # (fila - columna - orientacion para que el botón abarquen más)

# FUNCIÓN OBTENER NÚMERO
# Guardamos el indice en una variable para que vaya incrementando
def get_numbers(n):
    global i
    display.insert(i,n)
    i+=1

# AGREGAR OPERADOR
def get_operation(operator):
    global i
    operator_length = len(operator) # longitud del operador
    display.insert(i, operator)
    i+=operator_length

# LIMPIAR PANTALLA 
def clear_display():
    display.delete(0, END)

# BORRAR UN SOLO ELEMENTO
def undo():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        clear_display()
        display.insert(0, display_new_state)
    else:
        clear_display()
        display.insert(0, 'ERROR')

# CALCULAR
def calculate():
    display_state = display.get()
    try:
        math_expression =  compile(display_state, 'app.py', 'eval')
        result = eval(math_expression)
        clear_display()
        display.insert(0,result)
    except:
        clear_display()
        display.insert(0,"error")


# NUMERIC 1 - 9 BUTTONS
Button(root, text="1", command=lambda:get_numbers(1)).grid(row=2, column="0", sticky= W+E) # clase(montado en root - que dirá)donde estará ubicado
Button(root, text="2", command=lambda:get_numbers(2)).grid(row=2, column="1", sticky= W+E) 
Button(root, text="3", command=lambda:get_numbers(3)).grid(row=2, column="2", sticky= W+E)

Button(root, text="4", command=lambda:get_numbers(4)).grid(row=3, column="0", sticky= W+E)
Button(root, text="5", command=lambda:get_numbers(5)).grid(row=3, column="1", sticky= W+E)
Button(root, text="6", command=lambda:get_numbers(6)).grid(row=3, column="2", sticky= W+E)

Button(root, text="7", command=lambda:get_numbers(7)).grid(row=4, column="0", sticky= W+E)
Button(root, text="8", command=lambda:get_numbers(8)).grid(row=4, column="1", sticky= W+E)
Button(root, text="9", command=lambda:get_numbers(9)).grid(row=4, column="2", sticky= W+E)

# SECONDARY BUTTONS
Button(root, text="AC", command=lambda:clear_display()).grid(row=5, column="0", sticky= W+E)
Button(root, text="0", command=lambda: get_numbers(0)).grid(row=5, column="1", sticky= W+E)
Button(root, text="%", command=lambda:get_operation("%")).grid(row=5, column="2", sticky= W+E)

# ARITHMETIC OPERATIONS
Button(root, text="+", command=lambda:get_operation("+")).grid(row=2, column="3", sticky= W+E)
Button(root, text="-", command=lambda:get_operation("-")).grid(row=3, column="3", sticky= W+E)
Button(root, text="*", command=lambda:get_operation("*")).grid(row=4, column="3", sticky= W+E)
Button(root, text="/", command=lambda:get_operation("/")).grid(row=5, column="3", sticky= W+E)

# + SECONDARY BUTTONS
Button(root, text="<-", command=lambda: undo()).grid(row=2, column="4", sticky= W+E, columnspan=2)
Button(root, text="exp", command=lambda:get_operation("**")).grid(row=3, column="4", sticky= W+E)
Button(root, text="^2", command=lambda:get_operation("**2")).grid(row=3, column="5", sticky= W+E)
Button(root, text="(", command=lambda:get_operation("(")).grid(row=4, column="4", sticky= W+E)
Button(root, text=")", command=lambda:get_operation(")")).grid(row=4, column="5", sticky= W+E)
Button(root, text="=", command=lambda:calculate()).grid(row=5, column="4", sticky= W+E, columnspan=2)

root.mainloop()