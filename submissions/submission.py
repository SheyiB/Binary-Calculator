import matplotlib.pyplot as pyplot
import copy
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
def adder(x,y,z):
    res = my_xor(my_xor(x,y), z)
    carry = my_or(my_and(x,y), my_and(my_xor(x,y), z))
    return [res, carry]

X = []
print('Enter First Binary Sequence')
for i in range(0,4):
    X.append(int(input('')))
initial_X = copy.deepcopy(X)

Y = []
print('Enter Second Binary Sequence')
for i in range(0,4):
    Y.append(int(input('')))
initial_Y = copy.deepcopy(Y)

for i in range(0,4):
    Y[i] = my_xor(1, Y[i])

carry = 1
S = [0, 0, 0, 0]
for i in range(3, -1, -1):
    [S[i], carry] = adder(X[i], Y[i], carry)

if(carry == 0):
    for i in range(0,4):
        S[i] = my_xor(1, S[i])

    carry = 1
    for i in range(3, -1, -1):
        [S[i], carry] = adder(S[i], 0, carry)

    print('-', S)

else:
    print('+', S)


print(initial_X)
print(initial_Y)
fig, axis = pyplot.subplots(3, sharex=True, sharey=True)
axis[0].stem(initial_X)
axis[1].stem(initial_Y)
axis[2].stem(S)

pyplot.show()