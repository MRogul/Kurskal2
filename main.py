import numpy as np
import copy
'''
dla n od 3 do liczba wezłów

if istnieje cykl dlugosci n z wezla X
return False
return True

CzyIstniejeCykl(n, X, sciezka)
if n == 0
    sprawdz
    cykl
else
    dla
    kazdego
    bezposredniego
    sasiada
    S
    wezla
    X
    idz
    S
    if sciezka zawiera powtarzajace sie krawedzie(sciezka)
    return False
else
if CzyIstniejeCykl(n - 1, X, sciezka + S)
    return True
return False
'''

def Kruscal(Graf):
    połączenia=[]
    I_W=[]
    for i in range(len(Graf[0])):
        I_W.append(i)
        if i == len(Graf[0]):
            n=i

    P_MIN = 99
    for i in range(len(Graf[0])):
        for j in range(len(Graf[0])):
            if P_MIN > Graf[2][i][j] and [i, j] not in połączenia and [j, i] not in połączenia and Graf[1][i][j] != 0:
                P_MIN = Graf[2][i][j]
                A = i
                B = j
    połączenia.append([A,B])

    while len(połączenia) != len(Graf[0]):
        P_MIN = 99
        for i in range(len(Graf[0])):
            for j in range(len(Graf[0])):
                if P_MIN > Graf[2][i][j] and [i,j] not in połączenia and [j,i] not in połączenia and Graf[1][i][j] != 0:
                    P_MIN = Graf[2][i][j]
                    A = i
                    B = j
        odwiedzone=[]
        if cykl(Graf, połączenia, A, B, odwiedzone) == True:
            połączenia.append([A,B])
        print(odwiedzone)
    return połączenia



def cykl(Graf, połączenia, A, B, odwiedzone):
    odwiedzone.append([A,B])
    for i in range(len(połączenia)):
        if (A == połączenia[i][0] or A == połączenia[i][1]) and połączenia[i] not in odwiedzone:
            cykl(Graf, połączenia, połączenia[i][0], połączenia[i][1], odwiedzone)
        if (B == połączenia[i][0] or B == połączenia[i][1]) and połączenia[i] not in odwiedzone:
            cykl(Graf, połączenia, połączenia[i][0], połączenia[i][1], odwiedzone)
        if odwiedzone[0][0] == połączenia[i][0] or odwiedzone[0][0] == połączenia[i][1] or odwiedzone[0][1] == połączenia[i][0] or odwiedzone[0][1] == połączenia[i][1]:
            return False

    return True


if __name__ == '__main__':
    Wierzchołki = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    Połączenia = np.array([[0, 0, 1, 1, 0, 0, 0, 0],
                           [0, 0, 1, 1, 0, 0, 1, 0],
                           [1, 1, 0, 0, 0, 0, 0, 0],
                           [1, 1, 0, 0, 0, 1, 1, 1],
                           [0, 0, 0, 0, 0, 1, 0, 0],
                           [0, 0, 0, 1, 1, 0, 1, 0],
                           [0, 1, 0, 1, 0, 1, 0, 0],
                           [0, 0, 0, 1, 0, 0, 0, 0]])
    Wagi = np.array([[0, 0, 7, 10, 0, 0, 0, 0],
                     [0, 0, 8, 2, 0, 0, 1, 0],
                     [7, 8, 0, 0, 0, 0, 0, 0],
                     [10, 2, 0, 0, 0, 6, 11, 13],
                     [0, 0, 0, 0, 0, 3, 0, 0],
                     [0, 0, 0, 6, 3, 0, 5, 0],
                     [0, 1, 0, 11, 0, 5, 0, 0],
                     [0, 0, 0, 13, 0, 0, 0, 0]])

    Graf = (Wierzchołki, Połączenia, Wagi)

    print(Kruscal(Graf))