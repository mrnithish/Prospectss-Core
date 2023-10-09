from emailfinder.extractor import *
import csv,openpyxl
import pandas as pd

#Excel creation
excel=openpyxl.Workbook()
sheet=excel.active
sheet.title='Email List'
sheet.append(['Domain Name','Email'])

domain_list=[]


#read data from csv
with open('email.csv',encoding='utf-8-sig') as csvfile:
    reader=csv.DictReader(csvfile)
    domain_list=[]
    for row in reader:
        #print(row['Email'])
        domain_list.append(row['Email']) #csv to append list

for i in range(0,len(domain_list)):
    domain=domain_list[i]
    print('Domain :'+domain)
    emails1 = get_emails_from_google(domain)
    emails2 = get_emails_from_bing(domain)
    #emails3 = get_emails_from_baidu("snsce.ac.in")
    for i in range(0,len(emails1)):
        sheet.append([domain,emails1[i]])
    for i in range(0,len(emails2)):
        sheet.append([domain,emails2[i]])
    excel.save('Email Verification.xlsx')
    print("Successfull")