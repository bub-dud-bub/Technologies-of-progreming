import PySimpleGUI as sg

def player_guess(goal, inp, _try):
    form = sg.FlexForm('Simple data entry form')
    layout = [
          [sg.Text("Задумано четырёхзначное число:"+str(goal), size=(30, 1))],
          [sg.Text("Угадай число:", size=(10, 1)), sg.InputText('', key='inp')],
          [sg.Submit("Ок"), sg.Submit("Главное меню")]
         ]
    if (inp==None):
        pass
    elif (inp>=1000 and inp<=9999):
        cow, bull = 0, 0
        inp = str(inp)
        goal = str(goal)
        for i in range(0, 4):
            for n in range(0, 4):
                if (inp[i]==goal[n]):
                    if i==n:
                        bull+=1
                    else:
                        cow+=1
        layout.append([sg.Text("Коровы - "+str(cow)+", Быки - "+str(bull), size=(30, 1))])
        _try+=1
    else:
        layout.append([sg.Text("Число надо четырёхзначное", size=(30, 1))])

    window = sg.Window("Demo", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Ок":
            window.close()
            if int(values['inp']) == goal:
                victory(_try)
                return 0
            break
        if event == "Главное меню":
            window.close()
            return 0
    player_guess(goal, int(values['inp']), _try)

def machine_guess(inp, cow, bull, _try, all_dig, true_dig):
    inp = str(inp)
    if bull == 4:
        victory(_try)
    elif cow == 4:
        for i in range (0, 4):
            true_dig.[i] = str(inp[i])
    elif (cow==0 and bull==0):
        for i in range (0, 4):
            all_dig.remove(str(inp[i]))
    else:
        
        machine_input(1000*int(inp[0]) + 100*int(inp[1]) + 10*inp[2] + )


def victory(_try):
    form = sg.FlexForm('Simple data entry form')
    layout = [
          [sg.Text("Вы угадали!:", size=(30, 1))],
          [sg.Text("Число попыток: "+str(_try), size=(30, 1))],
          [sg.Submit("Играть снова"), sg.Submit("Главное меню")]
         ]
    window = sg.Window("Demo", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Играть снова":
            player_guess(3219, None, 1)
        if event == "Главное меню":
            return 0




form = sg.FlexForm('Simple data entry form')
layout = [
      [sg.Text("Выберите режим:", size=(30, 1))],
      [sg.Submit("Угадать число программы"), sg.Submit("Загадать число программе")]
     ]
window = sg.Window("Demo", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Угадать число программы":
        player_guess(3219, None, 1)
