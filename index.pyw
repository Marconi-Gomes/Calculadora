import tkinter as tk

def calcular(op):
    global operador
    try:
        if op == '=':
            num1 = float(entry.get())
            num2 = float(entry2.get())
            resultado_calculo = eval(f"{num1} {operador} {num2}")
            entry.delete(0, tk.END)  # Limpa a entrada principal
            entry.insert(0, int(resultado_calculo))  # Exibe o resultado como inteiro
            entry2.delete(0, tk.END)  # Limpa a entrada 2
        else:
            if entry2.get():  # Se já houver um número na entrada 2
                if operador:
                    num1 = float(entry.get())
                    num2 = float(entry2.get())
                    resultado_calculo = eval(f"{num1} {operador} {num2}")
                    entry.delete(0, tk.END)  # Limpa a entrada principal
                    entry.insert(0, int(resultado_calculo))  # Exibe o resultado como inteiro
                    entry2.delete(0, tk.END)  # Limpa a entrada 2

            operador = op  # Define o operador
            entry2.insert(0, entry.get())  # Passa o número atual para a entrada 2
            entry.delete(0, tk.END)  # Limpa a entrada principal

    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Erro")  # Exibe erro na entrada

def apagar():
    entry.delete(0, tk.END)
    entry2.delete(0, tk.END)

def pressionar_enter(event):
    calcular('=')

def pressionar_tecla(event):
    if event.char in '+-*/':
        calcular(event.char)
    elif event.char == '=' or event.keysym == 'Return':
        calcular('=')

# Criando a janela principal
root = tk.Tk()
root.title("Calculadora Simples")
root.configure(bg="black")

# Ajustando o tamanho da janela
root.geometry("400x500")  # Ajustando a altura da janela

# Variável para armazenar o resultado
operador = ""

# Entrada para os números
entry = tk.Entry(root, bg="white", font=("Arial", 24), justify='center', width=15)
entry2 = tk.Entry(root, bg="white", font=("Arial", 24), justify='center', width=15)

# Criando botões com estilo neon laranja
def neon_button(text, command):
    return tk.Button(root, text=text, command=command, bg="light blue", fg="black", font=("Arial", 16), padx=5, pady=5)  # Tamanho da fonte e padding ajustados

# Botões de operação
btn_adicionar = neon_button("+", lambda: calcular('+'))
btn_subtrair = neon_button("-", lambda: calcular('-'))
btn_multiplicar = neon_button("*", lambda: calcular('*'))
btn_dividir = neon_button("/", lambda: calcular('/'))
btn_igual = neon_button("=", lambda: calcular('='))
btn_apagar = neon_button("C", apagar)

# Layout das entradas
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Layout dos botões numéricos
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 0)
]

for (text, row, col) in buttons:
    btn_num = neon_button(text, lambda t=text: entry.insert(tk.END, t))
    btn_num.grid(row=row, column=col, sticky="nsew")

# Adicionando os botões de operação
btn_apagar.grid(row=4, column=1, sticky="nsew")
btn_adicionar.grid(row=5, column=0, sticky="nsew")
btn_subtrair.grid(row=5, column=1, sticky="nsew")
btn_multiplicar.grid(row=5, column=2, sticky="nsew")
btn_dividir.grid(row=6, column=0, sticky="nsew")
btn_igual.grid(row=6, column=1, sticky="nsew")

# Ajustando o peso das linhas e colunas
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for j in range(3):
    root.grid_columnconfigure(j, weight=1)

# Vinculando os eventos de tecla pressionada
root.bind('<Return>', pressionar_enter)
root.bind('<Key>', pressionar_tecla)

# Iniciando a aplicação
root.mainloop()
