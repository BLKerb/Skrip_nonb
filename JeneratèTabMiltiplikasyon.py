nonb=0
rep='w'

while(rep=='w' or rep=='W'):
    while(nonb<1 or nonb>10):
        nonb=int(input("Antre yon nonb ki twouvel ant zewo ak onz: \n"))
    print("Men valè a: " + str(nonb))
    print("Tab miltiplikasyon ", nonb, "se: ")
    
    for i in range(1,11):
         print(i, " x ", nonb, " = ", i*nonb)
  
    rep=(input ("Ou ta renmen jenere yon lòt tab? \n tape W pou wi oswa N pou non: "))
    if(rep=='w' or rep=='W'):
         nonb=0
    else:
        print("Mèsi, orevwa")
