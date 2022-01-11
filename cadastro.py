import PySimpleGUI as sg
texto1 = str(input("digite um texto para o primeiro caixa "))
texto2 = str(input("digite outro texto para o outro caixa"))
texto3 = str(input("digita o karalho agora "))
layout = [
            [sg.Text(texto1), sg.In(key=1)],
            [sg.Text(texto2), sg.In(key=2)],
            [sg.Text(texto3), sg.In(key=3)],
            [sg.Button('Save'), sg.Button('Exit')]
]
window = sg.Window('Primeira janela do rosendo', layout)
event, values = window.read()

