
ans ={}
temp =int(1)
def Binary_one(n,q):
    k =0
    for j in range(n,q):
        beq =[]
        temp =j
        while temp != 0:
            beq.append(temp%2)
            temp =temp //2
        for k in range(len(beq)-1):
            if beq[k] ==1 and beq[k+1] ==1:
                ans[j] ='True'
            else:
                ans[j] ='False'    
    print(ans)

x= int(input("Enter the start of the range: "))
y= int(input("Enter the end of the range: "))
Binary_one(x,y)