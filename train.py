import os
import string
from textblob import TextBlob

dir = os.path.normpath('D:\\SemEval2010_task8_all_data\\SemEval2010_task8_training')
f = open(os.path.join(dir,'TRAIN_FILE.TXT'))
a = f.read()
a=a.split('\n\n')

def extract(i):
    temp=b[0].split()
    temp=temp[1:]
    temp = ' '.join(i for i in temp)
    sen = temp
    e1=sen[sen.index('<e1>')+4:b[0].index('</e1>')-3]
    e2=sen[sen.index('<e2>')+4:b[0].index('</e2>')-3]
    exclude = set(string.punctuation)
    sen = ''.join(ch for ch in sen if ch not in exclude)
    vec=[]

    '''
    
    e1 = ''
    e2 = ''
    for i in sen:
        if(i.startswith('e1')):
            e1=i[2:(len(i)-2)]
        if(i.startswith('e2')):
            e2=i[2:(len(i)-2)]
    '''
    
    if(b[2].startswith('Other')):
       vec.append(e1)
       vec.append(e2)
    elif(b[2].endswith('(e1,e2)')):
       vec.append(e1)
       vec.append(e2)
    else:
       vec.append(e2)
       vec.append(e1)
    

    sen = sen.split()
    s =''
    for i in range(len(sen)):
        if(sen[i].startswith('e1') or sen[i].startswith('e2')):
            s = sen[i]
            s = s[2:(len(s)-2)]
            sen[i] = s
        vec.append(sen[i])

    return vec

'''
0 -> Cause-Effect (CE)
1 -> Instrument-Agency (IA)
2 -> Product-Producer (PP)
3 -> Content-Container (CC)
4 -> Entity-Origin (EO)
5 -> Entity-Destination (ED)
6 -> Component-Whole (CW)
7 -> Member-Collection (MC)
8 -> Message-Topic (MT)
9 -> Other
'''

train=[]
for i in range(10):
    train.append(list())

flag = 9

for i in range(8000):
    b = a[i].split('\n')
    if (b[1].startswith('Cause-Effect')):
        flag=0
    elif (b[1].startswith('Instrument-Agency')):
        flag=1
    elif (b[1].startswith('Product-Producer')):
        flag=2
    elif (b[1].startswith('Content-Container')):
        flag=3
    elif (b[1].startswith('Entity-Origin')):
        flag=4
    elif (b[1].startswith('Entity-Destination')):
        flag=5
    elif (b[1].startswith('Component-Whole')):
        flag=6
    elif (b[1].startswith('Member-Collection')):
        flag=7
    elif (b[1].startswith('Message-Topic')):
        flag=8
    else:
        flag=9
    train[flag].append(extract(i))


for i in range(10):
    for j in range(len(train[i])):
                   v = []
                   c = ' '.join(train[i][j][2:])    #excluding e1 and e2
                   wiki = TextBlob(c)
                   c = wiki.tags
                   for k in range(len(c)):
                       if(c[k][1].startswith('V') or c[k][1].startswith('I')):
                           v.append(c[k][0])
                   train[i][j][2:]=v[:]
dir= os.path.normpath('D:\\Semantic-Evaluation-master')
f = 'rel_'
for i in range(10):
    fn = f + str(i) +'.txt'
    x = open(os.path.join(dir,fn), "a")
    for  j in range(len(train[i])):
        for k in range(len(train[i][j])):
            x.write(train[i][j][k])
            x.write(' ')
        x.write('\n')
    x.close()
