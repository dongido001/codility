#Binary Gap
#----------------------------
#coded by Onwuka Gideon
#www.fb.com/dongidomed
#dongidomed@gmail.com]
#08059794251
 
def solution(N):
    bi = bin(int(N))[2:]
 
    arr = [] #for holding the values of 0  
    counter = 0 #counts the nuber 0
    cont = 0 #just counts the string(binary) 1 by 1
    lent = len(bi) # lenght of the binary
   
    if str(0) not in bi:
        return 0
   
    else:
        for i in bi:
            cont = cont + 1
            if i == str(1):
                if counter > 0:
                    arr.append(counter)
                    if (i == str(1)):
                        counter = 0
            if i == str(0):
                counter = counter + 1
            if cont == lent and counter > 0:
                arr.append(counter)
    return max(arr)
