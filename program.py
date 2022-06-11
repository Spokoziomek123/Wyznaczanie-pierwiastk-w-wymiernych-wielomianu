import os
def screen_clear():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
from time import sleep
On = True
def wielomian(list):
    wielomian = ""
    c = len(list)-1
    if len(list) == 1:
        return str(list[0])
    for i in list:
        if i < 0:
            if c==0:
                wielomian += (str(i))
            elif i==-1 and c!=1:
                wielomian += ("-" + "x^" + str(c))
            elif i==-1 and c==1:
                wielomian += ("-"+ "x")
            else:
                wielomian += (str(i)+"x^"+str(c))
        elif i == 0:
            c-=1
            continue
        else:
            if c==1:
                wielomian += ('+' + str(i) + "x")
            elif c==0:
                wielomian += ('+' + str(i))
            else:
                wielomian += ('+'+str(i)+"x^"+str(c))
        c -= 1
    sleep(1)
    print("wielomian" + str(wielomian))
    return wielomian
def współczynniki(list):
    a = False
    while a == False:
        n = input("Podaj liczbę współczynników: ")
        try:
            n= int(n)
            a = True
        except:
            print('Podałeś złe dane')
    a = False
    for i in range(1, int(n)+1):
        while a == False:
            g = input("Podaj współczynnik: ")
            try:
                g = int(g)
                a = True
            except:
                print('Podałeś złe dane')
        list.append(g)
        a = False
    return list

def prepans(dzielnik_lewa, dzielnik_prawa):
    for i in dzielnik_lewa:
        for j in dzielnik_prawa:
            x = j / i
            f = ""
            for k in mod_eq:
                if k == "x" and x < 0:
                    f += "("
                    f += str(x)
                    f += ")"
                elif k == "x" and x >= 0:
                    f += str(x)
                else:
                    f += str(k)
            sleep(0.25)
            print("")
            print("p/q = " + str(j) + "/" + str(i) + " = " + str(x))
            print("W(" + str(int(x)) +")" + " = " + str(f) + " = " + str(eval(f)))
            print(" ")
            if eval(f) == 0.0:
                ans.append(x)
    return ans

def find_lewa(a):
    s=""
    if a[0] == "x":
        lewa = 1
    else:
        for i in a:
            if i == "x":
                break
            else:
                s += str(i)
        lewa = int(s)
    return lewa

def find_prawa(a):
    s=""
    for i in range(len(a)-1,-1,-1):
        if a[i]=="+" or a[i]=="-":
            break
        else:
            s+=a[i]
    return s[::-1]

def modify(new_a):
    mod_eq=""
    for i in range(len(new_a)):
        if new_a[i] == "x" and i != 0 and new_a[i - 1] != "+" and new_a[i - 1] != "-":
            mod_eq += '*'
            mod_eq += str(new_a[i])
        else:
            mod_eq += str(new_a[i])
    return mod_eq

def changePowers(a):
    new_a=""
    for i in a:
        if i == "^":
            new_a += "**"
        else:
            new_a += i
    return  new_a

def koniec(ans):
    f = []
    if len(ans) == 2:
        f.append(ans[0])
    else:
        for i in range(len(ans) - 1):
            check = True
            for j in range(i + 1, -1, -1):
                if ans[i] == ans[j] and i != j:
                    check = False
            if check:
                f.append(ans[i])
    return f


def find_divisors(a):
    g=[]
    for i in range(1, int(a) + 1):
        if int(a) % i == 0:
            g.append(i)
            g.append(-i)
    if int(a) < 0:
        for i in (-1, int(a), -1):
            if int(lewa) % i == 0:
                g.append(i)
                g.append(-i)
    return g
while On == True:
    list = []
    list = współczynniki(list)
    a = wielomian(list)
    ans=[]
    dzielnik_lewa=[]
    s = ""
    dzielnik_prawa=[]
    lewa=find_lewa(a)
    prawa=find_prawa(a)
    new_a=changePowers(a)
    mod_eq=modify(new_a)
    dzielnik_lewa=find_divisors(lewa)
    dzielnik_prawa=find_divisors(prawa)
    sleep(0.25)
    print("Dzielniki lewego współczynnika" + str(dzielnik_lewa))
    sleep(0.25)
    print("Dzielniki prawego współczynnika" + str(dzielnik_prawa))
    ans=prepans(dzielnik_lewa,dzielnik_prawa)
    f=koniec(ans)
    if len(f) == 0:
        sleep(0.25)
        print("Wielomian nie posiada pierwiastków wymiernych")
    else:
        sleep(0.25)
        print("pierwiastki wielomianu to: " + str(f))
    a = True
    while a == True:
        hideo = input("Chcesz skończyć TAK/NIE? : ")
        if hideo == "tak" or hideo == "TAK" or hideo == "Tak":
            a = False
            On ="False"
        elif hideo == "nie" or hideo == "NIE" or hideo =="Nie":
            a = False
            screen_clear()
        else:
            sleep(0.25)
            print("I am the storm that is approaching Provoking Black clouds in isolation I am reclaimer of my name Born in flames I have been blessed My family crest is a demon of death!")