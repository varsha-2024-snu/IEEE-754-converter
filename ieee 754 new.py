from decimal import Decimal
num=Decimal(input("enter a number to convert into ieee 754 format:"))

def binary(num):             #converting decimal to binary function
    a=abs(int(num))
    b=abs(num)-a
    list1=[]
    list2=[]
    while True:
        if a==1 or a==0:
            list1.append(a)
            break
        else:
            list1.append(a%2)
            a=a//2
    for i in range(15):
        if b==1:
            list2.append(b)
            break
        else:
            b=b*2
            list2.append(int(b))
            b=b-int(b)
    
    list1=list1[::-1]
    c=""
    for j in list1:
        c+=str(j)
    d=""
    for k in list2:
        d+=str(k)
    binary_form=c+"."+d
    binary_form=Decimal(binary_form)
    return(binary_form)

if num==0.0:                    #special case zero for both double and single
    print("spl case zero")
else:
    binnum=binary(num)      #binary function call
    print("binary form:",binnum)
    a=str(binnum)
    a=list(a)
    point=None
    newpoint=None
    for i in range(0,len(a)):
        if a[i]==".":
            point=i
    if point is not None:
        a.pop(point)
    for l in range(0,len(a)):
        if a[l]=="1":
            newpoint=l
            break
            
    newlist=[]
    newlist=newlist+list(a[0:newpoint+1])+["."]+list(a[newpoint+1:len(a)])
    norm=""
    for i in newlist:
        norm+=i
    print("normalised form:",norm,"x 2^",str(point-newpoint-1))
    print("\n")
    print("===================================================================")

    #IEEE 754 single precision
    sing_exp=127+(point-newpoint-1)
    sing_mant=""
    for i in newlist[newpoint+2:len(newlist)]:
        sing_mant+=i
    zeros="0"*(23-len(sing_mant))
    sing_mant=sing_mant+zeros
    sign=0
    if num<0:
        sign=1
    if sing_exp>=255 and sing_mant==0 and sign==0:
        print("spl case positive infinity")
    if sing_exp>=255 and sing_mant==0 and sign==1:
        print("spl case neg infinity")
    if sing_exp==0 and sing_mant!=0 and sign==0:
        print("spl case positive denormalised")
    if sing_exp==0 and sing_mant!=0 and sign==1:
        print("spl case negative denormalised")
    if sing_exp>=255 and sing_mant!=0:
        print("spl case nan")
    else:
        if len(str(int(binary(sing_exp))))<8:
               sing_exp="0"+str(int(binary(sing_exp)))
        else:
            sing_exp=str(int(binary(sing_exp)))
        print("The IEEE 754 Single precision format:")
        print(sign, "   ", sing_exp,"   ",sing_mant)   
        print("Sign:",sign,"\nexponent:",sing_exp,"\nmantissa:",sing_mant)
        print("\n")
        print("====================================================================")

#IEEE 754 double precision
    doub_exp=1023+(point-newpoint-1)
    doub_mant=""
    for i in newlist[newpoint+2:len(newlist)]:
        doub_mant+=i
    zeros="0"*(52-len(doub_mant))
    doub_mant=doub_mant+zeros
    if doub_exp>=2047 and doub_mant==0 and sign==0:
        print("spl case positive infinity")
    if doub_exp>=2047 and doub_mant==0 and sign==1:
        print("spl case neg infinity")
    if doub_exp==0 and doub_mant!=0 and sign==0:
        print("spl case positive denormalised")
    if doub_exp==0 and doub_mant!=0 and sign==1:
         print("spl case negative denormalised")
    if doub_exp>=2047 and doub_mant!=0:
        print("spl case nan")
    else:
        doub_exp="0"+str(int(binary(doub_exp)))
        print("The IEEE 754 Double precision format:")
        print(sign,"   ",doub_exp,"   ",doub_mant)   
        print("Sign:",sign,"\nexponent:",doub_exp,"\nmantissa:",doub_mant)


    


                  

