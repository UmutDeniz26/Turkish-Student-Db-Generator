# encoding:utf-8

import random
def formatCustomDigit(number,digitNumberOfReturn):
    counter=0
    holdNumber=number
    while(number>=1):
        number/=10
        counter+=1
    
    return "0"*(digitNumberOfReturn-counter)+str(holdNumber)

names=open('attributes/isimler.txt','r',encoding='utf-8')
nameLines=names.readlines()

lastnames=open('attributes/soyisimler.txt','r',encoding='utf-8')
lastNameLines =lastnames.readlines()

pob=open('attributes/sehirler.txt','r',encoding='utf-8')
pobLines =pob.readlines()

depts=open('attributes/bolumler.txt','r',encoding='utf-8')
deptsLines =depts.readlines()

numberOfStudents=1000; #type the # of students youn want 

f=open('data.json', 'w', encoding='utf-8')
f.write('{"students":[')    

for i in range(numberOfStudents):
    f.write('\n{')
    f.write('\n\t"id": '+str(i+1)+',')
    f.write('\n\t"fname": "'+nameLines[random.randint(1,len(nameLines)-1)].replace('\n','').title()+'"'+',')
    f.write('\n\t"lname": "'+lastNameLines[random.randint(1,len(lastNameLines)-1)].replace('\n','').title()+'"'+',')
    f.write('\n\t"num": "15212'+formatCustomDigit(random.randint(1,9999999),7)+'",')
    f.write('\n\t"dept": "'+deptsLines[random.randint(1,len(deptsLines)-1)].replace('\n','').title() +'",')
    f.write('\n\t"pob": "'+pobLines[random.randint(0,len(pobLines)-1)].replace('\n','').replace('\t','')+'",')
    f.write('\n\t"dob": "'+str(random.randint(1997,2001))+'-'+
        str(formatCustomDigit(random.randint(1,12),2))+'-'+str(formatCustomDigit(random.randint(1,30),2))+'"')
    f.write('\n}'+ ',' if i!=numberOfStudents-1 else '' + '\n}')

f.write('\t]\n}')
f.close()
names.close()
lastnames.close()
pob.close()
depts.close()