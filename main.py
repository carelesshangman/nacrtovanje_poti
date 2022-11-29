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
    "črepinje": "Vožnja po razbiti steklovini",
    "rodeo": "Vožnja po kolesarski poti skozi Črnuče"
}


def mnozica_vescin(s):
    masterArr = []
    tmp = s.split(" ")
    tmp = "" if s == "" else tmp #😊
    for el in tmp:
        masterArr.append(kratice[el])
    return set(masterArr)


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


def mozna_pot(pot, zemljevid):
    canPass = 0
    for i in range(0,len(pot)-1):
        if (pot[i], pot[i + 1]) in zemljevid.keys():
            canPass += 1
        elif (pot[i + 1], pot[i]) in zemljevid.keys():
            canPass += 1
        else:
            return False
    return True


def potrebne_vescine(pot, zemljevid):
    skills = []
    tmp = ""
    for i in range(0, len(pot) - 1):
        if (pot[i], pot[i + 1]) in zemljevid.keys():
            tmp += zemljevid[(pot[i], pot[i + 1])] + " "
        elif (pot[i + 1], pot[i]) in zemljevid.keys():
            tmp += zemljevid[(pot[i + 1], pot[i])] + " "
    tmp = tmp.split(" ")
    for el in tmp:
        if el != "":
            skills.append(kratice[el])
    return set(skills)


def nepotrebne_vescine(pot, zemljevid, vescine):
    skills = []
    tmp = ""
    vescineArr = list(vescine)
    for i in range(0, len(pot) - 1):
        if (pot[i], pot[i + 1]) in zemljevid.keys():
            tmp += zemljevid[(pot[i], pot[i + 1])] + " "
        elif (pot[i + 1], pot[i]) in zemljevid.keys():
            tmp += zemljevid[(pot[i + 1], pot[i])] + " "
    tmp = tmp.split(" ")
    for el in tmp:
        if el != "":
            skills.append(kratice[el])

    return set([elem for elem in vescineArr if elem not in skills])



def koncna_tocka(pot, zemljevid, vescine):
    skillIssue=set()
    for x in range(len(pot) - 1):
        tmp=(pot[x],pot[x+1])
        novapot=potrebne_vescine(tmp, zemljevid)
        for x in novapot:
            if x not in vescine:
                skillIssue.add(x)
        if skillIssue!=set():
            return (tmp[0],skillIssue)
