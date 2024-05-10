import os
from colorama import Fore, Back, Style
from pynput.keyboard import Controller
import time
import random

keyboard = Controller()


#Координаты врагов
x1, y1 = 35, 2
x2, y2 = 10, 8
x3, y3 = 34, 7


hp_enemy_1 = 10
hp_enemy_2 = 15
hp_enemy_3 = 17

#Название объектов на карте
stone = '░'
ground = '░'
lava = '▓'
water = '▒'
player = '#'
wall1 = '║'
wall2 = '═'
uplwall = '╔'
uprwall = '╗'
dlwall = '╚'
drwall = '╝'    
web = '*'
underground = '?'
key = 'Ю'
money = '+'
enemy = '!'
heal = 'H'
trap = 'X'
tree = 'T'
sword = 'S'
trans = '~'
runduk = 'R'
fruit = 'F'



door = '-'
door_key = 0
door_under = '|'


heal_points_p = 100

fr_1 = 10 
fr_2 = 20 
money_p = 0


#Объекты, которые нельзя пройти
dangerous = [lava, water, tree, uplwall, wall2, dlwall, wall1, drwall, uprwall, door]

#Flag
fl_dead_or_life_1 = 0
fl_dead_or_life_2 = 0
fl_dead_or_life_3 = 0
fl_sword = 0
fl_trap = 0
fl_sp = 1
fl_fight = 0
fl_tab = 0

#Координаты игрока
x = 5
y = 5
#Локации
sp1 = [[uplwall, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, uprwall], 
[wall1, tree, tree, tree, tree, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, water, water, water, wall1], 
[wall1, tree, tree, ground, ground, ground, ground, ground, ground, ground, ground, water, water, water, ground, ground, ground, water, water, wall1], 
[wall1, trap, ground, ground, ground, ground, ground, ground, ground, trap, ground, water, water, ground, ground, ground, ground, ground, money, wall1], 
[trans, ground, ground, trap, ground, ground, ground, ground, ground, ground, ground, money, ground, ground, ground, ground, ground, ground, ground, wall1],
[wall1, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, wall1], 
[wall1, water, water, ground, ground, ground, ground, ground, ground, tree, tree, ground, ground, ground, ground, ground, ground, trap, ground, wall1], 
[wall1, water, water, water, money, ground, ground, tree, tree, tree, water, tree, ground, ground, ground, ground, ground, ground, ground, wall1], 
[wall1, water, water, water, ground, ground, tree, tree, tree, tree, water, tree, ground, ground, ground, ground, money, ground, ground, wall1],
[dlwall, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, drwall]]


sp2 = [[uplwall, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, trans, trans, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, uprwall], 
[wall1, ground, ground, ground, ground, ground, trap, ground, ground, ground, ground, water, water, water, water, ground, ground, ground, ground, wall1], 
[wall1, ground, ground, water, ground, water, ground, ground, ground, ground, water, ground, ground, ground, ground, water, water, ground, ground, wall1], 
[wall1, water, water, ground, ground, ground, water, water, water, water, ground, ground, ground, ground, ground, ground, ground, water, water, wall1], 
[trans, ground, sword, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, trans],
[wall1, water, water, water, water, ground, ground, trap, ground, ground, ground, ground, water, water, water, water, water, water, ground, wall1], 
[wall1, tree, tree, tree, tree, water, ground, ground, ground, ground, ground, water, water, ground, ground, ground, ground, ground, ground, wall1], 
[wall1, water, water, tree, tree, tree, water, water, ground, ground, water, ground, ground, ground, ground, tree, tree, tree, tree, wall1], 
[wall1, water, water, water, water, tree, tree, water, water, ground, ground, trap, ground, tree, tree, tree, water, water, water, wall1], 
[dlwall, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, trans, trans, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, drwall]]


sp3 = [[uplwall, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, uprwall], 
[wall1, ground, ground, ground, ground, water, water, water, tree, tree, ground, ground, ground, ground, ground, ground, ground, ground, trap, wall1], 
[wall1, ground, ground, ground, ground, water, water, water, tree, tree, trap, ground, ground, ground, ground, trap, ground, ground, ground, wall1], 
[wall1, ground, ground, ground, water, water, water, tree, tree, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, wall1], 
[wall1, ground, ground, water, water, water, tree, tree, ground, ground, ground, ground, ground, trap, ground, ground, ground, ground, ground, trans],
[wall1, ground, ground, water, water, water, tree, tree, ground, ground, trap, ground, ground, ground, ground, ground, ground, ground, tree, wall1], 
[wall1, ground, water, water, water, tree, tree, ground, ground, ground, ground, ground, ground, ground, ground, ground, tree, tree, tree, wall1], 
[wall1, ground, water, water, water, tree, tree, ground, ground, ground, ground, ground, ground, ground, ground, tree, tree, tree, tree, wall1], 
[wall1, water, water, water, tree, tree, ground, trap, ground, trap, ground, ground, ground, ground, tree, tree, tree, tree, tree, wall1], 
[dlwall, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, drwall]]


sp4 = [[uplwall, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, uprwall], 
[wall1, tree, tree, tree, tree, tree, tree, tree, tree, tree, tree, tree, tree, tree, tree, tree, tree, tree, tree, wall1],
[wall1, tree, ground, ground, ground, water, water, water, water, tree, tree, ground, ground, ground, ground, ground, ground, tree, key, wall1], 
[wall1, tree, ground, tree, ground, water, water, water, water, water, water, water, tree, ground, tree, tree, tree, tree, ground, wall1], 
[wall1, tree, ground, tree, ground, tree, tree, tree, tree, tree, tree, tree, tree, ground, water, tree, tree, tree, ground, wall1], 
[wall1, tree, ground, tree, ground, tree, ground, ground, ground, ground, ground, ground, ground, ground, water, water, water, ground, ground, wall1],
[wall1, tree, ground, tree, ground, tree, ground, tree, ground, tree, tree, tree, tree, ground, water, water, water, water, ground, wall1], 
[wall1, tree, ground, tree, ground, tree, ground, tree, ground, tree, tree, tree, tree, ground, water, water, water, water, ground, wall1], 
[wall1, tree, tree, tree, ground, ground, ground, tree, ground, ground, ground, tree, tree, ground, ground, ground, ground, ground, ground, wall1], 
[dlwall, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, trans, trans, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, drwall]]


sp5 = [[uplwall, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, trans, trans, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, uprwall], 
[wall1, tree, water, water, water, water, water, water, tree, ground, ground, tree, water, water, water, water, water, water, tree, wall1], 
[wall1, tree, water, water, water, water, water, water, tree, ground, ground, tree, water, water, water, water, water, water, tree, wall1], 
[wall1, tree, water, water, water, water, water, water, tree, door, door, tree, water, water, water, water, water, water, tree, wall1], 
[wall1, tree, water, water, water, water, water, water, tree, ground, ground, tree, water, water, water, water, water, water, tree, wall1],
[wall1, tree, water, water, water, water, water, water, tree, ground, ground, tree, water, water, water, water, water, water, tree,  wall1], 
[wall1, tree, water, water, water, water, water, water, tree, underground, underground, tree, water, water, water, water, water, water, tree, wall1], 
[wall1, tree, water, water, water, water, water, water, tree, tree, tree, tree, water, water, water, water, water, water, tree, wall1], 
[wall1, tree, water, water, water, water, water, water, tree, tree, tree, tree, water, water, water, water, water, water, tree, wall1], 
[dlwall, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, drwall]]
[wall1, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, ground, wall1]

#Локация подземелья
sp_under = [[uplwall, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, uprwall],
[wall1, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, wall1],
[wall1, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, wall1],
[wall1, stone, stone, stone, stone, lava, lava, lava, lava, lava, lava, lava, lava, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, wall1],
[wall1, stone, stone, stone, lava, lava, stone, stone, stone, stone, stone, lava, lava, lava, lava, lava, lava, lava, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, wall1],
[wall1, stone, stone, lava, lava, stone, stone, stone, stone, stone, stone, stone, stone, stone, lava, lava, lava, lava, lava, lava, lava, lava, lava, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, lava, lava, lava, lava, stone, wall1],
[wall1, stone, stone, lava, lava, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, lava, lava, lava, stone, stone, stone, stone, lava, wall1],
[wall1, stone, stone, lava, lava, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, lava, lava, lava, stone, stone, stone, stone, stone, stone, stone, lava, wall1],
[wall1, stone, stone, lava, lava, lava, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, lava, lava, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, lava, wall1],
[wall1, stone, stone, lava, lava, lava, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, lava, lava, stone, stone, stone, stone, stone, stone, stone, stone, stone, lava, lava, wall1],
[wall1, stone, stone, lava, lava, lava, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, lava, lava, stone, stone, stone, stone, stone, lava, stone, stone, stone, lava, lava, wall1],
[wall1, stone, stone, lava, lava, lava, stone, stone, stone, stone, stone, stone, stone, stone, lava, lava, lava, stone, stone, stone, stone, stone, stone, stone, stone, stone, lava, lava, stone, stone, stone, stone, stone, lava, stone, stone, stone, lava, lava, wall1],
[wall1, stone, stone, lava, lava, lava, lava, stone, stone, stone, stone, stone, stone, lava, lava, lava, lava, lava, lava, stone, stone, stone, stone, stone, stone, stone, stone, lava, stone, stone, stone, stone, lava, lava, stone, stone, stone, lava, lava, wall1],
[wall1, stone, stone, lava, lava, lava, lava, lava, stone, stone, stone, stone, lava, lava, lava, lava, lava, lava, lava, lava, lava, lava, lava, stone, stone, stone, stone, stone, stone, stone, stone, stone, lava, lava, stone, stone, stone, lava, lava, wall1],
[wall1, stone, stone, lava, lava, lava, lava, lava, stone, stone, stone, lava, lava, lava, lava, stone, stone, stone, stone, stone, lava, lava, lava, lava, lava, lava, stone, stone, stone, stone, stone, lava, lava, stone, stone, stone, stone, lava, lava, wall1],
[wall1, stone, stone, lava, lava, lava, lava, lava, lava, stone, lava, lava, lava, stone, stone, stone, stone, stone, stone, stone, stone, stone, lava, lava, lava, lava, lava, lava, stone, stone, lava, lava, lava, stone, stone, stone, stone, lava, lava, wall1],
[wall1, stone, stone, lava, lava, lava, lava, lava, lava, lava, lava, lava, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, lava, lava, lava, lava, stone, stone, stone, stone, stone, lava, lava, lava, wall1],
[wall1, stone, stone, lava, lava, lava, lava, lava, lava, lava, lava, lava, stone, stone, stone, runduk, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, door_under, stone, stone, stone, stone, stone, stone, lava, lava, lava, lava, wall1],
[wall1, stone, stone, lava, lava, lava, lava, lava, lava, lava, lava, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, door_under, stone, stone, stone, stone, stone, stone, lava, lava, lava, lava, wall1],
[wall1, underground, underground, lava, lava, lava, lava, lava, lava, lava, lava, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, stone, door_under, stone, stone, stone, stone, lava, lava, lava, lava, lava, lava, wall1],
[dlwall, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, wall2, drwall]]


sp = sp1


    
#Функция вывода поля (локации)
def pol(sp):
    global x1, x2, x3, y1, y2, y3
    os.system('cls')#Отчищает строку(вывод)
    print('Ваши хп:', heal_points_p)
    print('Ваши деньги:', money_p)
    for i in range(fr_1):#Вывод врагов
        for j in range(fr_2):
            if i == y and j == x:
                print(player, end='')
            elif i == y1 and j == x1 and sp == sp_under and fl_dead_or_life_1 == 0:
                print(enemy, end='')
                continue
            elif i == y2 and j == x2 and sp == sp_under and fl_dead_or_life_2 == 0:
                print(enemy, end='')
                continue
            elif i == y3 and j == x3 and sp == sp_under and fl_dead_or_life_3 == 0:
                print(enemy, end='')
                continue
                
                
            #Вывод всех остальных объектов и их цветов
            elif sp[i][j] == runduk and sp == sp_under:
                print(Fore.YELLOW + sp[i][j] + Fore.RESET, end='')
            elif sp[i][j] == ground and sp != sp_under:
                print(Fore.GREEN + sp[i][j] + Fore.RESET, end='')
            elif sp[i][j] == water:
                print(Fore.CYAN + sp[i][j] + Fore.RESET, end='')
            elif sp[i][j] == tree:
                print(Fore.GREEN + sp[i][j] + Fore.RESET, end='')
            elif sp[i][j] == lava:
                print(Fore.RED + sp[i][j] + Fore.RESET, end='')
            elif sp[i][j] == trap:
                print(Fore.MAGENTA + sp[i][j] + Fore.RESET, end='')
            elif sp[i][j] == money:
                print(Fore.YELLOW + sp[i][j] + Fore.RESET, end='')
            elif sp[i][j] == stone:
                print(Fore.WHITE + sp[i][j] + Fore.RESET, end='')
            elif sp[i][j] == fruit:
                print(Fore.YELLOW + sp[i][j] + Fore.RESET, end='')
            
            else:   
                print(sp[i][j], end='')
        print()




#Дэнги, непонятно зачем, но они есть
def func():
    global sp, y, x, money_p

    if sp[y][x] == money:
            sp[y][x] = ground
            os.system('cls')
            pol(sp)
            return 30    





def transition():#Переход между локациями
    global sp, fl_sp, x, y, fr_1, fr_2
    if sp[y][x] == trans and fl_sp == 1:
        sp = sp2
        fl_sp = 2
        x, y = 18, 4
        pol(sp)
    elif sp[y][x] == trans and fl_sp == 2  and x == 19 and y == 4:
        sp = sp1
        fl_sp = 1
        x, y = 1, 4
        pol(sp)
    elif sp[y][x] == trans and fl_sp == 2 and y == 9:
        sp = sp5
        fl_sp = 3
        x, y =  10, 1
        pol(sp)
    elif sp[y][x] == trans and fl_sp == 2 and y == 0:
        sp = sp4
        fl_sp = 4
        x, y =  9, 8
        pol(sp)
    elif sp[y][x] == trans and fl_sp == 2 and x == 0 and y == 4:
        sp = sp3
        fl_sp = 5
        x, y = 18, 4
        pol(sp)



    elif sp[y][x] == trans and fl_sp == 3:
        sp = sp2
        fl_sp = 2
        x, y = 9, 8
        pol(sp)
    elif sp[y][x] == trans and fl_sp == 4:
        sp = sp2
        fl_sp = 2
        x, y = 10, 1
        pol(sp)
    elif sp[y][x] == trans and fl_sp == 5:
        sp = sp2
        fl_sp = 2
        x, y = 1, 4
        pol(sp)
    
    elif sp[y][x] == underground and fl_sp == 3 and fl_sword == 1:
        sp = sp_under
        fl_sp = 6
        
        fr_1 = 21
        fr_2 = 40
        x, y = 1,18
        pol(sp)

    elif sp[y][x] == underground and fl_sp == 6:
        sp = sp5
        fl_sp = 3
        
        fr_1 = 10
        fr_2 = 20
        x, y = 10, 6
        pol(sp)




def enemy_shag_1():
    global x1, y1
    if fl_dead_or_life_1 == 0:
        spx = [-1, 1]
        spy = [-1, 1]
        ch = [1, 2]
        x1, y1 = 35, 2
        if sp == sp_under:
            if random.choice(ch) == 1:
                x1 += random.choice(spx)
            else:
                y1 += random.choice(spy)
def enemy_shag_2():
    global x2, y2
    if fl_dead_or_life_2 == 0:
        ch = [1, 2]
        spx = [-1, 1]
        spy = [-1, 1]
        x2, y2 = 10, 8
        if sp == sp_under:
            if random.choice(ch) == 1:
                x2 += random.choice(spx)
            else:
                y2 += random.choice(spy)
def enemy_shag_3():
    global x3, y3
    if fl_dead_or_life_3 == 0:
        ch = [1, 2]
        spx = [-1, 1]
        spy = [-1, 1]
        x3, y3 = 34, 7
        if sp == sp_under:
            if random.choice(ch) == 1:
                x3 += random.choice(spx)
            else:
                y3 += random.choice(spy)
def enemy_fight():
    global x, y, x1, x2, x3, y1, y2, y3, hp_enemy_1, hp_enemy_2, hp_enemy_3, fl_dead_or_life_1, fl_dead_or_life_2, fl_dead_or_life_3, fl_fight, door_key
    
    
    #Функции врагов
    if x == x1 and y == y1:
        chance = [1, 0, 0]
        damage_1 = [5, 10]
        hp_enemy_1 -= random.choice(damage_1)
        if hp_enemy_1 <= 0:
            print('Ты убил врага!!!')
            fl_dead_or_life_1 = 1
            y += 1
            time.sleep(1)
            x1, y1 = 10, 19
            if random.choice(chance) == 1 and door_key <= 1 :
                door_key += 1
                pol(sp)
        else:
            print('Не убил(')
    
    
    if x == x2 and y == y2:
        chance = [0, 1, 0]
        damage_2 = [5, 15]
        hp_enemy_2 -= random.choice(damage_2)
        if hp_enemy_2 <= 0:
            print('Ты убил врага!!!')
            fl_dead_or_life_2 = 1
            y += 1
            time.sleep(1)
            x2, y2 = 10, 19
            if random.choice(chance) == 1 and door_key <= 1:
                door_key += 1
            pol(sp)
        else:
            print('Не убил(')
           
    
    if x == x3 and y == y3:
        chance = [0, 0, 1]
        damage_3 = [5, 17]
        hp_enemy_3 -= random.choice(damage_3)
        if hp_enemy_3 <= 0:
            print('Ты убил врага!!!')
            fl_dead_or_life_3 = 1
            y += 1
            time.sleep(1)
            x3, y3 = 10, 19
            if random.choice(chance) == 1 and door_key <= 1:
                door_key += 1
            pol(sp)
        else:
            print('Не убил(')
    fl_fight = 0


    

    
    

pol(sp)#Перемещение и вывод меню объектов
while True:
    if sp == sp_under:
        if x == x1 and y == y1 or x == x2 and y == y2 or x == x3 and y == y3:
            enemy_fight()
    if keyboard.press('w') and not sp[y - 1][x] in dangerous and fl_trap == 0 and fl_fight == 0 and fl_tab == 0:
        y -= 1
        if sp == sp_under:
            enemy_shag_1()
            enemy_shag_2()
            enemy_shag_3()
        pol(sp)
    elif keyboard.press('s') and not sp[y + 1][x] in dangerous and fl_trap == 0 and fl_fight == 0 and fl_tab == 0:    
        y += 1
        if sp == sp_under:
            enemy_shag_1()
            enemy_shag_2()
            enemy_shag_3()
        pol(sp)
    elif keyboard.press('a') and not sp[y][x - 1] in dangerous and fl_trap == 0 and fl_fight == 0 and fl_tab == 0:
        x -= 1
        if sp == sp_under:
            enemy_shag_1()
            enemy_shag_2()
            enemy_shag_3()
        pol(sp)
    elif keyboard.press('d') and not sp[y][x + 1] in dangerous and fl_trap == 0 and fl_fight == 0 and fl_tab == 0:
        x += 1
        if sp == sp_under:
            enemy_shag_1()
            enemy_shag_2()
            enemy_shag_3()
        pol(sp)
    
    if keyboard.press('Tab'):
        fl_tab = 1
        os.system('cls')
        print('''R = Рундук главное сокровищи
▓ = Лава
▒ = Вода
# = Персонаж
? = Переход на подземелье
Ю = Ключ
+ = Монетки
! = Враг
X = Ловушка
S = Меч великого война Юрнеро
~ = Перход''')
        time.sleep(0.5)
        keyboard.wait('Tab')
        fl_tab = 0
        os.system('cls')
        pol(sp)
    #Работа trap
    if sp[y][x] == trap:
        os.system('cls')
        pol(sp)
        print("Вы попались в ловушку зажмите 'e'")
        fl_trap = 1
        keyboard.wait('e')
        fl_trap = 0
        os.system('cls')
        pol(sp)
        sp[y][x] = ground
        fl = None
    
    #Интерактивные объекты
    if sp[y][x] == runduk:
        sp[y][x] == stone
        print('Ты нашел рундук!!!')
        break
        
        

    
    if sp[y][x] == sword:
        sp[y][x] = ground
        os.system('cls')
        pol(sp)
        fl_sword = 1
        print('Ты поднял меч')
        print('Теперь ты можешь идти в подземелья')
    
    #Открытие дверей
    if door_key >= 1:
        sp5[3][9] = ground
        sp5[3][10] = ground
    if door_key >= 2:
        sp_under[17][28] = stone
        sp_under[18][28] = stone
        sp_under[19][28] = stone
    if door_key == 1 and fl_dead_or_life_1 == 1 and fl_dead_or_life_2 == 1 and fl_dead_or_life_3 == 1:
        door_key = 2
    

    if heal_points_p <= 0:
        print('Ты умер, и тайна рундука ушла в небытие.')
        break
    if sp[y][x] == key:
        sp[y][x] = ground
        os.system('cls')
        pol(sp)
        door_key = 1
    
    
    transition()
    
    
    time.sleep(0.3)
    
    
    if sp[y][x] == money:
        money_p += func()
        
        
        
        
