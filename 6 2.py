vvod=input()
d=vvod.split()
s=[]
count=0
count1=0
for i in range (len(d)):
    x=d[i]

    for p in range (len(x)):
        s+=x[p]
        if 'а'==x[p] or 'А'==x[p]:
            count+=1
    print(x,count/len(x)*100,"% буквы а") 
    count=0

    for p in range (len(x)):
        s+=x[p]
        if 'б'==x[p] or 'Б'==x[p]:
            count1+=1
    print(x,count1/len(x)*100,"% буквы б") 
    count1=0
