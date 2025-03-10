import tkinter as tk

def hide_label():
    label.pack_forget()  # Remove o widget da janela

def show_label():
    label.pack()  # Adiciona o widget novamente na janela

# Configuração da janela principal
root = tk.Tk()
root.geometry("300x200")

# Criação de um label
label = tk.Label(root, text="Texto que pode ser removido")
label.pack(pady=10)

# Botão para remover o label
button_hide = tk.Button(root, text="Esconder Texto", command=hide_label)
button_hide.pack(pady=5)

# Botão para mostrar o label novamente
button_show = tk.Button(root, text="Mostrar Texto", command=show_label)
button_show.pack(pady=5)

root.mainloop()
