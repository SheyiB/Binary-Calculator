 


# fb = (input('Enter First Binary Sequence'))

# sb = (input('Enter Second Binary Sequence'))

# for i,k in fb,sb:
#     print(i,k)

# # print('----AND OPERATION----')

# # fb = int(input('Enter First Binary Sequence'))

# # sb = int(input('Enter Second Binary Sequence'))

# # def my_and(fb,sb):
# #     if fb&sb == 1:
# #         return 1
# #     else:
# #         return 0
    

# #print(fb and sb)
# #print(my_and(fb,sb))



# # print('----XOR OPERATION----')

# # fb = int(input('Enter First Binary Sequence'))

# # sb = int(input('Enter Second Binary Sequence'))

# # def my_xor(fb,sb):
# #     if fb != sb:
# #         return 1
# #     else:
# #         return 0

# # print(my_xor(fb,sb))

# # print('----OR OPERATION----')

# # fb = int(input('Enter First Binary Sequence'))

# # sb = int(input('Enter Second Binary Sequence'))

# # def my_or(fb,sb):
# #     if fb|sb == 1:
# #         return(1)
# #     else:
# #         return(0) 
    
# # print(fb or sb) 
# # print(my_or(fb,sb))
print('----4 BIT BINARY ADDER----')

def my_and(fb,sb):
    if(( fb==1) and (sb == 1)):
        return 1
    else:
        return 0

def my_xor(fb,sb):
    if(fb!=sb):
        return 1
    else:
        return 0

def my_or(fb,sb):
    if((fb==0) and (sb==0)):
        return 0
    else:
        return 1

fb = []
print('Enter First Binary Sequence')
for i in range(0,4):
    fb.append(input(' '))

sb = []
print('Enter Second Binary Sequence')
for i in range(0,4):
    sb.append(input(' '))

rem = 0
Sum = [0,0,0,0]

for i in range(3, -1, -1):
    Sum[i] = my_xor(my_xor(fb[i], sb[i]), rem)
    rem = my_or(my_and(fb[i],sb[i]),my_and(my_xor(fb[i], sb[i]), rem))
                
                
print(' ',fb)
print('+')
print(' ',sb)
print('_______________')
print('The carry is ',rem, 'The Sum is',Sum)
    
    