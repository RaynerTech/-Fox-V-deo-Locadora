"""
...A Python GUI  - transforma tkinter, Qt, Remi, WxPython 
em interfaces portáteis e amigáveis ​...
"""


import PySimpleGUI as sg
"""
#O tema pode ser escolhido na documentação do
pacote e podemos passar como parementos 
alteraçoes usando algumas propiedades 
"""
sg.theme('DarkBlue7')

# O meu freme foi criado dentro de uma lista
frame = [  [sg.Text('FOX VIDEO LOCADORA',text_color='red', background_color='green', font='roboto 20')],
            [sg.Text('INFOMAÇÕES DO CLIENTE',font='roboto 15')],
            [sg.Text('CPF   '),sg.Input(key='cpf')],
            [sg.Text('NOME'), sg.Input(key='nome')],
            [sg.Text('RG'), sg.Input(key='rg')],
            [sg.Text('Código'), sg.Input(key='codigo')],
            [sg.Text('Filme  '),sg.Input(key='filme')],
            [sg.Text('lançamento'), sg.Input(key='lancamento')],
            [sg.Button('Enviar'), sg.Button('Cancel')],
            [sg.Output(size=(50,20))]
#passamdo o output com um tamanho definido para mostras na tela do layout os valores
            
]

#com esse comando posso criar uma janela
win = sg.Window('Fox Video Locadora').layout(frame)

#loop para obter os valores 
while True:
    event, values = win.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': 
        break
    print(f'Informações do Cliente \n Nome:  {values["nome"]} \n CPF: {values["cpf"]} \n RG: {values["rg"]} \n Codigo: {values["codigo"]} \n Filme: {values["filme"]} \n Lançãmento: {values["lancamento"]} ')
    print('='*20)
    print(f'Informações do Produto  \n Codigo: {values["codigo"]} \n Filme: {values["filme"]} \n Lançãmento: {values["lancamento"]} ')
win.close()