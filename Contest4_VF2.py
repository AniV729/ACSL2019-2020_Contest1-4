#Anirudh Venkat
#8th grade
#Clague middle
lines=[]
with open("input.txt") as f:
    for line in f:                      #Executing the code line by line
        n=line.split()
        n=list(map(int,n))              #Converting all the strings in the list to integers
        o_p=n[0:6]                      #Splitting n by the moves needed to be done and the player and opponent's initial values
        moves=n[7:]
        lowest_val=[]
        prime_check=[]
        square_check=[]
        angle_check=[]
        p1=[]
        p2=[]
        def lower(a):                   #Function to find lowest possible value in the given list.
            lowest_val.clear()          #Clears list each time
            acc_a=53
            for i in a:
                if i<acc_a:
                    acc_a=i
            lowest_val.append(acc_a)


        def prime(a):                   #Function to check if number is prime or not. If true, it appends 1. If false, it appends 0.
            prime_check.clear()         #Clears list each time before starting
            for i in range(2,a):
                if a%i==0:
                    prime_check.append(0)
                    return
            prime_check.append(1)


        def square(a):                  #Function to check if number is a perfect square or not. Follows similar procedure to above function
            square_check.clear()        #Clears list each time before starting
            if (a**(1/2))%1==0 and a>4:
                square_check.append(1)
            else:
                square_check.append(0)

        def angle(val,roll):            #Function to check if the piece moves at least 1 move horizontally and then 1 vertically
            angle_check.clear()         #Clears list each time
            tot=val+roll
            if val<27 and val>1:
                for i in range(val,tot+1):
                    if ((i-1)/5)%1==0 and tot>i+1:      #Between 1 and 27, this is formula to use
                        angle_check.append(1)
                        return
            if val>29:
                for i in range(val,tot+1):
                    if((i+1)/5)%1==0 and tot>i+1:       #Between 29 and 52, this is formula to use
                        angle_check.append(1)
                        return
            angle_check.append(0)


        def patolli(a):
            lower(a[3:])            #Finding lowest value of the players deck
            value=lowest_val[0]
            roll_num=moves[0]
            summ=value+roll_num
            pos1=a.index(value)
            if summ>52:
                del moves[0]
                return
            elif summ==52:
                if summ==52:        #This is just to be sure and is superfluous.
                    del o_p[pos1]
                    del moves[0]
                    return                
            elif summ in a:
                del moves[0]
                return
            prime(summ)
            square(summ)
            if prime_check[0]==1:       #What to do if the value is actually prime
                    if summ in a:
                        del moves[0]
                        return
                    else:
                        if summ+6<52:
                            prime_up=summ+6
                            prime_dup=summ+6
                        else:
                            o_p[pos1]=summ
                            del moves[0]
                            return
                            
                        for i in range(summ, prime_up+1):
                            if i in a:
                                prime_dup=i-1
                                break
                        o_p[pos1]=prime_dup
                        del moves[0]
                        return
                        
            elif square_check[0]==1:    #What to do if the value is actually a perfect sqr
                if summ in a:
                    del moves[0]
                    return
                else:
                    square_up=1
                    square_dup=1
                for i in range(square_up, summ+1):
                    if i==a[pos1]:
                        continue
                    if i in a:
                        square_dup=i+1
                o_p[pos1]=square_dup
                del moves[0]
                return

            else:
                angle(value,roll_num)   #What to do if it moves horizontally, then vertically
                if angle_check[0]==1:
                    for i in range(value+1,summ+1):
                        if i%roll_num==0:
                            if i in a:
                                del moves[0]
                                return
                            else:
                                del moves[0]
                                o_p[pos1]=i
                                return
                
                else:                   #What to do normally
                    o_p[pos1]=summ
                    del moves[0]
                    return
            
                    



        while len(moves)>0: ##Keep executing patolli till there are no moves left
            patolli(o_p)
            for i in range(0,len(o_p)): ##Insurance policy
                if o_p[i]==52:
                    del o_p[i]
            if len(o_p)==3:
                o_p.append('GAME OVER')     ##If all the values reach 52
                break

        p1=o_p[3:]
        if p1[0]=='GAME OVER':
            p1=''.join(str(i) for i in p1)  ##Coverting Game Over to a string
            print(p1)
        else:
            p1.sort()
            for i in range(0,len(p1)):
                p1[i]=str(p1[i])+' '
            p1=''.join(str(i) for i in p1)  ##Converting the numbers in order to a string
            print(p1)
            
                
                
                
            
        
        
            
            
                    
            
            
            
                
            
            
                
                
                
