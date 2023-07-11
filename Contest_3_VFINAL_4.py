##Anirudh Venkat
##Grade 8
##Clague Middle School
lines=[]
with open("input.txt") as f:
    for line in f:
        n=line
        n=n.split()
        n=list(n[0])        #Turning into lists and getting rid of the /n
        p2=[]
        p3=[]
        p4=[]
        p6=[]
        p7=[]
        for i in range(0,len(n)):
            if n[i].isalpha():
                n[i]=n[i].upper()       #Making everything uppercase
                
        def AND(a):         #function to combine the nots and letters, and add & symbols
            le=len(a)
            for i in range(0,le-1):
                try:
                    k=a[i]
                    j=a[i+1]
                    if (k.isalpha() and j.isalpha()) or (k.isalpha() and j=='~'):
                        a.insert(i+1,'&')
                        AND(a)
                except:
                    pass
            for i in range(0,le-1):
                try:
                    if a[i]=='~' and a[i+1].isalpha():
                        a.insert(i,a[i+1]+'Z')          #So all of them are alpha
                        del a[i+1]
                        del a[i+1]
                except:
                    pass

        AND(n)
        
        p1=['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
        def Veitch(a):
            A1=['0','1','4','5','8','9','12','13']
            A2=['2','3','6','7','10','11','14','15']
            B1=['0','1','2','3','4','5','6','7']
            B2=['8','9','10','11','12','13','14','15']
            C1=['1','2','5','6','9','10','13','14']
            C2=['0','3','4','7','8','11','12','15']
            D1=['4','5','6','7','8','9','10','11']
            D2=['0','1','2','3','12','13','14','15']        #These are lists for all the values in each column
            legt=len(a)
            while legt>0:
                legt=len(a)
                try:
                    Indiana=a.index('+')
                except:
                    Indiana=len(a)
                
                    
                for i in range(0,Indiana):
                    if a[i].isalpha():                      #Adding all the alphabets to a lists that are in the same variables
                        p2.append(a[i])

                for i in p2:
                    p7.append(i)
                p2.clear()
                for i in p7:
                    if i not in p2:
                        p2.append(i)

                
                p4.append(p2[0:Indiana])
                for mike in range(1,len(p4)):
                    p5=[]
                    for pike in p4[mike]:
                        if len(pike)==1:
                            p5.append(pike+'Z')
                        if len(pike)==2:
                            pike=list(pike)
                            del pike[len(pike)-1]
                            pike=''.join(pike)
                            p5.append(pike)
                        p5.append(''.join(p5))
                    del p5[0:len(p5)-1]
                    p6.append(p5[len(p5)-1])
                    
                for i in range(0,len(p2)):
                    if p2[i] in p6:
                        del p2[i]
                        del p2[p2.index(p6[p2[i]])]
                        
                        
                    
                        
                for o,s in enumerate(p2):               #Changing all the letters to their respective lists
                    if s=='A':
                        p2[o]=A1
                    elif s=='AZ':
                        p2[o]=A2
                    elif s=='B':
                        p2[o]=B1
                    elif s=='BZ':
                        p2[o]=B2
                    elif s=='C':
                        p2[o]=C1
                    elif s=='CZ':
                        p2[o]=C2
                    elif s=='D':
                        p2[o]=D1
                    elif s=='DZ':
                        p2[o]=D2
                    
                for m in p2[0]:                             #To find all the common terms in all the lists in p2
                    cool=0
                    legth=len(p2)
                    for ske in p2:
                        if m in ske:
                            cool=cool+1
                    if cool==legth:
                        p3.append(m)
            
                    for i in p3:                            #Changing the zeros to ones in p1 in the positions that were the common terms
                        p1[int(i)]='1'
                    p3.clear()                              #Clearing both lists so it doesnt interfere in while loop
                p2.clear()
                p7.clear()
                try:
                    del a[0:a.index('+')+1]                 #Deleting 'a' up the next + sign, so while loop will eventually end
                except:
                    del a[0:len(a)]
                legt=len(a)
            
                
                
                
        Veitch(n)
        strg=''
        for i in p1:
            strg=strg+str(i)
        hexo=hex(int(strg,2))                               #Converting the 'binary expression' to hexadecimal
        hexi=list(hexo)
        del hexi[0]
        del hexi[0]
        hexo=''.join(hexi)
        if len(hexo)!=4:
            strg_zeros='0'*(4-(len(hexo)%4))                        #Add extra zeros
            hexi=list(strg_zeros+hexo)
        for i in range(0,len(hexi)):
            if hexi[i].isalpha():
                hexi[i]=hexi[i].upper()                     #Make all the lower cases upper case
        print(hexi)
                       
                
        
        
        
                        
                        
                        
                            
                            
                        
                               

