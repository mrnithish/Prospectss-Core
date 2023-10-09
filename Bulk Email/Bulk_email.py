import csv,openpyxl
import pandas as pd
import re,email,is_disposable_email
from email_validator import validate_email, EmailNotValidError

#Excel creation
excel=openpyxl.Workbook()
sheet=excel.active
sheet.title='Verified Emails'
sheet.append(['Email','Validate Email','Domain Address','Disposable Email','Deliverable Email','Reason'])

#read data from csv
with open('email.csv',encoding='utf-8-sig') as csvfile:
    reader=csv.DictReader(csvfile)
    email_list=[]
    for row in reader:
        #print(row['Email'])
        email_list.append(row['Email']) #csv to append list

# print(email_list)
#list creation for data storing
Size_of_List=len(email_list)
isvalidemail=[]
isDomainAddress=[]
isDisposableMail=[]
isDeliverableMail=[]
isReason=[]


def domainAddress(res): # identity domain address
    res = res.split('@')[1]
    # print(res)
    isDomainAddress.append(res)

def checkemail(s):# check email is valid 
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if re.match(pattern,s):
        # print("Valid Email")
        isvalidemail.append("Valid Email")
    else:
        # print("Invalid Email")
        isvalidemail.append("Invalid Email")

def disposableEmail(email):  # check it is disposal or not mail
    result = is_disposable_email.check(email)
    if(result==True):
        #print("Disposable Email")
        isDisposableMail.append("Yes")
    else:
        # print("Non Disposable Email")
        isDisposableMail.append("No")

def emailValidate(email):  # check the email deliverability 
    try:
        emailinfo = validate_email(email, check_deliverability=True)
        email = emailinfo.normalized
        # print("Deliverable Email")
        isDeliverableMail.append("Yes")
        isReason.append("-")
    except EmailNotValidError as e:
        # print("Not Deliverable Email")
        # print(str(e))
        isDeliverableMail.append("No")
        isReason.append(str(e)) #reason for not deliverable 
        


for i in range(0,Size_of_List):
    email=email_list[i]    

    checkemail(email)

    domainAddress(email)

    disposableEmail(email)

    emailValidate(email) #deliverable mail or not


try:
    for i in range(0,Size_of_List):
        sheet.append([email_list[i],isvalidemail[i],isDomainAddress[i],isDisposableMail[i],isDeliverableMail[i],isReason[i]]) #Appending the data to the excelsheet
    excel.save('Email Verification.xlsx')
    print("Successfull")
except Exception as e:
    print("error")

# email=input("Enter the email:")

# checkemail(email)

# domainAddress(email)

# disposableEmail(email)

# emailValidate(email)
