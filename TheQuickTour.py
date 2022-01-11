import PySimpleGUI as sg

sg.popup("Salve garai", "essa é a telinha mais simples possivel")
# sg.Window se refere a janela toda
# pra organizar as linhas, o SimpleGUI usa os colchetes [], ou seja, tudo que estiver num mesmo colchete, estará na mesma linha
event, values = sg.Window("Get filename example",
                          [[sg.Text("filename")],
                           [sg.Input(), sg.FileBrowse()],
                           [sg.OK(), sg.Cancel()]]).read(close=True)

sg.theme("Dark2")
layout = [[sg.Text("filename")],
          [sg.Input(), sg.FileBrowse()],
          [sg.OK(), sg.Cancel()], ]
window = sg.Window("get file name example", layout)
event, values = window.read()
window.close()




