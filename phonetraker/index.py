import phonenumbers 
from phonenumbers import geocoder, carrier, timezone

number = input("Entrez le numéro de téléphone: ")
phone_number = phonenumbers.parse(number)

print("Pays                 : ", geocoder.description_for_number(phone_number, 'fr'))
print("Opérateur            : ", carrier.name_for_number(phone_number, 'fr'))
print("Timezone             : ", timezone.time_zones_for_number(phone_number))
print("Valide               : ", phonenumbers.is_valid_number(phone_number))
print("Possible             : ", phonenumbers.is_possible_number(phone_number))
print("Format international : ", phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL))
print("Format national      : ", phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.NATIONAL))
print("Format E164          : ", phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.E164))