import PySimpleGUI as sg
equation = ""

listOfOps = ['*', '/', '+', '-', '%', '**']

def addtoequation(event):
    global equation
    if event == '1':
        equation = f"{equation}1"
    elif event == '2':
        equation = f"{equation}2"
    elif event == '3':
        equation = f"{equation}3"
    elif event == '4':
        equation = f"{equation}4"
    elif event == '5':
        equation = f"{equation}5"
    elif event == '6':
        equation = f"{equation}6"
    elif event == '7':
        equation = f"{equation}7"
    elif event == '8':
        equation = f"{equation}8"
    elif event == '9':
        equation = f"{equation}9"
    elif event == '0':
        equation = f"{equation}0"
    elif event == '00':
        equation = f"{equation}00"
    elif event == '⬅':
        equation = equation[0:-1]
    elif event == 'X':
        if equation[-1] not in listOfOps:
            equation = f"{equation}*"
    elif event == '÷':
        if equation[-1] not in listOfOps:
            equation = f"{equation}/"
    elif event == '-':
        if equation[-1] not in listOfOps:
            equation = f"{equation}-"
    elif event == '.':
        if equation[-1] not in listOfOps:
            equation = f"{equation}."
    elif event == '=':
        if equation[-1] not in listOfOps:
            equation = str(eval(equation))
    elif event == '+':
        if equation[-1] not in listOfOps:
            equation = f"{equation}+"
    elif event == '^':
        if equation[-1] not in listOfOps:
            equation = f"{equation}**"
    elif event == '%':
        if equation[-1] not in listOfOps:
            equation = f"{equation}%"
    try:
        equation_display = equation.replace('*','x')
        equation_display = equation_display.replace('/','÷')
        equation_display = equation_display.replace('**','^')
    except:
        return
    window['-TEXT-'].update(equation_display)


sg.change_look_and_feel('Dark Blue 3')   # Add a touch of color
# All the stuff inside the window.
font = ("Arial, 25")
ButtonFont = ("Arial, 13")
layout = [  [sg.Text('0',key='-TEXT-', font = font)],
            [sg.Button('1', size=(6,3), font = ButtonFont), sg.Button('2', size=(6,3), font = ButtonFont), sg.Button('3', size=(6,3), font = ButtonFont), sg.Button('⬅', size=(6,3), font = ButtonFont)],
            [sg.Button('4', size=(6,3), font = ButtonFont), sg.Button('5', size=(6,3), font = ButtonFont), sg.Button('6', size=(6,3), font = ButtonFont), sg.Button('X', size=(6,3), font = ButtonFont)],
            [sg.Button('7', size=(6,3), font = ButtonFont), sg.Button('8', size=(6,3), font = ButtonFont), sg.Button('9', size=(6,3), font = ButtonFont), sg.Button('÷', size=(6,3), font = ButtonFont)],
            [sg.Button('^', size=(6,3), font = ButtonFont), sg.Button('0', size=(6,3), font = ButtonFont), sg.Button('%', size=(6,3), font = ButtonFont), sg.Button('-', size=(6,3), font = ButtonFont)],
            [sg.Button('=', size=(6,3), font = ButtonFont), sg.Button('00', size=(6,3), font = ButtonFont), sg.Button('.', size=(6,3), font = ButtonFont), sg.Button('+', size=(6,3), font = ButtonFont)]]

# Create the Window
window = sg.Window('Calculator', layout,size=(290, 420)) #290,360

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.Read()
    if event in (None, 'Exit'):
        break
    addtoequation(event)


window.close()