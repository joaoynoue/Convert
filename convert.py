import tkinter as tk
from tkinter import filedialog, messagebox
import os
import fitz

pdf = None

# Janela Principal 
janela_principal = tk.Tk()
janela_principal.title("Conversor")
janela_principal.geometry("500x500")
janela_principal.resizable(False, False)
janela_principal.grid_rowconfigure(0, weight=1)
janela_principal.grid_columnconfigure(0, weight=1)
status_label = tk.Label(janela_principal,text='Nenhum arquivo selecionado')
status_label.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10)

#Função Selecionar  
def selecionar_pdf():
    global pdf
    pdf = filedialog.askopenfilename(
        parent=janela_principal,
        title="Selecionar Um Arquivo PDF",
        filetypes=[("Arquivos PDF", "*.pdf")]
    )
    
    if pdf:
        status_label.config(text="Arquivo selecionado!")
    else:
        status_label.config(text="Nenhum arquivo selecionado")
        

#Função converter

def converter():

    if not pdf:
        messagebox.showwarning("Aviso", "Selecione um arquivo para poder converter")
        return
    
    arquivo_salvo = filedialog.askdirectory(
        parent=janela_principal, title="Selecione uma paste para salvar a conversão"

    )

    if not arquivo_salvo:
        messagebox.showwarning("Aviso", "Selecione uma pasta para salvar os arquivos")
        return 
    
    try:
        doc = fitz.open(pdf)  
        total_paginas = doc.page_count

        for i, pagina in enumerate(doc, start=1):
            pix = pagina.get_pixmap(dpi=300)  
            nome_arquivo = os.path.join(arquivo_salvo, f"pagina_{i}.png")
            pix.save(nome_arquivo)

        
        messagebox.showinfo("Sucesso", f"{total_paginas} página(s) convertida(s) para PNG com sucesso!")
        doc.close()
    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao converter: {e}")
        
        
        
        
        
    




#Botão Selecionar o PDF 

botao_arquivo = tk.Button(janela_principal, text="Selecionar PDF", command=selecionar_pdf)
botao_arquivo.grid(row=0, column=0, sticky="ew", padx=10, pady=20)


#Botão da Conversão

botao_converter = tk.Button(janela_principal, text="Converter",command=converter )
botao_converter.grid(row=0, column=1, sticky="ew", padx=10, pady=20)


janela_principal.mainloop()