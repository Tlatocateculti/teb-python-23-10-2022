def strzalka(skala=1,powiel=1,dol=False):
    druk=''
    druk="**"*2*skala+"*"*skala
    podstawa=len(druk)
    druk=("  "*skala + druk + "  "*skala)*powiel+"\n"
    ilosc=skala*2
    while (ilosc>0):
        tmp=("  "*skala + "*" + " "*(podstawa-2) + "*" + "  "*skala)*powiel+"\n"
        druk= druk+tmp if dol else tmp+druk
        """
        if dol==True:
            druk=druk+tmp
        else:
            druk=tmp+druk
        """
        ilosc-=1
    tmp="**"*skala + "*" + " "*(podstawa-2) + "*" + "**"*skala
    podstawa=len(tmp)-2
    tmp=tmp*powiel + "\n"
    druk= druk+tmp if dol else tmp+druk
    ilosc=1
    while(podstawa-(ilosc*2)>0):
        tmp=(" "*ilosc + "*" + " "*(podstawa-(ilosc*2)) + "*" + " "*ilosc)*powiel + "\n"
        druk= druk+tmp if dol else tmp+druk
        ilosc+=1
    tmp=(" "*ilosc+("**" if skala%2==0 else "*")+" "*ilosc)*powiel + "\n"
    druk= druk+tmp if dol else tmp+druk
    """
    tmp=" "*ilosc
    if (skala%2==0):
        tmp+="**"
    else:
        tmp+="*"
    druk=tmp+"\n"+druk
    
    """
    
    return druk 
   
print(strzalka(skala=2,powiel=2,dol=True))
print(strzalka(powiel=4))
print(strzalka(skala=3,dol=True))




