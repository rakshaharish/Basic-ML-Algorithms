import csv
with open('lab1.csv','r') as f:
    read=csv.reader(f)
    data=[]
    print("given training example:")
    for row in read:
        print(row)
        if(row[-1]=="yes" or row[-1]=="Yes" or row[-1]=="YES"):
             data.append(row)
    print('---------------------------------')
    print("positive training example:")
    for dat in data:
        print(dat)
       
    length=len(data[0])-1
               
    h=['$']*(length)
    print('---------------------------------')
    val=1
    for x in data:
         print('instance',val,"is",h)
         for i in range(0,len(x)-1):
            if(h[i]=='?'):
                continue
            elif(h[i]=='$'):
                h[i]=x[i]
            elif(h[i]!=x[i]):
                h[i]='?'
         print('hypothesis',val,"is",h)
         print('---------------------------------')
         val=val+1
    print('most specific hypothesis',h)

