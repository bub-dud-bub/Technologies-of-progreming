import PySimpleGUI as sg
import random

def number_checker(inp):
    for i in range(0, 3):
        for n in range(i+1, 4):
            if (inp[i]==inp[n]):
                return False
    return True


def player_guess(goal, inp, _try):
    form = sg.FlexForm('Simple data entry form')
    layout = [
          [sg.Text("Задумано четырёхзначное число:"+str(goal), size=(40, 1))],
          [sg.Text("Угадай число:", size=(10, 1)), sg.InputText('', key='inp')],
          [sg.Submit("Ок"), sg.Submit("Главное меню")]
         ]
    if (inp==None):
        pass
    elif (inp>=1000 and inp<=9999):
        cow, bull = 0, 0
        inp = str(inp)
        goal = str(goal)
        if (number_checker(inp)==False):
            layout.append([sg.Text("Цифры числа не должны повторяться", size=(30, 1))])
        for i in range(0, 4):
            for n in range(0, 4):
                if (inp[i]==goal[n]):
                    if i==n:
                        bull+=1
                    else:
                        cow+=1
        if len(layout)==3:
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


def machine_think(inp, _try, cow, bull, all_dig):
    if bull == 4:
        victory(_try)
    elif (cow==0 and bull==0):
        for t in all_dig:
            for i in range (0, 4):
                for n in range (0, 4):
                    t = str(t)
                    if t[i]==inp[n]:
                        all_dig.remove(t)
    elif (cow==4):
        for t in all_dig:
            for i in range (0, 4):
                n = 0
                while n < 4:
                    if str(t[i])==inp[n]:
                        break
                    n+=1
                if n==4:
                    all_dig.remove(t)
                    break
    else:
        for t in all_dig:
            save = False
            for i in range (0, 4):
                for n in range (0, 4):
                    t = str(t)
                    if (t[i]==inp[n]):
                        save = True
            if save == False:
                all_dig.remove(int(t))
    inex = random.randint(0, len(all_dig))
    _try+=1
    machine_guess(all_dig[index], _try, all_dig)

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


def machine_guess(inp, _try, all_dig):
    form = sg.FlexForm('Simple data entry form')
    layout = [
          [sg.Text("Программа предложила число: "+str(inp), size=(50, 1))],
          [sg.Text("Введите число коров:", size=(30, 1)), sg.InputText('', key='cow')],
          [sg.Text("Введите число быков:", size=(30, 1)), sg.InputText('', key='bull')],
          [sg.Submit("Ок"), sg.Submit("Главное меню")]
         ]
    window = sg.Window("Demo", layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Ок":
            window.close()
            machine_think(str(inp), _try, int(values['cow']), int(values['bull']), all_dig)
            return 0
        if event == "Главное меню":
            window.close()
            break



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
    if event == "Загадать число программе":
        layout = [
              [sg.Text("Задумайте четырёхзначное число с неповторяющимися цифрами. Программа попытается угадать его.", size=(100, 1))],
              [sg.Submit("Начать игру")]
             ]
        window = sg.Window("Demo", layout)
        all_dig = []
        for i in range(1000,10000):
            if (number_checker(str(i))==True):
                all_dig.append(i)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            if event == "Начать игру":
                window.close()
                index = random.randint(0, len(all_dig))
                machine_guess(all_dig[index], 1, all_dig)
                break
            if event == "Главное меню":
                window.close()
                break
