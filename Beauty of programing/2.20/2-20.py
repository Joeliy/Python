def Main():
    fp = open("result.txt","w")
    rg = range(2,32)
    i = 1
    while(i<18446744073709551616):
        hit = 0
        hit1 = -1
        hit2 = -1
        j=0
        while((j < len(rg)) and (hit<=2)):
            if i % rg[j] != 0:
                hit += 1
                if hit == 1:
                    hit1 == j
                elif hit ==2:
                    hit2 == j
                else:
                    break
            j += 1
        if (hit == 2) and (hit1 +1 == hit2):
            print>>fp,"found{0}",i
        i += 1

    fp.flush()
    fp.close()

if __name__ =='__main__':
    Main()
