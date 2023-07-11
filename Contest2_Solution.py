##Anirudh Venkat
##Grade 8
##Clague Middle School
lines=[]
with open("input.txt") as f:
    for line in f:
        n=line
        m=n.split()             #Splitting each line into lists
        Yarn1=list(m[0])
        Yarn2=list(m[1])
        p1=[]
        p2=[]
        p3=[]
        p4=[]
        def lower(a,b):         #Function to find the list with the lower amount of character
            if len(Yarn1)>=len(Yarn2):
                p1.append(len(Yarn2))
                p4.append(len(Yarn1))
            else:
                p1.append(len(Yarn1))
                p4.append(len(Yarn2))
        lower(Yarn1,Yarn2)
        def direct(a,b):        #Function to cancel out the like terms in like places
            dude=0
            LA=p1[len(p1)-1]
            for i in range(0,LA):
                try:            #Try here because it will give an error at the end
                    if a[i]==b[i]:
                        del a[i]        #Deletes the element from both lists at that specific function
                        del b[i]
                        dude=1
                        break
                except:
                    pass
            if dude==1:    
                direct(a,b)         #Use recursive to avoid error of changing the length of the for loop to be longer than that of the strings
                
        def Side(a,b):          #Function to cancel out the terms that satisfies the third step
            k=0
            while k==0:
                k=1
                LAM=p1[len(p1)-1]
                for i in range(0,LAM):
                    try:        #Try here because it will cause error at the end
                        direct(a,b)
                        if Yarn1[i]==Yarn2[i+1] and Yarn2[i]==Yarn1[i+1]:
                            direct(a,b)
                            del Yarn1[i]
                            del Yarn2[i+1]
                            del Yarn2[i]
                            k=2
                            break
                        direct(a,b) #Since this direct step always comes first, the more times its repeated here, the safer
                        
                        if Yarn1[i]==Yarn2[i+1] and Yarn2[i]!=Yarn1[i+1]:
                            direct(a,b)
                            del Yarn1[i]
                            del Yarn2[i+1]
                            del Yarn2[i]
                            k=2
                            break
                        direct(a,b)
                        
                        if Yarn2[i]==Yarn1[i+1] and Yarn1[i]!=Yarn2[i+1]:
                            direct(a,b)
                            del Yarn1[i+1]
                            del Yarn2[i]
                            del Yarn1[i]
                            k=2
                            break
                    except:
                        pass
                    direct(a,b)
                if k==2:
                    k=0
            
        def AlphaCon(a,b):          #Function to convert Alphabets into numbers
            tune=0
            good=0
            instrument=0
            skw=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
            for p,i in enumerate(a):
                if i in skw:
                    idk=skw.index(i)+1
                    try:
                        a[p]=idk
                    except:
                        a.append(idk)
            for p,i in enumerate(b):
                if i in skw:
                    lol=skw.index(i)+1
                    try:
                        b[p]=lol
                    except:
                        b.append(lol)
            lower(a,b)
            ok=p1[len(p1)-1]
            for i in range(0,ok):
                tune=tune+a[i]-b[i]             
                instrument=p4[len(p4)-1]-p1[len(p1)-1]
                good=tune+instrument       #adding the numbers together
            print(good)
 
        direct(Yarn1,Yarn2)         #Calling all of the functions
        Side(Yarn1,Yarn2)
        AlphaCon(Yarn1,Yarn2)

        
