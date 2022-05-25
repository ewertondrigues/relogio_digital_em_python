#importando tkinter

from tkinter import*
from tkinter import ttk
from turtle import bgcolor
from datetime import datetime


#Cores

cor1 = "#3d3d3d" #preto
cor2 = "#fafcff" #branca
cor3 = "#21c25c" #verde
cor4 = "#eb463b" #vermelha
cor5 = "#3080f0" #azul

# Plano de Fundo do Relogio

fundo = cor1

#Cor da Fonte

fonte = cor2

#Escopo ou Corpo

janela =Tk()
janela.title("")
janela.geometry("440x180")
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg=cor1)


#Data e Hora Função

def relogio():
    tempo = datetime.now()
    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%B")
    ano = tempo.strftime("%Y")

    l1.config(text=hora)
    l1.after(200, relogio)
    l2.config(text=dia_semana + "   "  + str(dia) + "/" + str(mes) + "/" + str(ano))

#Configuração da Hora
l1 = Label(janela, text="", font=("Ivy 80"), bg=fundo, fg=cor2)
l1.grid(row=0, column=0, sticky = NW, padx = 5)


#Configuração da Data
l2 = Label(janela, text="", font=("Ivy 18"), bg=fundo, fg=cor2)
l2.grid(row=1, column=0, sticky = NW, padx = 5)



relogio()
janela.mainloop()