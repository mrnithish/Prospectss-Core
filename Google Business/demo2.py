from google_business_listing_scraper import *
response = google.business_listing_scraper(business_url="https://www.google.com/search?q=coffee+shops+near+%2Cme&rlz=1C1CHBF_enIN1043IN1043&biw=1233&bih=950&tbm=lcl&sxsrf=AJOqlzXH9DfJKhK8g_UvXTlPB7iyy2y_fw%3A1678704449794&ei=Qf8OZJ-SMOadseMP8vaS2AU&ved=0ahUKEwjftqaz3dj9AhXmTmwGHXK7BFsQ4dUDCAk&uact=5&oq=coffee+shops+near+%2Cme&gs_lcp=Cg1nd3Mtd2l6LWxvY2FsEAMyCggAELEDEMkDEEMyBQgAEJIDMgQIABBDMgQIABBDMgQIABBDMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgARQAFgAYKiFFmgDcAB4AIABqAGIAagBkgEDMC4xmAEAwAEB&sclient=gws-wiz-local#rlfi=hd:;si:;mv:[[11.117090099999999,77.043917],[11.034794999999999,76.9816314]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:9")
data=response['body']
print(data)