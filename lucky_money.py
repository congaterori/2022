import os
import time
import random
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("tet")
if os.name == "nt":
    os.system('cd tet && tet.bat')
def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
print("\033[0;33;40m")
clear()
def type(file):
    a = open(file,"r")
    print(a.read())
    a.close()
type("tet/logo.txt")
time.sleep(3)
print("\033[0;32;40m")
clear()
type("tet/logo.txt")
type("tet/luckeymoney.txt")
input("Press any key to continue . . . ")
clear()
lixi = True
while lixi:
    print("\033[0;31;40m")
    clear()
    type("tet/li_xi.txt")
    time.sleep(1)
    clear()
    type("tet/li_xi_2.txt")
    time.sleep(1)
    clear()
    type("tet/li_xi.txt")
    print("\033[1;32;40mChoose a number\033[0m")
    print("\033[0;37;40m")
    print("1.Open")
    print("2.Get another")
    print("3.Exit")
    try:
        choose = int(input())
    except:
        clear()
        print("you only can choose number 1-3")
        input("Press any key to continue . . . ")
        lixi = True
    if choose == 1:
        open_file = True
        while open_file:
            clear()
            print("\033[0;31;40m")
            type("tet/li_xi_open.txt")
            print()
            print("loading...")
            time.sleep(3)
            clear()
            break
        showme = True
        while showme:
            print("\033[0;32;40m")
            clear()
            list1 = [1, 2, 3, 4, 5, 6, 7]
            num = random.choice(list1)
            clear()
            print("Congratulations you got:")
            if num == 1:
                type("tet/money/1bigdola.txt")
            if num == 2:
                type("tet/money/1dola_old.txt")
            if num == 3:
                type("tet/money/1dola.txt")
            if num == 4:
                type("tet/money/50dola.txt")
            if num == 5:
                type("tet/money/100dola.txt")
            if num == 6:
                type("tet/money/combo100dola.txt")
            if num == 7:
                type("tet/money/fivedola_gold.txt")
            input("")
            break
    if choose == 3:
        exit()