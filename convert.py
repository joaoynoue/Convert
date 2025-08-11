import tkinter as tk
from tkinter import filedialog


pdf = None

# Janela Principal 
janela_principal = tk.Tk()
janela_principal.title("Conversor")
janela_principal.geometry("500x500")
janela_principal.resizable(False, False)
janela_principal.grid_rowconfigure(0, weight=1)
janela_principal.grid_columnconfigure(0, weight=1)

#Função Selecionar  
def selecionar_pdf():
    global pdf
    pdf = filedialog.askopenfilename(
        title="Selecionar Um Arquivo PDF",
        filetypes=[("Arquivos PDF", "*.pdf")])
    
    if pdf is True:
        print("Arquivo Selecionado!")
    else:
        print("Nenhum arquivo selecionado")



#Botão Selecionar o PDF 

botao_arquivo = tk.Button(janela_principal, text="Selecionar PDF", command=selecionar_pdf)
botao_arquivo.grid(row=0, column=0, sticky="ew", padx=10, pady=20)


#Botão da Conversão

botao_converter = tk.Button(janela_principal, text="Converter",command="janela_confirmacao" )
botao_converter.grid(row=0, column=1, sticky="ew", padx=10, pady=20)


janela_principal.mainloop()