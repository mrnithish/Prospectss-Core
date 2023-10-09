import phonenumbers
from phonenumbers import geocoder,carrier,timezone


def lineTypeNumber(phone_number):
# Determine the type of phone number
    if phonenumbers.number_type(phone_number) == phonenumbers.PhoneNumberType.MOBILE:
        return"Mobile phone number" 
    elif phonenumbers.number_type(phone_number) == phonenumbers.PhoneNumberType.FIXED_LINE:
        return"Fixed-line phone number" 
    elif phonenumbers.number_type(phone_number) ==phonenumbers.PhoneNumberType.TOLL_FREE:
        return"Toll Free" 
    elif phonenumbers.number_type(phone_number) ==phonenumbers.PhoneNumberType.PREMIUM_RATE:
        return"Premium Rate" 
    elif phonenumbers.number_type(phone_number) ==phonenumbers.PhoneNumberType.PAGER:
        return"Pager" 
    elif phonenumbers.number_type(phone_number) ==phonenumbers.PhoneNumberType.PERSONAL_NUMBER:
        return"Personal Number" 
    elif phonenumbers.number_type(phone_number) ==phonenumbers.PhoneNumberType.UAN:
        return"UAN" 
    elif phonenumbers.number_type(phone_number) ==phonenumbers.PhoneNumberType.SHARED_COST:
        return"Shared Cost" 
    elif phonenumbers.number_type(phone_number) ==phonenumbers.PhoneNumberType.VOIP:
        return"VOIP" 
    elif phonenumbers.number_type(phone_number) ==phonenumbers.PhoneNumberType.UNKNOWN:
        return"Unknown"
    else:
        return"-"




def verifyPhoneNumber(phone_number):
    
    Valid_Number=phonenumbers.is_valid_number(phone_number)

    if Valid_Number==True:

        Country_Code=phone_number.country_code

        National_Number=phone_number.national_number

        Country=geocoder.description_for_number(phone_number,'en')

        Carrier=carrier.name_for_number(phone_number, 'en')

        Time_Zone_Num=timezone.time_zones_for_number(phone_number)

        Valid_Number=phonenumbers.is_valid_number(phone_number)

        Number_Possible=phonenumbers.is_possible_number(phone_number)

        timezones=str(Time_Zone_Num)
        Time_Zones=timezones[2:len(timezones)-3]

        print("Number : "+Number+"\nCountry Code : "+str(Country_Code)+"\nNational Number : "+str(National_Number) +"\nLocation : "+Country+"\nCarrier : "+Carrier+"\nTime Zone : "+Time_Zones+"\nPossible Number : "+str(Number_Possible)+"\nValid Number : "+str(Valid_Number)+"\nLine Type : "+lineTypeNumber(phone_number))
    else:

        print("Wrong Number")

try:
        Number=input("Enter the Phone Numbers with country code: ")

        phone_number = phonenumbers.parse(Number)
    
        verifyPhoneNumber(phone_number)


except Exception:
    print("Type the number with country code")


