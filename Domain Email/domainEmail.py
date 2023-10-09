from emailfinder.extractor import *


emails1 = get_emails_from_google("snsce.ac.in")
emails2 = get_emails_from_bing("snsce.ac.in")
#emails3 = get_emails_from_baidu("snsce.ac.in")
print(emails1)
print(emails2)