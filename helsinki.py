def beolvasas():
    olimpia = []
    helsinki = {}
    forras = open("helsinki.txt","r")
    for sor in forras:
        sor = sor.strip().split()
        sor[0] = int(sor[0])
        sor[1] = int(sor[1])
        helsinki = {
            "helyezes": sor[0],
            "sportolokszama" : sor[1],
            "sportnev" : sor[2],
            "versenyszamnev" : sor[3]
        }
        olimpia.append(helsinki)
        helsinki = {}
    forras.close()
    return olimpia


def hanyhelyezes(olimpia):
    mennyi = 0
    for i in range(len(olimpia)):
        mennyi += 1
    return mennyi

def arany(olimpia):
    hanyarany = 0
    for i in range(len(olimpia)):
        if olimpia[i]["helyezes"] == 1:
            hanyarany+=1
    return hanyarany
def ezust(olimpia):
    hanyezust = 0
    for i in range(len(olimpia)):
        if olimpia[i]["helyezes"] == 2:
            hanyezust+=1
    return hanyezust
def bronz(olimpia):
    hanybronz = 0
    for i in range(len(olimpia)):
        if olimpia[i]["helyezes"] == 3:
            hanybronz+=1
    return hanybronz
def osszerem(arany,ezust,bronz,olimpia):
    for i in range(len(olimpia)):
        osszeserem = arany+ezust+bronz
    return osszeserem

def pontokosszege(olimpia):
    olimpiaipontok = 0
    for i in range(len(olimpia)):
        if olimpia[i]["helyezes"] == 1:
            olimpiaipontok += 7
        elif olimpia[i]["helyezes"] == 2:
            olimpiaipontok += 5
        elif olimpia[i]["helyezes"] == 3:
            olimpiaipontok += 4
        elif olimpia[i]["helyezes"] == 4:
            olimpiaipontok += 3
        elif olimpia[i]["helyezes"] == 5:
            olimpiaipontok += 2
        else:
            olimpiaipontok += 1
    return olimpiaipontok

def tornamennyi(olimpia):
    torna = 0
    for i in range(len(olimpia)):
        if olimpia[i]["sportnev"] == "torna":
            if olimpia[i]["helyezes"] == 1 or olimpia[i]["helyezes"] == 2 or olimpia[i]["helyezes"] == 3:
                torna += 1
    return torna

def uszasmennyi(olimpia):
    uszas = 0
    for i in range(len(olimpia)):
        if olimpia[i]["sportnev"] == "uszas":
            if olimpia[i]["helyezes"] == 1 or olimpia[i]["helyezes"] == 2 or olimpia[i]["helyezes"] == 3:
                uszas += 1
    return uszas

def ermekszamanagyobb(tornamennyi,uszasmennyi):
    tornanagyobb = tornamennyi
    uszasnagyobb = uszasmennyi
    if tornanagyobb > uszasnagyobb:
        print("Torna sportágban szereztek több érmet")
    elif uszasnagyobb > tornanagyobb:
        print("Úszás sportágban szereztek több érmet")
    else:
        print("Egyenlő volt az érmek száma")
 
def sportolokszama(olimpia):
    mennyisportolo = 0
    for i in range(len(olimpia)):
        if olimpia[i]["sportolokszama"] > mennyisportolo:
            mennyisportolo = olimpia[i]["sportolokszama"]
    for i in range(len(olimpia)):
        if olimpia[i]["sportolokszama"] == mennyisportolo:
            print("Helyezés:",olimpia[i]["helyezes"])
            print("Sportág:",olimpia[i]["sportnev"])
            print("Versenyszám:",olimpia[i]["versenyszamnev"])
            print("Sportolók száma:",mennyisportolo)




beolvas = beolvasas()
print(beolvas)
print("3. feladat")
mennyihelyezes = hanyhelyezes(beolvas)
print("Pontszerző helyezések száma:",mennyihelyezes)
print("4. feladat")
mennyiarany = arany(beolvas)
print("Arany:",mennyiarany)
mennyiezust = ezust(beolvas)
print("Ezüst:",mennyiezust)
mennyibronz = bronz(beolvas)
print("Bronz:",mennyibronz)
osszeserem = osszerem(mennyiarany,mennyiezust,mennyibronz,beolvas)
print("összesen:",osszeserem)
print("5, feladat")
pontossz = pontokosszege(beolvas)
print("Olimpiai pontok száma: ",pontossz)
print("6. feladat")
uszas = uszasmennyi(beolvas)
torna = tornamennyi(beolvas)
melyikanagyobb = ermekszamanagyobb(torna,uszas)
print("7. feladat")
hanysportolo = sportolokszama(beolvas)