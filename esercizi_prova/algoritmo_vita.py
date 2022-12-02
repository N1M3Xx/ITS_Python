def primo():
    n_b=0
    anno=0

    while((anno<5) and (n_b<3)):
        print("\n", anno+1, "° anno delle superiori")
        r=input("\nSei stato bocciato? ")
        if(r=="si"):
            n_b+=1
        else:
            anno+=1

    print("\nInizia il Lavoro")
    
def secondo():
    n_p=0

    for x in range(30):
        r=input("\nTi sei infortunato? ")
        if(r=="no"):
            print("\nallora lavori e tasi")
            r=input("\nPromozione? ")
            if(r=="si"):
                n_p+=1
            if(n_p==3):
                break
        else:
            break
    

print("Nasce la persona")
print("\nLa persona segue elementari e medie")
primo()
print("\nPENSIONE!!!!!!!!!!!")