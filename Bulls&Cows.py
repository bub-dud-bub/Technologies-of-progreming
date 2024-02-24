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
                winner = 'player'
                victory(_try, winner)
                return 0
            break
        if event == "Главное меню":
            window.close()
            return 0
    player_guess(goal, int(values['inp']), _try)


def farm(inp, _try, bull, cow, all_dig):
    new = []
    if bull == 4:
        winner = 'machine'
        victory(_try, winner)
        return 0
    elif (cow==0 and bull==0):
        for t in all_dig:
            save = True
            for i in range (0, 4):
                for n in range (0, 4):
                    tdd = str(t)
                    if tdd[i]==inp[n]:
                        save = False
            if save==False:
                pass
            else:
                new.append(t)
    elif (cow==4):
        for t in all_dig:
            c = 0
            for i in range (0, 4):
                for n in range(0, 4):
                    tdd = str(t)
                    if tdd[i]==inp[n]:
                        c+=1
                        break
            if c==4:
                new.append(t)
                print(str(t))
    elif(cow>0 and cow<4):
        for t in all_dig:
            save = False
            for i in range (0, 4):
                for n in range (0, 4):
                    tdd = str(t)
                    if (tdd[i]==inp[n]):
                        save = True
            if save == True:
                new.append(t)

    if (bull>0 and bull<4 and cow!=0):
        all_dig = new
        new = []
    if (bull==1):
        for t in all_dig:
            for i in range(0,4):
                tdd = str(t)
                if (tdd[i]==inp[i]):
                    new.append(t)
                    break
    elif (bull==2):
        for t in all_dig:
            save = False
            for i in range(0,3):
                for n in range (i+1, 4):
                    tdd = str(t)
                    if (tdd[i]==inp[i] and tdd[n]==inp[n]):
                        save = True
            if save == True:
                    new.append(t)
    elif (bull==3):
        for t in all_dig:
            tdd = str(t)
            if (tdd[0]==inp[0] and tdd[1]==inp[1] and tdd[2]==inp[2]) or (tdd[0]==inp[0] and tdd[1]==inp[1] and tdd[3]==inp[3]) or (tdd[0]==inp[0] and tdd[2]==inp[2] and tdd[3]==inp[3]) or (tdd[1]==inp[1] and tdd[2]==inp[2] and tdd[3]==inp[3]):
                new.append(t)

    if int(inp) in new:
        new.remove(int(inp))
    if len(new)==0:
        new = all_dig
    return new

def machine_think(inp, _try, cow, bull, all_dig):

    new = farm(inp, _try, bull, cow, all_dig)
    _try+=1
    inp = int(inp)
    per = 1
    pos = 3
    while per <= 1000:
        an_inp = inp
        stop = 0
        while True:
            if an_inp >= inp:
                an_inp+=per
            elif an_inp < inp:
                an_inp-=per
            if per == 1:
                old_dig, new_dig = inp % 10, an_inp % 10
            elif per == 10:
                old_dig, new_dig = inp % 100 // 10, an_inp % 100 // 10
            elif per == 100:
                old_dig, new_dig = inp % 1000 // 100, an_inp % 1000 // 100
            elif per == 1000:
                old_dig, new_dig = inp // 1000, an_inp // 1000
            if an_inp in new:
                break
            if new_dig >= 9:
                an_inp = inp-per
                stop+=1
            if new_dig <= 1:
                an_inp = inp+per
                stop+=1
            if stop==2:
                break
        if stop==2:
            pos-=1
            per*=10
            inp = an_inp
            continue
        an_inp, an_bull, an_cow = machine_guess_2(an_inp, _try, new)
        new = farm(str(an_inp), _try, an_bull, an_cow, new)
        if int(an_inp) in new:
            new.remove(int(an_inp))
        _try+=1
        if an_bull==bull and an_cow==cow:
            pos-=1
            per*=10
            inp = an_inp
            continue
        else:
            all_dig = new
            new = []
        if an_bull - bull == 1:
            for t in all_dig:
                tdd = str(t)
                if tdd[pos]==str(new_dig):
                    new.append(t)
        elif an_bull - bull == -1:
            for t in all_dig:
                tdd = str(t)
                if tdd[pos]==str(old_dig):
                    new.append(t)
        elif an_cow - cow == 1:
            for t in all_dig:
                tdd = str(t)
                for i in range(0,4):
                    if tdd[i]==str(new_dig):
                        new.append(t)
        elif an_cow - cow == -1:
            for t in all_dig:
                tdd = str(t)
                for i in range(0,4):
                    if tdd[i]==str(old_dig):
                        new.append(t)
        pos-=1
        per*=10
        inp = an_inp
        bull = an_bull
        cow = an_cow





    inex = random.randint(0, len(new)-1)
    machine_guess(new[inex], _try, new)

def victory(_try, winner):
    if winner == 'player':
        win = "Вы угадали!:"
    elif winner == 'machine':
        win = 'Программа угадала'
    form = sg.FlexForm('Simple data entry form')
    layout = [
          [sg.Text(win, size=(30, 1))],
          [sg.Text("Число попыток: "+str(_try), size=(30, 1))],
          [sg.Submit("Играть снова"), sg.Submit("Главное меню")]
         ]
    window = sg.Window("Demo", layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Играть снова":
            if winner == 'player':
                player_guess(3219, None, 1)
            elif winner == 'machine':
                all_dig = []
                for i in range(1000,10000):
                    if (number_checker(str(i))==True):
                        all_dig.append(i)
                inex = random.randint(0, len(all_dig))
                machine_guess(all_dig[inex], 1, all_dig)
        if event == "Главное меню":
            window.close()
            MainMenu()
            return 0


def machine_guess(inp, _try, all_dig):
    print(str(inp)+"\n")
    form = sg.FlexForm('Simple data entry form')
    layout = [
          [sg.Text("Программа предложила число: "+str(inp), size=(50, 1), font='Any 16')],
          [sg.Text("Введите число быков:", size=(30, 1), font='Any 12'), sg.Combo(['0', '1', '2', '3', '4'], default_value = '0', key='bull', size=(30, 6), font='Any 12')],
          [sg.Text("Введите число коров:", size=(30, 1), font='Any 12'), sg.Combo(['0', '1', '2', '3', '4'], default_value = '0', key='cow', size=(30, 6), font='Any 12')],
          [sg.Text(str(len(all_dig)))],
          [sg.Submit("Ок", font='Any 12'), sg.Submit("Главное меню", font='Any 12')]
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

def machine_guess_2(inp, _try, all_dig):
    print(str(inp)+"\n")
    form = sg.FlexForm('Simple data entry form')
    layout = [
          [sg.Text("Программа предложила число: "+str(inp), size=(50, 1), font='Any 16')],
          [sg.Text("Введите число быков:", size=(30, 1), font='Any 12'), sg.Combo(['0', '1', '2', '3', '4'], default_value = '0', key='bull', size=(30, 6), font='Any 12')],
          [sg.Text("Введите число коров:", size=(30, 1), font='Any 12'), sg.Combo(['0', '1', '2', '3', '4'], default_value = '0', key='cow', size=(30, 6), font='Any 12')],
          [sg.Text(str(len(all_dig)))],
          [sg.Submit("Ок", font='Any 12'), sg.Submit("Главное меню")]
         ]
    window = sg.Window("Demo", layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == "Ок":
            window.close()
            return inp, int(values['bull']), int(values['cow'])
            return 0
        if event == "Главное меню":
            window.close()
            break

def MainMenu():
    form = sg.FlexForm('Simple data entry form')
    layout = [
          [sg.Text("Выберите режим:", size=(30, 1), font='Any 16')],
          [sg.Submit("Угадать число программы", font='Any 12'), sg.Submit("Загадать число программе", font='Any 12')]
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
        if event == "Угадать число программы":
            inex = random.randint(0, len(all_dig))
            player_guess(all_dig[inex], None, 1)
        if event == "Загадать число программе":
            layout = [
                  [sg.Text("Задумайте четырёхзначное число с неповторяющимися цифрами. Программа попытается угадать его.", size=(100, 1), font='Any 16')],
                  [sg.Submit("Начать игру", font='Any 12')]
                 ]
            window = sg.Window("Demo", layout)

            while True:
                event, values = window.read()
                if event == sg.WIN_CLOSED:
                    break
                if event == "Начать игру":
                    window.close()
                    inex = random.randint(0, len(all_dig))
                    machine_guess(all_dig[inex], 1, all_dig)
                    break
                if event == "Главное меню":
                    window.close()
                    break
MainMenu()
