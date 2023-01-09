# encoding:utf-8

import random
def format2Digit(number):
    if 0 < number < 10:
        return "0" + str(number)
    else:
        return str(number)
    
pobs=["Eskisehir","Istanbul","Ankara","Bursa","Izmir"];

depts=["Bilgisayar Müh.","Elektrik-Elektronik Müh.","Endüstri Müh.","İnşaat Müh."]

f=open('data.json', 'w', encoding='utf-8')
names=open('isimler.txt','r',encoding='utf-8')
lines =names.readlines()

lastnames=open('soyisimler.txt','r',encoding='utf-8')
lastlines =lastnames.readlines()

sehirler=open('sehirler.txt','r',encoding='utf-8')
sehirlerLines =sehirler.readlines()

#selam
f.write('{"students":[')    
numberOfStudents=300;
for i in range(numberOfStudents):
    f.write('\n{')
    f.write('\n\t"id": '+str(i+1)+',')
    f.write('\n\t"fname": "'+lines[random.randint(1,len(lines)-1)].replace('\n','').title()+'"'+',')
    f.write('\n\t"lname": "'+lastlines[random.randint(1,len(lastlines)-1)].replace('\n','').title()+'"'+',')
    f.write('\n\t"num": "15212017'+format2Digit(random.randint(1,99))+""+format2Digit(random.randint(1,99))+'",')
    f.write('\n\t"dept": "'+str(random.randint(1,4)) +'",')
    f.write('\n\t"pob": "'+sehirlerLines[random.randint(0,len(sehirlerLines)-1)].replace('\n','').replace('\t','')+'",')
    f.write('\n\t"dob": "'+str(random.randint(1997,2001))+'-'+str(format2Digit(random.randint(1,12)))+'-'+str(format2Digit(random.randint(1,30)))+'"')
    f.write('\n}')
    if i!=numberOfStudents-1:
        f.write(',')
    f.write('\n')
f.write('\t]\n}')
f.close()
names.close()
