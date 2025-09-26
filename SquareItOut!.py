Lis = [12.33,12312.2,3132,31,2,0.078]
odd = []
even = []
A = []
def square_it_out(L):
    print("The maximum number in the list is:", max(L))
    for i in L:
        A.append(i**2)
    print("The square of each number in the list is:", A)
    for i in range(len(L)):
        if i % 2 == 0:
            even.append(L[i])
        else:
            odd.append(L[i])
    print("The numbers with odd index are:", odd)
    print("The numbers with even index are:", even)


square_it_out(Lis)