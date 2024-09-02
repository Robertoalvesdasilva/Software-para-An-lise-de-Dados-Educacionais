
from pathlib import Path
from tkinter import*
from tkinter.messagebox import *
import os
import time
import sys
from tkinter import ttk
alunos =[]


def cadastra_alunos():
    frame_cadastro_alunos = Frame(telaprincipal, bg="#c0c0c0", width=500, height=500)
    frame_cadastro_alunos.place(x=0, y=0)
    
    def voltar():
        frame_cadastro_alunos.destroy()
        
    def salvar_aluno():
        nome = nome_aluno.get()
        matricula = int(matricula_aluno.get())

        if not nome or not matricula:
            showinfo("ERRO", "PREENCHA TODOS OS CAMPOS!")
            return
        
        novo_aluno = {'nome': nome, 'matricula': matricula, 'notas': ['']*8, 'trabalhos': ['']*10}
        alunos.append(novo_aluno)
        
        # Adiciona o novo aluno à tabela
        lista.insert("", "end", values=(matricula, nome))
        
        showinfo("SUCESSO", "Cadastro de aluno realizado com sucesso!")
        frame_cadastro_alunos.destroy()

    Label(frame_cadastro_alunos, text="Cadastro de Alunos", font=('Arial', 18), bg="#c0c0c0").place(x=150, y=10)

    Label(frame_cadastro_alunos, text="Nome", font=('Arial', 12), bg="#c0c0c0").place(x=50, y=50)
    nome_aluno = Entry(frame_cadastro_alunos, width=30, font=('Arial', 12))
    nome_aluno.place(x=150, y=50)

    Label(frame_cadastro_alunos, text="Matricula", font=('Arial', 12), bg="#c0c0c0").place(x=50, y=100)
    matricula_aluno = Entry(frame_cadastro_alunos, width=30, font=('Arial', 12))
    matricula_aluno.place(x=150, y=100)
    
    Button(frame_cadastro_alunos, text="Salvar", font=('Arial', 12), command=salvar_aluno).place(x=150, y=300)

    Button(frame_cadastro_alunos, text="Voltar", font=('Arial', 12), command=voltar).place(x=250, y=300)

def relatorio_alunos():
    
    relatorio = Toplevel(telaprincipal)
    relatorio.title("Relatório de Alunos")
        
    relatorio.geometry('794x1123')  # Tamanho A4
    
    relatorio.config(background='#c0c0c0')
        
    Label(relatorio, text="Relatório de Alunos", font=('Arial', 18), bg="#c0c0c0").pack(pady=10) # titulo
    
    
    text_area = Text(relatorio, wrap=WORD, width=90, height=50, font=('Courier New', 12))  # Definindo a fonte e tamanho
    text_area.pack(pady=10)

    text_area.tag_configure("header", font=('Courier New', 12, 'bold'), background='#d3d3d3')  # Fonte e cor de fundo do cabeçalho
    
    
    # Cabeçalho do relatório
    report_text = f"{'Matrícula':<40} {'Nome':<40}\n"
    text_area.insert(END, report_text, "header")
      
    
    # Loop para inserir os dados de cada aluno
    for aluno in alunos:
        text_area.insert(END, f"{aluno['matricula']:<10} {aluno['nome']:<0}\n")
    
       
    
    # Desabilitar a edição da área de texto (apenas leitura)
    text_area.config(state=DISABLED)
    
    # Botão para fechar a janela do relatório
    Button(relatorio, text="Fechar", font=('Arial', 12), command=relatorio.destroy).pack(pady=10)
        
def abrir_edicao_aluno():
    selected_item = lista.selection()
    if not selected_item:
        showinfo("ERRO", "Selecione um aluno para editar.")
        return
    
    selected_item = selected_item[0]
    aluno_selecionado = lista.item(selected_item)['values']
    
    matricula = int(aluno_selecionado[0])
    aluno = next((aluno for aluno in alunos if aluno['matricula'] == matricula), None)
    
    if aluno:
        janela_edicao_aluno(aluno)
    else:       
        showinfo("ERRO", "Aluno não encontrado.")
def janela_edicao_aluno(aluno):
    edicao_window = Toplevel(telaprincipal)
    edicao_window.title(f"Editar Notas e Trabalhos - {aluno['nome']}")
    edicao_window.geometry('600x600')
    
    Label(edicao_window, text=f"Aluno: {aluno['nome']}", font=('Arial', 16)).pack(pady=10)
    
    # Notas
    notas_entries = []
    for i in range(8):
        Label(edicao_window, text=f"Nota {i+1}", font=('Arial', 12)).place(x=50, y=50 + i*30)
        nota_entry = Entry(edicao_window, width=10, font=('Arial', 12))
        nota_entry.place(x=150, y=50 + i*30)
        nota_entry.insert(0, aluno['notas'][i])
        notas_entries.append(nota_entry)
    
    # Trabalhos
    trabalhos_entries = []
    for i in range(10):
        Label(edicao_window, text=f"Trabalho {i+1}", font=('Arial', 12)).place(x=300, y=50 + i*30)
        trabalho_entry = Entry(edicao_window, width=10, font=('Arial', 12))
        trabalho_entry.place(x=400, y=50 + i*30)
        trabalho_entry.insert(0, aluno['trabalhos'][i])
        trabalhos_entries.append(trabalho_entry)
    
    def salvar_alteracoes():
        aluno['notas'] = [nota_entry.get() for nota_entry in notas_entries]
        aluno['trabalhos'] = [trabalho_entry.get() for trabalho_entry in trabalhos_entries]
        showinfo("SUCESSO", "Notas e Trabalhos atualizados com sucesso!")
        edicao_window.destroy()
    
    Button(edicao_window, text="Salvar", font=('Arial', 12), command=salvar_alteracoes).place(x=150, y=500)
    Button(edicao_window, text="Fechar", font=('Arial', 12), command=edicao_window.destroy).place(x=250, y=500)

telaprincipal = Tk()
telaprincipal.title("TELA PRINCIPAL")
telaprincipal.geometry('1500x770')
telaprincipal.maxsize(1500,770)
telaprincipal.minsize(1500,770)


painel1 = PanedWindow(bd=4,relief='groove',bg="#E0FFFF")
painel1.pack(fill=BOTH, expand=1)


titulo = Label(painel1,text="ACPED",width=1000,height=3,font=14,bg="#B0E0E6")
titulo.pack(side=TOP)

frame1 = Frame(painel1,width=170,height=1000,bg="#7FFFD4")
frame1.pack(expand=False,fill='both',side="left")

butao = Button(frame1,text="TURMA",padx=16,width=12,height=3,font="segoe 10",bg="#5F9EA0")
butao.pack(side=TOP,padx=20,pady=20)

buton1 = Button(frame1,text="CADASTRAR ALUNO",width=16,height=3,font="segoe 10",bg="#5F9EA0",command=cadastra_alunos)
buton1.pack(side=TOP,padx=20,pady=20)

buton1 = Button(frame1,text="RELATORIO",width=16,height=3,font="segoe 10",bg="#5F9EA0",command=relatorio_alunos)
buton1.pack(side=TOP,padx=20,pady=20)

Button(frame1, text="AVALIAÇÕES", width=16, height=3, font="segoe 10", bg="#5F9EA0", command=abrir_edicao_aluno).pack(side=TOP, padx=20, pady=20)


# Configurando a lista de alunos
style = ttk.Style()
style.configure("Treeview", font=('Arial', 12)) 
    
style.configure("Treeview.Heading", font=('Arial', 14))  
colunas = ("Matrícula", "Nome")

lista = ttk.Treeview(painel1, columns=colunas, show='headings')
lista.heading("Matrícula", text="Matrícula")
lista.heading("Nome", text="Nome")

lista.column("Matrícula", anchor=CENTER, width=150)
lista.column("Nome", anchor=W, width=1050)

lista.pack(fill=BOTH, expand=True)



telaprincipal.mainloop()