A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, R, S, T, U, V = "ABCDEFGHIJKLMNOPRSTUV"

zemljevid = {
    (A, B): "gravel trava",
    (A, V): "pešci lonci",
    (B, C): "bolt lonci",
    (B, V): "",
    (C, R): "stopnice pešci lonci",
    (D, F): "stopnice pešci",
    (D, R): "pešci",
    (E, I): "trava lonci",
    (F, G): "trava črepinje",
    (G, H): "črepinje pešci",
    (G, I): "avtocesta",
    (H, J): "robnik bolt",
    (I, M): "avtocesta",
    (I, P): "gravel",
    (I, R): "stopnice robnik",
    (J, K): "",
    (J, L): "gravel bolt",
    (K, M): "stopnice bolt",
    (L, M): "robnik pešci",
    (M, N): "rodeo",
    (N, P): "gravel",
    (O, P): "gravel",
    (P, S): "",
    (R, U): "trava pešci",
    (R, V): "pešci lonci",
    (S, T): "robnik trava",
    (T, U): "gravel trava",
    (U, V): "robnik lonci trava"
}

mali_zemljevid = {(A, B): "robnik bolt",
                  (A, C): "bolt rodeo pešci",
                  (C, D): ""}

kratice = {
    "stopnice": "Spust po stopnicah",
    "pešci": "Divjanje med pešci",
    "lonci": "Slalom med cvetličnimi lonci",
    "bolt": "Slalom med odvrženimi skiroji",
    "robnik": "Skok na robnik pločnika",
    "gravel": "Vožnja po razsutem makadamu",
    "trava": "Oranje zelenic parkov",
    "avtocesta": "Vožnja po avtocesti",
    "crepinje": "Vožnja po razbiti steklovini",
    "rodeo": "Vožnja po kolesarski poti skozi Črnuče"
}

def mnozica_vescin(s):
    masterArr = []
    tmp = s.split(" ")
    for el in tmp:
        masterArr.append(kratice[el])
    masterArr = set() if s == "" else masterArr
    return set(masterArr)

#print(mnozica_vescin("robnik bolt stopnice"))

def dvosmerni_zemljevid(zemljevid):
    masterDict = {}
    zKeys = zemljevid.keys()
    for el in zKeys:
        tmp = (el[0], el[1])
        tmpR = (el[1], el[0])
        shorts = []
        splitAccess = zemljevid[tmp].split(" ")
        if zemljevid[tmp] == "" or zemljevid[tmp] == None:
            masterDict[el] = set()
            masterDict[tmpR] = set()
        else:
            for item in splitAccess:
                if item in kratice.keys():
                    shorts.append(kratice[item])
            masterDict[el] = set(shorts)
            masterDict[tmpR] = set(shorts)

    return masterDict


print(dvosmerni_zemljevid({(A, B): "robnik bolt",(A, C): "bolt rodeo pešci",(C, D): ""}))