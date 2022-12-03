def primo():
    n_b=0
    anno=0

    print("\nLa persona segue elementari e medie")
    while((anno<5) and (n_b<3)):
        print("\n", anno+1, "° anno delle superiori")
        r=input("\nSei stato bocciato? ")
        if(r=="si"):
            n_b+=1
        else:
            anno+=1
    secondo()
    
def secondo():
    n_p=0

    print("\nInizia il Lavoro")
    for x in range(30):
        r=input("\nTi sei infortunato? ")
        if(r=="no"):
            n_p=terzo(n_p)
            if(n_p==3):
                print("\nSei diventato capo dell'azienda")
                break
        else:
            break
def terzo(n_p):
    print("\nallora lavori e tasi")
    r=input("\nPromozione? ")
    if(r=="si"):
        n_p+=1
    return n_p

print("Nasce la persona")
primo()
print("\nPENSIONE!!!!!!!!!!!")