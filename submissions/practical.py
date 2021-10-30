bin01 = input('Enter first binary \n -->')
bin02 = input('Enter second binary \n -->')



def compliment(ni):
    nie = str(ni)
    niw = len(nie)
    niq = 'p'
    for i in range(niw):
        if nie[i] == '1':
            niq = niq + '0'
        if nie[i] == '0':
            niq = niq + '1'
    niq = niq.strip('p')
   # niq = int(niq)   
    return niq 

#print(compliment('101111'))
#b1 = bin(bin01)
#b1 = b1.lstrip('-0b')
#print(b1)

#print(type(b1))
def calculator(x,y,carry):
    sume = int(x) + int(y)+ int(carry)
    if(sume == 1):
        carry = 0
    elif (sume > 1 and sume !=3):
        sume = 0
        carry = 1
    elif( sume ==3):
        sume = 1
        carry = 1
    
    return sume,carry

def adder(n,p,carry):

    ln = len(str(n))
    lp = len(str(p))
    res = [0,0,0,0]
    carry=0
    for i  in range(ln-1,-1,-1) :
        #print (str(n)[i])
        #res.append(int(calculator(str(n)[i],str(n)[i],carry)))
        nn = n[i]
        np = p[i]
        iop = calculator(int(nn),int(np),carry)
        print('%s + %s + %s = %s'%(nn,np,carry,iop[0]))
        res[i] = iop[0]
        carry = iop[1]
        
    n= 'p'
    for i in range(len(res)):
        n = n + str(res[i])
    n = n.strip('p')
    
    return n
            

#adder('1011','0011',0)
#print(calculator(1,1,1))
def bin_check(num):
    for i in str(num):
        if(int(i)>1):
            return False    
        

def bin_check02(num):
    if (bin_check(num) != False):
        return num
    else:
        num = int(num)
        num = bin(num)
        num = num.lstrip('-0b')
        num 
        return num
    

#print(bin_check02('9011')) 


print('''
             %s
         +   %s
         -----------
             %s
         -----------
       '''%(bin01,bin02,adder(bin01,bin02,0)))