def strzalka(skala=1,powiel=1):
    druk=''
    druk="**"*2*skala+"*"*skala
    podstawa=len(druk)
    druk=("  "*skala + druk + "  "*skala)*powiel
    ilosc=skala*2
    while (ilosc>0):
        druk=("  "*skala + "*" + " "*(podstawa-2) + "*" + "  "*skala)*powiel + "\n" + druk
        ilosc-=1
        #ilosc=ilosc-1
    tmp=("**"*skala + "*" + " "*(podstawa-2) + "*" + "**"*skala)*powiel
    podstawa=len(tmp)-2
    druk=tmp + "\n" + druk
    ilosc=1
    while(podstawa-(ilosc*2)>0):
        druk=" "*ilosc + "*" + " "*(podstawa-(ilosc*2)) + "*" + "\n" + druk
        ilosc+=1
    druk=" "*ilosc+("**" if skala%2==0 else "*") + "\n" + druk
    """
    tmp=" "*ilosc
    if (skala%2==0):
        tmp+="**"
    else:
        tmp+="*"
    druk=tmp+"\n"+druk
    
    """
    
    return druk 
   
print(strzalka(powiel=2))


