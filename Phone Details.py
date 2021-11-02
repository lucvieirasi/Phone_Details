import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobileNo = input("Insira o numero com o codigo do pais: ")
mobileNo = phonenumbers.parse(mobileNo)

#Pegando as timezone`s dos numeros telefonicos.
print(timezone.time_zones_for_number(mobileNo))

print(carrier.name_for_number(mobileNo, "br"))

# Pegando a regiao da informacao
print(geocoder.description_for_number(mobileNo))

#Validando o numero de telefone
print(" Numero de telefone valid :",phonenumbers.is_valid_numbe(mobileNo))

#Checando Possibilidade do numero
print("Checando a possibilidade do numero :",phonenumbers.is_possible_number(mobileNo))
