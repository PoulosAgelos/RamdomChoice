import random

men=int(input("INPUT MEN:"))
women=int(input("INPUT WOMEN:"))
giroi=int(input("INPUT GIROI:"))

telika_zeugaria=[],[]

def choice(SmallList,BigList):
    pinakas=[]
    TM=False
    if ((len(SmallList)+len(BigList))%2)==1:
        TM=True
    for i in range(len(SmallList)):
        s=random.choice(SmallList)
        b=random.choice(BigList)
        SmallList.remove(s)
        BigList.remove(b)
        pinakas.append([s, b])

    for i in range(len(BigList)):
        try:
            b1 = random.choice(BigList)
            BigList.remove(b1)
            b2 = random.choice(BigList)
            BigList.remove(b2)
            pinakas.append([b1, b2])
        except:
            if TM:
                print("\n-----------------------------------------------")
                print("The player: '", b1, "' has not teamate.")
            break
        i=+2
    #print("the player with number:",BigList,"has not teamate.")

    return pinakas

def createlist(number):
    lista=[]
    for i in range(number):
        lista.append(i + 1)
    return lista

def printPinaka(pinakas,mnumber,wnumber):
    if(mnumber>wnumber):
        for i in range(0,len(pinakas),2):
            if (i==women//2 +1):
                try:
                    print("[WOMEN",pinakas[i],"ANDRA] VS [ANDRA",pinakas[i+1],"ANDRA]")
                except:
                    print("[WOMEN", pinakas[i], "ANDRA]PERISYEI")
            elif i <= women//2:
                print("[WOMEN",pinakas[i],"ANDRA] VS [WOMEN",pinakas[i+1],"ANDRA]")
            else:
                try:
                    print("[ANDRA  ",pinakas[i],"ANDRA] VS [  ANDRA",pinakas[i+1],"ANDRA]")
                except:
                    if(mnumber>wnumber+1):
                        print("[ANDRA  ", pinakas[i], "ANDRA] WITHOUT OPPENENT")
                    else:
                        print("[WOMEN",pinakas[i],"ANDRA] WITHOUT OPPENENT")
    elif mnumber==wnumber:
        for i in range(0, len(pinakas), 2):
            try:
                print("[WOMEN", pinakas[i], "ANDRA] VS [WOMEN", pinakas[i + 1], "ANDRA]")
            except:
                print("[WOMEN", pinakas[i], "ANDRA] WITHOUT OPPENENT")
    else:
        for i in range(0,len(pinakas),2):
            if (i==men//2 +1):
                try:
                    print("[MEN",pinakas[i],"WOMEN] VS [WOMEN",pinakas[i+1],"WOMEN]")
                except:
                    print("[MEN", pinakas[i], "WOMEN] WITHOUT OPPENENT")
            elif i <= men//2:
                print("[MEN",pinakas[i],"WOMEN] VS [MEN",pinakas[i+1],"WOMEN]")
            else:
                try:
                    print("[WOMEN",pinakas[i],"WOMEN] VS [WOMEN",pinakas[i+1],"WOMEN]")
                except:
                    if wnumber>mnumber+1:
                        print("[WOMEN", pinakas[i], "WOMEN] WITHOUT OPPENENT")
                    else:
                        print("[MEN",pinakas[i],"WOMEN] WITHOUT OPPENENT")


for i in range(giroi):
    womenlist = createlist(women)
    menlist = createlist(men)
    if (women <= men):
        print("MEN POOL")
        telikos_pinakas = choice(womenlist,menlist)
    else:
        print("WOMEN POOL")
        telikos_pinakas = choice(menlist,womenlist)
    print("\nRound:", i + 1)
    printPinaka(telikos_pinakas,men,women)
    print("-----------------------------------------------")







