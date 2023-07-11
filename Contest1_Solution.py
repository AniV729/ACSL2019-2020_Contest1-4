# Anirudh Venkat 8th Grade Clague Middle School, Ann Arbor, Michigan
#Nov 27, 2019
# ASCL Contest#1
lines=[]
with open("input.txt") as f:    #Opening file to read input line by line
    for line in f:
        m=line
        s=m.split()
        n=list(s[0])
        n=list(map(int,n))
        num=int(s[1])
        p1=[]                   # 2 separate lists for first and second terms, with first term being split into a list of itself 
        leth=len(n)
        lend=n[leth-num]
        for i in range(0,leth-num):     #Putting the sum (Units digit) for each number up to the given number and the given number into the list
            a=n[i]
            if len(str(a+lend))==1:
                p1.append(a+lend)
            else:
                k=a+lend
                lol=str(k)
                lil=int(lol[0])
                p1.append(k-(10*lil))

        p1.append(lend)                 #Putting number into the list


        for i in range(leth-num+1,leth):# Putting absolute value of the differences between all values after the given number and the given number into the list
            b=n[i]
            p1.append(abs(lend-b))

        gucci = ''.join(str(i) for i in p1)     # Turning list back into string
        gucci=int(gucci)                        # Turning string into integer
        print(gucci)                            #Printing output
            
        
        

        
        
        
