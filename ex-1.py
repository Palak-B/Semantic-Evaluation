import os
import string
from textblob import TextBlob

dir = os.path.normpath('C:\\Users\\user\\Downloads\\SemEval2010_task8_all_data\\SemEval2010_task8_all_data\\SemEval2010_task8_training')
f = open(os.path.join(dir,'TRAIN_FILE.TXT'))
a = f.read()
a=a.split('\n\n')

def extract(i):
    temp=b[0].split()
    temp=temp[1:]
    temp = ' '.join(i for i in temp)
    sen = temp
    exclude = set(string.punctuation)
    sen = ''.join(ch for ch in sen if ch not in exclude)
    vec=[]

    sen = sen.split()
    e1 = ''
    e2 = ''
    for i in sen:
        if(i.startswith('e1')):
            e1=i[2:(len(i)-2)]
        if(i.startswith('e2')):
            e2=i[2:(len(i)-2)]

    if(b[2].startswith('Other')):
       vec.append(e1)
       vec.append(e2)
    elif(b[2].endswith('(e1,e2)')):
       vec.append(e1)
       vec.append(e2)
    else:
       vec.append(e2)
       vec.append(e1)

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
    if (b[1].startswith('Content-Container')):
        flag=3
    if (b[1].startswith('Entity-Origin')):
        flag=4
    if (b[1].startswith('Entity-Destination')):
        flag=5
    if (b[1].startswith('Component-Whole')):
        flag=6
    if (b[1].startswith('Member-Collection')):
        flag=7
    if (b[1].startswith('Message-Topic')):
        flag=8
    
