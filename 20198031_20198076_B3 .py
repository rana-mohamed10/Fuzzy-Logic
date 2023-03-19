"""
names : Mahmoud Emad Ibrahim - 20198076   Group : B3
        Rana Mohamed    - 20198031      
        
        
"""

def fuzzification(xcord,Type,crisp):
    myset=[]
    ycord=[]
    member=0
    #print(len(xcord))
    for i in range(len(xcord)):
        xcord[i]=int(xcord[i])
    if (Type=="TRI"):
        ycord=[0,1,0]
        if len(xcord)!=3:
            print("Please enter 3 coordinates")
        else:

                myset.append(xcord)
                myset.append(ycord)


    elif(Type=="TRAP"):
        ycord=[0,1,1,0]
        if len(xcord)!=4:
            print("Please enter 4 coordinates")
        else:
             myset.append(xcord)
             myset.append(ycord)

    for i in range(len(xcord)):
        #print(myset)

        for j in range(len(ycord)-1):
            #print(myset[i][j], myset[i + 1][j])
            dy=(myset[i+1][j+1]-myset[i+1][j])
            dx=(myset[i][j+1]-myset[i][j])
            #print(dy)
            if (dx==0 ):
                continue
            elif (dy==0):
                continue
            else:
                #print(dx,dy)
                m = dy / dx
            c=myset[i+1][j]-(myset[i][j]*m)

            #print(y)
            #print(c)

            y = m * crisp + c
            #print(y)

            if crisp<xcord[0] or crisp>xcord[-1]:
                member=0
            elif crisp>xcord[j] and crisp<xcord[j+1]:
                member=y

            else:
                pass

        print(member)

        break

    return member

#allmem=[[0, 0.3,0.5], [0.5, 0.3333333333333335,0.6], [0.3,0.5, 0], [0.5, 0], [0, 0.33333333333333326]]
#operator=[['or',"and"], ['and','and_not'], ['and','or'], ['and'], ['and_not']]
def Inference (operator,allmem):
    value=[]
    for i in range(len(operator)):
        for j in range(len(operator[i])):
            if (operator[i][j]=="and"):
                r=min(allmem[i][j],allmem[i][j+1])
            elif (operator[i][j]=="or"):
                r=max(allmem[i][j],allmem[i][j+1])
            elif (operator[i][j]=="and_not"):
                inv=1-allmem[i][j+1]
                r=min(allmem[i][j],inv)
            else:
                inv=1-allmem[i][j+1]
                r=max(allmem[i][j],inv)
            allmem[i][j+1]=r
        value.append(allmem[i][-1])
    #print(value)    
    return value 
#outval=[['low', ['0', '25', '50']], ['normal', ['25', '50', '75']], ['high', ['50', '100', '100']]]
#inf=[0.33333333333333326, 0.3333333333333335, 0, 0, 0]
#outset=['low', 'normal', 'normal', 'high', 'high']
def Defuzzification(outval,inf,outset,out):
    cent=[]                           
    Zsum=0                         
    Rsum=0                         
    for j in outval:
        sum1=0
        for i in j[1]:
            i=int(i)
            sum1=sum1+i           
        cent.append([j[0],sum1/len(j[1])])   
   # print(cent)
    for i in range(len(inf)):
      
      for j in cent:
          if outset[i]==j[0]: 
              Zsum+= inf[i]*j[1]       
              Rsum+= inf[i]
              #print(Zsum)
              #print(j[1])
    z=Zsum/Rsum
    z=round(z, 2)  #37.5
    Min=9999999
    setsList=[]
    for i in outval:
        if z>int(i[1][0]) and z<int(i[1][-1]):
            x=fuzzification(i[1], outset, z)
            setsList.append([x,i[0]])
    #print(setsList)        
    for i in setsList:        #[['l', 25.0], ['n', 50.0], ['h', 83.33333333333333]]
        if i[0]<=Min:            #[[0.5, 'l'], [0.5, 'n']]
            Min=i[0]
            Set=i[1]
            #print(Min)
            #print(Set)
            
            
    print("The predicted" , out, "is",Set,z)

    #return z
#outtype="TRI"
#Defuzzification(outval,inf,outset,"risk" )
#preMenu
def intro():
    print("Fuzzy Logic ToolBox", "\n===================")
    print("1-Create a new fuzzy system", "\n2- Quit")

def mainMenu():
    print("Main Menu:", "\n========", "\n1- Add variable.", "\n2- Add fuzzy sets to an existing variables.", "\n3- Add rules.", "\n4- Add simulation on crisp sets.")

def number1():
    print("Enter the variable’s name, type (IN/OUT) and range ([lower, upper]): (Press x to finish)", "\n----------------------------------------------------------------------------------------")

def number2p1():
    print("Enter variable's name\n")

def number2p2():
    print("\nEnter the fuzzy set name, type (TRI/TRAP) and values: (Press x to finish)", "\n-----------------------------------------------------")

def number3():
    print("Enter the rules in this format: (Press x to finish)\nIN_variable set operator IN_variable set => OUT_variable set", "\n------------------------------------------------------------")

def number4():
    print("Enter the crisp values:", "\n-----------------------")

Errormsg = "CAN’T START THE SIMULATION! Please add the fuzzy sets and rules first."
varsList = list() # user's input of var name, range and type
varsList2 = list() # user's input of var name, range and type
varsList3 = list()  # user's input of var name, range and type
outList=list()
varList4=list()
operators=list()
outset=list()


Tool={}
#Menu
intro()#Intro message
#An input variable for intro menu

while True:
    intronum = int(input())
    if intronum == 1:
        print("Enter the system's name and a brief description:", "\n------------------------------------------------")
        Name = input()
        desc = input()
        while True:
            mainMenu()  # To print Main Menu
            menuNum = int(input())  # take a var from user
            if menuNum == 1:
                number1()  # Print number 1 option's message
                  
                while True:  # Suggsetion : you take vars in list then assign every single index to a variable and split them then by the space then use them
                    var = input()
                    if var == "x" or var == "X":  # If condition for "X" option
                        break
                    else:
                        w=var.split(" ")
                        if w[1]=="IN":
                            varsList.append(w[0])                       
                            Tool[w[0]]={"type":w[1],"Range":w[2:],"fuzzy":[]}
                        elif w[1]=="OUT":
                            outList=[w[0]]
                        else:
                            print("please enter a valid variable type ",'\n')
                        #print(Tool)
            
            elif menuNum == 2:
               outval=[]
               while True:
                    number2p1()  # number2 part1 msg
                    varname = input()
                    if varname not in varsList and varname not in outList :
                        print("Please choose existing variable name",'\n')
                    elif varname in varsList:
                        number2p2()                    
                        while True:
                            var2 = input()                           
                            w1=var2.split(" ")                        
                            if var2 == "x" or var2 == "X":  # If condition for "X" option
                                break
                            else:
                                Tool[varname]["fuzzy"].append({w1[0]:{"type":w1[1],"values":w1[2:]}})
                                #print(Fuzzy["name"])
                                varsList2.append(var2)
                        break
                    else:
                        number2p2()
                        while True:
                            var2 = input()                           
                            w1=var2.split(" ")
                            if var2 == "x" or var2 == "X":  # If condition for "X" option
                                break
                            else:
                                outval.append([w1[0],w1[2:]])
                                outtype=[w1[1]]
                                print(outtype)
                        #print(Tool)
                        filter
                        break  
            elif menuNum == 3:
                number3()
                           
                while True:
                    varsList3=[]
                    op=[]
                    var3 = input()
                    w2=var3.split(" ")
                    
                    if var3 == "x" or var3 == "X":  # If condition for "X" option
                        break
                    else:
                        outset.append(w2[-1])
                        for i in varsList:
                            op=[]
                            for j in range(len(w2)):
                                
                                if w2[j-1]=="not" and i==w2[j] :
                                    a=["not",w2[j],w2[j+1]]
                                    varsList3.append(a)
                                elif i==w2[j]:
                                    a=[w2[j],w2[j+1]]    
                                    varsList3.append(a)
                                elif w2[j]=="or" or w2[j]=="and" or w2[j]=="or_not" or w2[j]=="and_not":
                                    op.append(w2[j])
                    varList4.append(varsList3) 
                    operators.append(op)
                    #print(operators)
                        
            elif menuNum == 4:
                try:
                   
                   if len(varsList2)>0 and len(varList4)>0:
                       number4()
                       members={}
                       for i in varsList:
                           #print(varsList)
                           print(i)
                           crisp=input()
                           crisp=int(crisp)
                           members.update({i:[]})                                           
                           for j in range(len(Tool[i]["fuzzy"])):
                               for k in Tool[i]["fuzzy"][j].keys():
                                
                                   xcord=Tool[i]["fuzzy"][j][k]["values"]
                                   #print(j)
                               
                                   Type=Tool[i]["fuzzy"][j][k]["type"]
                                   member=fuzzification(xcord, Type, crisp) 
                                   
                                   members[i].append({k:member})
                       print("Running the simulation…",'\n')
                       print("Fuzzification => done")
                   #print(members)
                   allmem=[]
                   for i in varList4:
                       memval=[]
                       for j in i:
                           if j[0]=="not":
                               for k in members[j[1]]:
                                   a=str(k.keys())
                                   #print(j.keys())
                                   b= len(j[2])
                                   if j[2]==a[12:12+b] :
                                      
                                       mem1=1-k[j[2]]
                                       memval.append(mem1)
                           else:
                             for k in members[j[0]]:
                                 a=str(k.keys())
                                 b= len(j[1])
                                 #print(j.keys())
                                 if j[1]==a[12:12+b] :
                                    
                                     mem1=k[j[1]]
                                     memval.append(mem1)
                       allmem.append(memval)
                   #print(allmem)
                   
                   d=varsList2[1]
                   d=varList4[1]
                   inf=Inference(operators, allmem)
                   #print(inf)
                   
                   print("Inference => done")
                   # print("Defuzzification => done",'\n')
                   Defuzzification(outval,inf,outset,outList[0])
                   print("Defuzzification => done",'\n')

                except:
                    print(Errormsg)
            elif menuNum == "Close" or menuNum == "close":
                break
            else:
                print("please enter a valid input")
    elif intronum == 2:
        break
    else:
        print("please enter a valid input")
                     

int