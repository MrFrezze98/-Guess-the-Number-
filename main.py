import PySimpleGUI as sg
import logic

def main():
    sg.theme('LightBlue2')

    layout = [
        [sg.Text("Ласкаво просимо до гри 'Вгадай число'!", size=(30, 1), justification='center')],
        [sg.Text("Введіть число між 1 та 100:", size=(30, 1), justification='center')],
        [sg.InputText(size=(10, 1), key='-INPUT-')],
        [sg.Button('Вгадати'), sg.Button('Вийти')],
        [sg.Text('', size=(30, 1), key='-OUTPUT-', justification='center')],
    ]

    window = sg.Window('Гра "Вгадай число"', layout, finalize=True)
    
    logic.setup_game()

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, 'Вийти'):
            break

        result = logic.play_round(values['-INPUT-'])
        window['-OUTPUT-'].update(result)

    window.close()

if __name__ == "__main__":
    main()
