import sys

filename="puzzles.txt"
fp = open(filename, 'rb')
n=2
m=0
list=[]
result=[]
row=0
for i, line in enumerate(fp):
    if i==n:
        for j in range(0,4):
            if line[1+3*j]=='1':
                elem = int(line[2 + 3 * j])+10
            elif line[2 + 3 * j]!=' ':
                elem = int(line[2 + 3 * j])
            if line[2 + 3 * j]==' ':
                row=4-m
                print("**",row)
            else:list.append(elem)
        m+=1
        if(m==4):
            print(list)
            count=0
            for a in range (15):
                for b in range(a,15):
                    if list[a]>list[b]:
                        count+=1
            print(count)
            print(row)
            result.append((count+row)%2)
            list = []
            n+=5
            m=0
        else:n=n+2

print(result)
flag = ' '
for i in range(128):
    if result[i]==0:
        flag = '1' + flag
    else:
        flag = '0' + flag
print('SharifCTF{%016x}' % int(flag, 2))