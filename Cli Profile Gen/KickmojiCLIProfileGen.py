print("Run Multiple times for each profile you want to set up, Made by @Sunmeetzenda @adneZ")



ProfileNum = input("What is this profile Number :")

nickname = input("What nickname do you want to give this Profile?:")

firstname= input("What is your First name? Or type {random} for random name:")

lastname= input("what is your last name? Or type {random} for random name:")

Phname= input("What is your Phonetic Name, Press Enter to Skip:")

Phlastname= input("what is your Phonetic Last Name, Press Enter to Skip:")

#code must be 6 letters
while True:
  phonenumber = input('Input the first 6 numbers of your phone number:')
  if len(phonenumber) == 6:
    break
  else:
    print('The Phone number must be 6 characters')

CardType= input("Enter Card Type: Visa, Americanexpress, Discover, or Mastercard MUST BE SPELLED RIGHT:")

CardNum= input("Enter your entire Card Number:")

Cardcvv= input("Enter your card CVV:")

#code must be 2 letters
while True:
  ExpirationMonth = input('Enter your Card Expiration Month, Example (03 for March or 10 for October):')
  if len(ExpirationMonth) == 2:
    break
  else:
    print('The ExpirationMonth must be 2 Numbers')

#code must be 4 letters
while True:
  ExpirationYear = input('Enter Expiration Year, Example (2022):')
  if len(ExpirationYear) == 4:
    break
  else:
    print('The ExpirationYear must be 4 Numbers')

Address1= input("Enter your Address for line 1 (only street name and Number):")

Address2= input("Enter your Address for line 2 if Required, Or input {random} for a random Apartment:")

Address3= input("Enter you Address for line 3 if Required:")


City= input("Enter your City:")

#state must be 2 Letters
while True:
  state = input('Input your state:')
  if len(state) == 2:
    break
  else:
    print('The state must be 2 characters')

#Country code must be 2 letters
while True:
  Country = input("What Country are you from? US OR GB OR UK:")
  if len(Country) ==2:
    break
  else:
    print("Country Code must be 2 Letters!")

Postal= input("What is your postal Code or Zip Code:")



print("PROFILE LAYOUT**************")
print("id,nickName,firstName,lastName,phoneticName,phoneticSurname,phoneNumber,cardType,cardNumber,cardCVV,expireMonth,expireYear,address1,address2,address3,city,state,country,postal")
print("Your Profile BELOW")
profileinputs =(ProfileNum +','+ nickname +','+ firstname +','+ lastname +','+ Phname +','+ Phlastname +','+ phonenumber +"{random4}"+','+ CardType +','+ CardNum +','+ Cardcvv +','+ ExpirationMonth +','+ ExpirationYear +','+ "{random} "+ Address1 +','+ Address2 +','+ Address3 +','+ City +','+ state +','+ Country +','+ Postal )
print('_______________________________________________________________________________________________________________________________________')
print('_______________________________________________________________________________________________________________________________________')

print("Lets Double check a few things, is the task Number-----"+ '\t'+ '\t', ProfileNum)
print("Lets Double check a few things, is the Nickname-----"+ '\t'+ '\t', nickname)
print("Lets Double check a few things, is the firstname-----"+ '\t'+ '\t', firstname)
print("Lets Double check a few things, is the Last Name-----"+ '\t'+ '\t', lastname)
print("Lets Double check a few things, is the Phone number -----"+ '\t', phonenumber + "{random4}")
print("Lets Double check a few things, is the Card Type-----"+ '\t'+ '\t', CardType)
print("Lets Double check a few things, is the Card Number-----"+ '\t'+ '\t', CardNum)
print("Lets Double check a few things, is the Card CVV-----"+ '\t'+ '\t', Cardcvv)
print("Lets Double check a few things, is the Expiration month-----"+ '\t', ExpirationMonth)
print("Lets Double check a few things, is the Expiration year-----"+ '\t', ExpirationYear)
print("Lets Double check a few things, is the Address 1-----"+ '\t'+ '\t', "{random} "+Address1)
print("Lets Double check a few things, is the Address 2-----"+ '\t'+ '\t', Address2, )
print("Lets Double check a few things, is the City-----"+ '\t'+ '\t', City)
print("Lets Double check a few things, is the state-----"+ '\t'+ '\t', state)
print("Lets Double check a few things, is the Country------"+ '\t'+ '\t', Country)
print("Lets Double check a few things, is the Postal Code ------"+ '\t', Postal)
print("-------------------------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------------------------")

while True:
  question= input("Does Everything in the Profile Look correct? (Yes or No)")
  if len(question) ==3:
    break
  else:
    print('Please Close the Window and Try Again :)')


print("-------------------------------------------------------------------------------------------------------------------")



print("""

         ________ ________   ________  ________         ____.________ __________
        /  _____/ \_____  \  \_____  \ \______ \       |    |\_____  \\______   /
       /   \  ___  /   |   \  /   |   \ |    |  \      |    | /   |   \|    |  _/
       \    \_\  \/    |    \/    |    \|    `   \ /\__|    |/    |    \    |   /
        \______  /\_______  /\_______  /_______  / \________|\_______  /______  /
               \/         \/         \/        \/                    \/       \/
        


        """)

filename= ("Profiles.csv")
f = open(filename,'a')

f.write(profileinputs+ '\n')

