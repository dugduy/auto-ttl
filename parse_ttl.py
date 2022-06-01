from json import dump
data=open('./Bản sao của STNHĐ - PHASE 5 - CÂU HỎI TRẮC NGHIỆM - TV02 - 025.txt',encoding='utf8').read()
f=open('data.json','w')
ttal=[]
for i in range(1,100,1):
    print(i)
    aq=data[data.index('Câu hỏi %s'%i):data.index('Câu hỏi %s'%(i+1))]
    ans=aq.split('Các phương án lựa chọn:')[1]
    ans_parsed=[]
    crctn=''
    for l in ans.split('\n'):
        if ':' not in l:
            # print('ctn!')
            # print(l)
            crctn+='\n'+l
            # print(crctn)
            continue
        elif l!='':
            # print(crctn)
            if len(ans_parsed):
                ans_parsed[-1][-1]+=crctn
            # l+=crctn
            crctn=''
            ans_parsed.append(l.split(':',1))
    ans_parsed=dict(ans_parsed)
    # print(ans_parsed)
    q=aq.split('Các phương án lựa chọn:')[0]
    q_parsed=[]
    crctn=''
    for l in q.split('\n'):
        if ':' not in l:
            # print('ctn!')
            # print(l)
            crctn+='\n'+l
            # print(crctn)
            continue
        elif l!='':
            # print(crctn)
            if len(q_parsed):
                q_parsed[-1][-1]+=crctn
            # l+=crctn
            crctn=''
            q_parsed.append(l.split(':',1))
    q_parsed=dict(q_parsed)
    # print(q_parsed)
    ttal.append({'q':q_parsed,'a':ans_parsed})
print(ttal)
dump(ttal,f)