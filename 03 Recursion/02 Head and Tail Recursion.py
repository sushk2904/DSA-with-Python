#Head Recursion

#Tail Recursion


# 1 to N Recursion 
#a) Head
def Head_1toN_func(i, N):
    if i > N:
        return
    print(i)
    Head_1toN_func(i+1, N)
Head_1toN_func(1,4)

#b) Tail
def Tail_1toN_func(N):
    if N==0:
        return
    Tail_1toN_func(N-1)
    print(N)
Tail_1toN_func(4)


#N to 1 Recursion
#a) Head
def Nto1_Head_func(N):
    if N == 0:
        return
    print(N)
    Nto1_Head_func(N-1)
Nto1_Head_func(4)

#b) Tail
def Nto1_Tail_func(i, N):
    if i>N:
        return
    Nto1_Tail_func(i+1, N)
    print(i)
Nto1_Tail_func(1,4)
