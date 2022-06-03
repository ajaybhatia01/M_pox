
a=open("/home/ajay/primer_monkeypox/all_mer_counts_dumps.fa","r")
x=a.read()
a.close()

b=open("/home/ajay/primer_monkeypox/mpox_mer_counts_dumps.fa","r")
y=b.read()
b.close()

c=0
d=0
i=0
for i in y:        #counter for total seqences in y file
    if i == ">":
        d = d+1

l=0
for l in x:        #counter for total sequences in x file
    if l == ">":
        c = c+1
    
t_seq_y = d
t_seq_x = c

ini_y = 0
fin_y = 403 
ini_x = 0
fin_x = 403
j=0
k=0
all_code=''
for k in range(t_seq_y):
    flag=0
    curr_seq_y = y[ini_y:fin_y]   #selection for a seq in y file

    for j in range(t_seq_x):
        print(t_seq_x)
        print(j)
        if j==0:
            ini_x = 0
            fin_x = 403
        else:
            ini_x = fin_x+1
            fin_x = ini_x+403
        curr_seq_x = x[ini_x:fin_x]   #selection for a seq in x file
        if(curr_seq_y == curr_seq_x):  #comparing two sequences
            print('equal')
            flag=1
            break                 #stoping loop if equal find
    if flag==0:
        for code in curr_seq_y:
            all_code=all_code + code
    ini_y=fin_y+1
    fin_y=ini_y+403

with open("/home/ajay/py_test/remained.fa", 'a') as f:
    counter=0
    for code in all_code:
        if code == '>':
            if counter!=0:
                f.write('\n')
                f.write(code)
            elif counter == 0:
                counter=1
                f.write(code)
        else:
                f.write(code)
f.close()

file=open("/home/ajay/py_test/remained.fa", 'r')
f=file.read()
print(f)
