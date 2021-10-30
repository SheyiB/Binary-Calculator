import matplotlib.pyplot as pyplot

#this is the basic Xor calculator that determines the sum for 4 binary numbers
def calculator(x,y,u,z,carry):
    sume = int(x) + int(y)+int(u)+int(z)+ int(carry)
    if(sume == 1):
        carry = 0
    elif (sume > 1 and sume <3):
        sume = 0
        carry = 1
    elif( sume ==3):
        sume = 1
        carry = 1
    elif( sume >3):
        sume = 0
        carry = 0
    
    return sume,carry

#Takes in a value and an initial value-point: 'n' and starts inserting the value starting from the inital value point 'n'
#I used this to insert the result of the multiplication into a list and do a right-shift to the left 
def insata(lol,n):
    stands = ['0','0','0','0','0','0','0','0']
    for lo in lol:
        stands[n] = lo
        n = n+1
    ings = [str(stan) for stan in stands]
    n_ings = ''.join(ings)
    return n_ings

#this does the multiplication of the partial products, it take in the result of the right shifted products        
def mult_adder(n,o,p,q,carry):
    ln = len(str(n))
    res = [0,0,0,0,0,0,0,0]
    carry=0
    for i  in range(ln-1,-1,-1) :
        #print (str(n)[i])
        #res.append(int(calculator(str(n)[i],str(n)[i],carry)))
        nn = n[i]
        np = p[i]
        no = o[i]
        nq = q[i]
        iop = calculator(int(nn),int(no),int(np),int(nq),carry)
        #print('%s + %s + %s+ %s+ %s = %s'%(nn,np,carry,iop[0]))
        res[i] = iop[0]
        carry = iop[1]
        
    n= 'p'
    for i in range(len(res)):
        n = n + str(res[i])
    n = n.strip('p')
    
    return n
                        
#the main multiplier function: Take in 2 inputs and multiplies them. Then returns the products using the above functions
def mult(num1,num2):
    liop =[]
    n=4
    for i in range(3,-1,-1):
        nint = int(num2[i]) * int(num1)
        liop.append(insata(str(nint),n))
        n=n-1
    n = mult_adder(liop[0],liop[1],liop[2],liop[3],0)

    return n, liop[0],liop[1],liop[2],liop[3]



num1 = input('enter a number\n ->')
num2 = input('enter another number\n ->')

num1list = []
num2list = []

#this takes in an empty list and a set of values then inserts them into the list
def appe(lio=[],num=str):
    nume = int(num)
    for i in range(4):
        lio.append(int(num[i]))
    return lio

num1list = appe(num1list,num1)
num2list = appe(num2list,num2)


ans = mult(num1,num2)

finale = ans[0]

finList = []
finList = appe(finList,finale)


print('''
            %s
        x   %s
        -----------
           %s
           %s
           %s
           %s
          -----------
           %s
          -----------
        '''%(num1,num2,ans[1],ans[2],ans[3],ans[4],ans[0]))

fig, axis = pyplot.subplots(3, sharex=True, sharey=True)
axis[0].stem(num1list)
axis[1].stem(num2list)
axis[2].stem(finList)



pyplot.show()