# -*- coding: utf-8 -*-
import Worker as wk
from tkinter import (Tk, Button, Frame, filedialog, Label)
import threading

class Mensagem:

    def __init__(self, master=None, mensagem='Erro'):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text=mensagem)
        self.msg["font"] = ("Calibri", "13", "italic")
        self.msg.pack ()

        self.sair = Button(self.widget1)
        self.sair["text"] = "OK"
        self.sair["font"] = ("Calibri", "13")
        self.sair["width"] = 10
        self.sair['command'] = self.widget1.quit
        self.sair.pack()

# TELA PRINCIPAL
class Menu:

    def __init__(self, master=None):
        self.master = master

        self.nomeArquivo = None

        # criando os conteiners
        self.conteinerFile = Frame(master)
        self.conteiner1 = Frame(master)
        self.conteiner2 = Frame(master)
        self.conteiner3 = Frame(master)
        self.conteiner4 = Frame(master)
        self.conteiner5 = Frame(master)
        self.conteiner0 = Frame(master)

        self.conteinerFile.pack()
        self.conteiner1.pack()
        self.conteiner2.pack()
        self.conteiner3.pack()
        self.conteiner4.pack()
        self.conteiner5.pack()
        self.conteiner0.pack()

        self.botaoFile = self.criaBotao(self.conteinerFile, 'Escolha um arquivo', self.getFile)
        self.botao1 = self.criaBotao(self.conteiner1, 'Validar nomes', self.release1)
        self.botao2 = self.criaBotao(self.conteiner2, 'Gerar lista de sinônimos', self.release2)
        self.botao3 = self.criaBotao(self.conteiner3, 'Gerar informações', self.release3)
        self.botao4 = self.criaBotao(self.conteiner4, 'Gerar coordenadas geográficas', self.release4)
        self.botao5 = self.criaBotao(self.conteiner5, 'Todas as operações.', self.todasReleases)
        self.botao0 = self.criaBotao(self.conteiner0, 'Sair', None)
        self.botao0['command'] = self.conteiner0.quit

        # distanciando verticalmente
        self.botaoFile.grid(row=0, column=0, pady=(3, 10))
        self.botao1.grid(row=1, column=0, pady=(3, 10))
        self.botao2.grid(row=2, column=0, pady=(3, 10))
        self.botao3.grid(row=3, column=0, pady=(3, 10))
        self.botao4.grid(row=4, column=0, pady=(3, 10))
        self.botao5.grid(row=5, column=0, pady=(3, 10))
        self.botao0.grid(row=6, column=0, pady=(3, 10))

    def criaBotao(self, conteiner, texto, funcao):
        botao = Button(conteiner, width=40, pady=10) # criando os botões
        botao['text'] = texto               # atribuindo nome
        botao.bind('<Button-1>', funcao)    # adicionando evento
        botao["font"] = ("Calibri", "13")   # fonte
        botao.pack()                        # salvando o botão

        return botao

    def getFile(self, event):
        self.nomeArquivo = filedialog.askopenfilename(initialdir = ".",title = "Selecione o arquivo",filetypes = (("Planilha","*.xlsx"),("Todos arquivos","*.*")))

    def mensagemErro(self):
        mensagem = Tk()
        Mensagem(mensagem, "Selecione um arquivo usando o primeiro botão.")
        mensagem.title('Aviso')
        mensagem.mainloop()

    def release1(self, event):
        if self.nomeArquivo.__eq__(''):
            threading.Thread(target=self.mensagemErro).start()
        else:
            wk.release1(self.nomeArquivo)

    def release2(self, event):
        if self.nomeArquivo.__eq__(''):
            threading.Thread(target=self.mensagemErro).start()
        else:
            wk.release1(self.nomeArquivo)

    def release3(self, event):
        if self.nomeArquivo.__eq__(''):
            threading.Thread(target=self.mensagemErro).start()
        else:
            wk.release1(self.nomeArquivo)

    def release4(self, event):
        if self.nomeArquivo.__eq__(''):
            threading.Thread(target=self.mensagemErro).start()
        else:
            wk.release1(self.nomeArquivo)

    def todasReleases(self, event):
        if self.nomeArquivo.__eq__(''):
            threading.Thread(target=self.mensagemErro).start()
        else:
            wk.release1(self.nomeArquivo)


root = Tk()
root.title('Macrofitas Mining')
root.geometry("800x600")
root.resizable(0, 0)
Menu(root)
root.mainloop()