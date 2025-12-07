l=input("Enter the Sentence: ").split()
s=""
for i in l:
    main=i
    symbol=""
    for j in range(len(i)-1,0,-1):
        if(not i[j].isalnum()):
            symbol=i[j:]
            main=i[:j]
        else:
            break
    if len(main)>2:
        main=main[0]+str(len(main)-2)+main[-1]
    s+=main+symbol+" "
print(s.rstrip())
