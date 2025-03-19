import phonenumbers
from phonenumbers.geocoder import description_for_number

phone_number2 = phonenumbers.parse("+254743339801")

print("\nPhone Numbers Location\n")

print(description_for_number(phone_number2,"en"))