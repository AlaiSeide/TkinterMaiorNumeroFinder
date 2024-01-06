import tkinter as tk

def encontrar_maior():

    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        num3 = int(entry3.get())

        maior = num1

        if num2 > maior:
            maior = num2

        if num3 > maior:
            maior = num3

        resultado.config(text=f"O maior número é: {maior}")

    except ValueError:
        resultado.config(text="Digite todos os valores corretamente.")

janela = tk.Tk()

janela.title('Maiornumberfinder')
janela.geometry('350x200')
janela.resizable(False, False)

label1 = tk.Label(janela, text="Digite o primeiro número:")
label1.pack()

entry1 = tk.Entry(janela)
entry1.pack()

label2 = tk.Label(janela, text="Digite o segundo número:")
label2.pack()

entry2 = tk.Entry(janela)
entry2.pack()

label3 = tk.Label(janela, text="Digite o terceiro número:")
label3.pack()

entry3 = tk.Entry(janela)
entry3.pack()

botao = tk.Button(janela, text="Encontrar Maior", command=encontrar_maior)
botao.pack()

resultado = tk.Label(janela, text=" ")
resultado.pack()

janela.mainloop()
