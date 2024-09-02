from pathlib import Path
from tkinter import*
from tkinter.messagebox import *
import os


import sys
  

alunos = []
professores = ["02988123390","068687"]
pastaApp=os.path.dirname(__file__)



##############################################################################

# Cadastro dos Professor
def cadastro():
    def voltar():
        cadastro.destroy()
        inicializa()
    def cadastro_professor():
        
        nome_professor = (nome.get())
        cpf_professor = (cpf.get())
        email_professor = (email.get())
        telefone_professor = (telefone.get())        
        instituicao_professor = (instituicao.get())
        senha_professor = (senha.get())

        novo_professor = (nome_professor, cpf_professor, email_professor, telefone_professor,
                                 instituicao_professor, senha_professor)
        
        professores.append(novo_professor)
        if nome_professor == "" and senha_professor == "" and cpf_professor == "" and telefone_professor == "":
            showinfo("ERRO", " PRENCHA OS CAMPOS! ")
            
            
        else:
            cadastro.destroy()
            inicializa()
        
    pastaApp=os.path.dirname(__file__)   
    cadastro = Tk()
    cadastro.title("TELA DE CADASTRO")
    cadastro.geometry('600x630')
    cadastro.maxsize(600,630)
    cadastro.minsize(600,630)
    cadastro.config(background='#c0c0c0')
    cadastro.iconbitmap('imagens/icon.ico')
    ima_salvar = PhotoImage(file = pastaApp+'\\Nova pasta1/salvar.png')
    ima_voltar = PhotoImage(file = pastaApp+'\\Nova pasta1/voltar.png')


    ima3 = PhotoImage(file=pastaApp+'\\Nova pasta1/cadastro.png')
    foto = Label(cadastro,image=ima3,width="600",height="630")
    foto.place(x=0,y=0)
    #cadastro.attributes("-alpha",1)
    
    
    nome = Entry(cadastro,width="28",border=0,font=('bold 18 '))
    nome.place(x=135,y=175)
    nome.focus()  
     

    cpf = Entry(cadastro,width="30",border=0,font=('bold 18 '))
    cpf.place(x=107,y=230)

    email = Entry(cadastro,width="30",border=0,font=('bold 18'))
    email.place(x=140,y=288)

    telefone = Entry(cadastro,width="30",border=0,font=('bold 18'))
    telefone.place(x=160,y=346)
    

    instituicao = Entry(cadastro,width="30",border=0,font=('bold 18'))
    instituicao.place(x=185,y=405)

    senha = Entry(cadastro,width="30",border=0,font=('bold 18'))
    senha.place(x=135,y=463)

    buton1 = Button(cadastro,width=80,border=1,height=80,image=ima_salvar,command=cadastro_professor)
    buton1.place(x=288,y=530)

    buton1 = Button(cadastro,text="voltar",width=70,height=20,image=ima_voltar,border=0,command=voltar)
    buton1.place(x=480,y=138)
    

    cadastro.mainloop()

##############################################################################

        

def menu():
    def cadastra_alunos():
        frame_cadastro_alunos = Frame(telaprincipal, bg="#c0c0c0", width=500, height=500)
        frame_cadastro_alunos.place(x=0, y=0)
        
        def voltar():
            frame_cadastro_alunos.destroy()
            
        def salvar_aluno():
            nome_aluno = nome.get()
            cpf_aluno = cpf.get()
            email_aluno = email.get()
            telefone_aluno = telefone.get()
            curso_aluno = curso.get()

            if not nome_aluno or not cpf_aluno or not email_aluno or not telefone_aluno or not curso_aluno:
                showinfo("ERRO", "PREENCHA TODOS OS CAMPOS!")
                return

            novo_aluno = (nome_aluno, cpf_aluno, email_aluno, telefone_aluno, curso_aluno)
            alunos.append(novo_aluno)
            showinfo("SUCESSO", "Cadastro de aluno realizado com sucesso!")
            frame_cadastro_alunos.destroy()

        Label(frame_cadastro_alunos, text="Cadastro de Alunos", font=('Arial', 18), bg="#c0c0c0").place(x=150, y=10)

        Label(frame_cadastro_alunos, text="Nome", font=('Arial', 12), bg="#c0c0c0").place(x=50, y=50)
        nome = Entry(frame_cadastro_alunos, width=30, font=('Arial', 12))
        nome.place(x=150, y=50)

        Label(frame_cadastro_alunos, text="CPF", font=('Arial', 12), bg="#c0c0c0").place(x=50, y=100)
        cpf = Entry(frame_cadastro_alunos, width=30, font=('Arial', 12))
        cpf.place(x=150, y=100)

        Label(frame_cadastro_alunos, text="Email", font=('Arial', 12), bg="#c0c0c0").place(x=50, y=150)
        email = Entry(frame_cadastro_alunos, width=30, font=('Arial', 12))
        email.place(x=150, y=150)

        Label(frame_cadastro_alunos, text="Telefone", font=('Arial', 12), bg="#c0c0c0").place(x=50, y=200)
        telefone = Entry(frame_cadastro_alunos, width=30, font=('Arial', 12))
        telefone.place(x=150, y=200)

        Label(frame_cadastro_alunos, text="Curso", font=('Arial', 12), bg="#c0c0c0").place(x=50, y=250)
        curso = Entry(frame_cadastro_alunos, width=30, font=('Arial', 12))
        curso.place(x=150, y=250)

        Button(frame_cadastro_alunos, text="Salvar", font=('Arial', 12), command=salvar_aluno).place(x=150, y=300)
        Button(frame_cadastro_alunos, text="Voltar", font=('Arial', 12), command=voltar).place(x=250, y=300)

    def imprimir_alunos():
        report_window = Toplevel(telaprincipal)
        report_window.title("Relatório de Alunos")
        report_window.geometry('600x400')
        report_window.config(background='#c0c0c0')

        Label(report_window, text="Relatório de Alunos", font=('Arial', 18), bg="#c0c0c0").pack(pady=10)

        text_area = Text(report_window, wrap=WORD, width=80, height=20)
        text_area.pack(pady=10)

        report_text = "Nome\tCPF\tEmail\tTelefone\tCurso\tNota\tTrabalho\tData do Trabalho\n"
        report_text += "-"*100 + "\n"

        
            
        for aluno in alunos:
            report_text += "|""\t".join(aluno) + "\n"

        text_area.insert(END, report_text)
        text_area.config(state=DISABLED)

        Button(report_window, text="Fechar", font=('Arial', 12), command=report_window.destroy).pack(pady=10)
    def sair():
        telaprincipal.destroy()
        inicializa()
    
    telaprincipal = Tk()
    telaprincipal.title("TELA PRINCIPAL")
    telaprincipal.geometry('500x500')
    telaprincipal.maxsize(900,500)
    telaprincipal.minsize(500,500)
    telaprincipal.config(background='#ffffdd')
    telaprincipal.iconbitmap('imagens/icon.ico')



    Label1 = Label(telaprincipal,text="SEJA BEM VINDO  ACPED",width=45,height=5,relief="flat",bg="#ffffff",font="areal 14")
    Label1.place(x=0,y=0)

    buton1 = Button(telaprincipal,text="CADASTRAR ALUNO",width=10,height=3,font="segoe 10",command=cadastra_alunos)
    buton1.place(x=10,y=120)

    buton1 = Button(telaprincipal,text="AGENDA",width=10,height=3,font="segoe 10")
    buton1.place(x=10,y=200)

    buton1 = Button(telaprincipal,text="DISCIPLINA",width=10,height=3,font="segoe 10")
    buton1.place(x=10,y=280)

    buton1 = Button(telaprincipal,text="IMPRIMIR RELATORIO DAS ALUNOS",border=1,width=10,height=3,font="segoe 10",command=imprimir_alunos)
    buton1.place(x=10,y=360)

    buton1 = Button(telaprincipal,text="",border=0,width=10,height=3,font="segoe 10")
    buton1.place(x=220,y=120)

    buton1 = Button(telaprincipal,text="",border=0,width=10,height=3,font="segoe 10")
    buton1.place(x=220,y=200)

    buton1 = Button(telaprincipal,text="",border=0,width=10,height=3,font="segoe 10")
    buton1.place(x=220,y=280)

    buton1 = Button(telaprincipal,text="",border=0,width=10,height=3,font="segoe 10")
    buton1.place(x=220,y=360)

    buton1 = Button(telaprincipal,text="voltar",border=0,width=10,height=3,font="segoe 10",command=sair)
    buton1.place(x=400,y=120)



    telaprincipal.mainloop()

##############################################################################
def inicializa():
    
    def acessar():
        cpf_digitado = (cpf_login.get())
        senha_digitado = (senha_login.get())
        for prof in professores:
            if prof[1] == cpf_digitado or "02988123390" == cpf_digitado and prof[5] == senha_digitado or "068687" == senha_digitado:
                tela_de_login.destroy()
                menu()
                return
            elif prof [0] == cpf_digitado and prof[1] == senha_digitado:
                tela_de_login.destroy()
                menu()
                return
        showinfo("ERRO", "USUARIO OU SENHA INVALIDO. ") 

    def cadastrar():
        tela_de_login.destroy()
        cadastro()

#usuario_login.pack(side = TOP ,expand=True)
    tela_de_login = Tk()
    ima1 = PhotoImage(file=pastaApp+"\\imagens/LOGIN.png")
    foto = Label(tela_de_login,image=ima1,width="600",height="600")
    foto.place(x=0,y=0)
    #tela_de_login.attributes("-alpha",0.9)
    tela_de_login.title("LOGIN")
    tela_de_login.geometry("550x400+500+200")
    tela_de_login.maxsize(550,400)
    tela_de_login.config(background='#00ff80')
    tela_de_login.iconbitmap('imagens/icon.ico')
    label = Label(text="LOGIN",background="#7b959a", foreground='#b28048',font=('arial 18'))
    label.place(x=160,y=10)

    cpf_login1 = Label(tela_de_login,text="CPF",width=10,height=1,relief="flat",bg="#045e61",font=('arial 14 bold underline'),foreground='white',)
    cpf_login1.place(x=140,y=70)

    cpf_login = Entry(tela_de_login,width=18,bg="#045e61",justify=CENTER,border=0,font=('arial 12 bold underline'))
    cpf_login.place(x=120,y=110)
    cpf_login.focus()

    senha_login1 = Label(tela_de_login,text="SENHA",width=10,height=1,padx=1,relief="flat",bg="#045e61",font=('arial 14 bold underline'),foreground='white',)
    senha_login1.place(x=140,y=160)
    senha_login = Entry(tela_de_login,show="*",bg="#045e61",justify=CENTER,width=18,border=0,font=('arial 12 bold underline'))
    senha_login.place(x=120,y=200)
    

    buton = Button(tela_de_login,text="CADASTRAR",width=10,height=1,padx=3,relief="solid",bg="#A9A9A9",font="segoe 10 bold", command=cadastrar)
    buton.place(x=50,y=280)
    buton1 = Button(tela_de_login,text="ACESSAR",width=10,height=1,padx=3,relief="solid",bg="#A9A9A9",font="segoe 10 bold",command=acessar)
    buton1.place(x=260,y=280)

   

    tela_de_login.mainloop()
inicializa()

