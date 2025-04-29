from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, image, Paragraph, Spacer
import webbrowser


root = Tk()

class Relatorios():
    def printCliente(self):
        webbrowser.open('clientee.pdf')
    def geraRelatCliente(self):
        self.c = canvas.canvas('cliente.pdf')

        self.codigoReal = self.codigo_entry.get()
        self.nomeReal = self.nome_entry.get()
        self.telefoneReal = self.fone_entry.get()
        self.cidadeReal = self.cidade_entry.get()
        self.c.setFont('Helvetica', 24)
        self.c.drawString(100, 750, 'Relatório de Clientes')


class Funcs:
    def limpa_tela(self):
        self.codigo_entry.delete(0, 'end')
        self.nome_entry.delete(0, 'end')
        self.fone_entry.delete(0, 'end')
        self.cidade_entry.delete(0, 'end')

    def conecta_bd(self):
        self.con = sqlite3.connect('clientes.db')
        self.cursor = self.con.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
                                codigo INTEGER PRIMARY KEY AUTOINCREMENT,
                                nome TEXT NOT NULL,
                                telefone TEXT,
                                cidade TEXT)''')
        self.con.commit()

    def desconecta_bd(self):
        self.con.close()

    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.telefone = self.fone_entry.get()
        self.cidade = self.cidade_entry.get()

    def add_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute('''INSERT INTO clientes (nome, telefone, cidade) VALUES (?, ?, ?)''',
                            (self.nome, self.telefone, self.cidade))
        self.con.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()

    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute('''SELECT codigo, nome, telefone, cidade FROM clientes ORDER BY nome ASC;''')
        for i in lista:
            self.listaCli.insert('', 'end', values=i)
        self.desconecta_bd()

    def OnDoubleClick(self, event):
        self.limpa_tela()
        for n in self.listaCli.selection():
            col1, col2, col3, col4 = self.listaCli.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.fone_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4)

    def deleta_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute('''DELETE FROM clientes WHERE codigo = ?''', (self.codigo,))
        self.con.commit()
        self.desconecta_bd()
        self.limpa_tela()
        self.select_lista()

    def altera_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute('''UPDATE clientes SET nome = ?, telefone = ?, cidade = ? WHERE codigo = ?''',
                            (self.nome, self.telefone, self.cidade, self.codigo))
        self.con.commit()
        self.desconecta_bd()
        self.select_lista()

class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.conecta_bd()
        self.desconecta_bd()
        self.select_lista()
        self.menus()
        root.mainloop()

    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.geometry("800x600")
        self.root.configure(background='#1e3743')
        self.root.resizable(width=True, height=True)
        self.root.maxsize(width=800, height=800)
        self.root.minsize(width=500, height=400)

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bg='#dfe3ee', bd=4, highlightbackground='#759fe6', highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(self.root, bg='#dfe3ee', bd=4, highlightbackground='#759fe6', highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgets_frame1(self):
        self.bt_limpar = Button(self.frame_1, text='Limpar', bd=2, bg='#107db2', fg='white',
                                font=('verdana', 8, 'bold'), command=self.limpa_tela)
        self.bt_limpar.place(relx=0.21, rely=0.1, relwidth=0.1, relheight=0.15)

        self.bt_buscar = Button(self.frame_1, text='Buscar', bd=2, bg='#107db2', fg='white',
                                font=('verdana', 8, 'bold'), command=lambda: print("Buscar"))
        self.bt_buscar.place(relx=0.32, rely=0.1, relwidth=0.1, relheight=0.15)

        self.bt_novo = Button(self.frame_1, text='Novo', bd=2, bg='#107db2', fg='white',
                              font=('verdana', 8, 'bold'), command=self.add_cliente)
        self.bt_novo.place(relx=0.61, rely=0.1, relwidth=0.1, relheight=0.15)

        self.bt_alterar = Button(self.frame_1, text='Alterar', bd=2, bg='#107db2', fg='white',
                                 font=('verdana', 8, 'bold'), command=self.altera_cliente)
        self.bt_alterar.place(relx=0.72, rely=0.1, relwidth=0.1, relheight=0.15)

        self.bt_apagar = Button(self.frame_1, text='Apagar', bd=2, bg='#107db2', fg='white',
                                font=('verdana', 8, 'bold'), command=self.deleta_cliente)
        self.bt_apagar.place(relx=0.83, rely=0.1, relwidth=0.1, relheight=0.15)

        self.lb_codigo = Label(self.frame_1, text='Código', bg='#dfe3ee', fg='#107db2')
        self.lb_codigo.place(relx=0.05, rely=0.05)
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        self.lb_nome = Label(self.frame_1, text='Nome', bg='#dfe3ee', fg='#107db2')
        self.lb_nome.place(relx=0.05, rely=0.35)
        self.nome_entry = Entry(self.frame_1, bg='#dfe3ee', fg='#555555', font=('verdana', 10, 'bold'))
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.85)

        self.lb_fone = Label(self.frame_1, text='Telefone', bg='#dfe3ee', fg='#107db2')
        self.lb_fone.place(relx=0.05, rely=0.6)
        self.fone_entry = Entry(self.frame_1, bg='#dfe3ee', fg='#555555', font=('verdana', 10, 'bold'))
        self.fone_entry.place(relx=0.05, rely=0.7, relwidth=0.4)

        self.lb_cidade = Label(self.frame_1, text='Cidade', bg='#dfe3ee', fg='#107db2')
        self.lb_cidade.place(relx=0.5, rely=0.6)
        self.cidade_entry = Entry(self.frame_1, bg='#dfe3ee', fg='#555555', font=('verdana', 10, 'bold'))
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.4)

    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height=3, columns=('col1', 'col2', 'col3', 'col4'))
        self.listaCli.heading('#0', text='')
        self.listaCli.heading('#1', text='Código')
        self.listaCli.heading('#2', text='Nome')
        self.listaCli.heading('#3', text='Telefone')
        self.listaCli.heading('#4', text='Cidade')

        self.listaCli.column('#0', width=1)
        self.listaCli.column('#1', width=50)
        self.listaCli.column('#2', width=200)
        self.listaCli.column('#3', width=125)
        self.listaCli.column('#4', width=125)

        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroolista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscroll=self.scroolista.set)
        self.scroolista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        self.scroolista.config(command=self.listaCli.yview)

        self.listaCli.bind('<Double-1>', self.OnDoubleClick)

    def menus(self):
        self.menu_bar = Menu(self.root)
        self.root.config(menu=self.menu_bar)

        self.options_menu = Menu(self.menu_bar, tearoff=0)       
        self.menu_bar.add_cascade(label='Opções', menu=self.options_menu)
        self.options_menu.add_command(label='Sair', command=self.root.quit)
        self.options_menu.add_command(label='Limpa Cliente', command=self.limpa_tela)
        self.menu_bar.add_cascade(label='Sobre', menu=self.select_lista)
Application()
