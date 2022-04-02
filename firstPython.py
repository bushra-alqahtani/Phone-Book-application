 #dictionary
contact_list = {
	'1111111111' : "Amal",
	'2222222222' : "Mohammed",
	'3333333333' : "Khadijah",
	'4444444444' : "Abdullah",
	'5555555555' : "Rawan",
	'6666666666' : "Faisal",
	'7777777777'  : "Layla"
}
# this Function Takes number to get username
def NumberSearch(con,number):
    if len(uinput) == 10 and number.isdigit():
        for number , name in con.items():
            if uinput == number:
                return name
        else:
            return "Sorry, the number is not found "
    else:
        return "This is invalid number"


# This Function takes a name to get phone number
def NameSearch(con , name):
    for number,name in con.items():
        if uinput == name:
            return number
    else:
        return "The name you've entered isn't in list"

# This Function let the user to add new contact info
def AddContact(con,number,name):
    if len(number) == 10 and number.isdigit():
        con[number] = name
    else:
        return "Error , Please use 10 length number or valid number"
    return con


message = int(input("Welcome to Phone Book application  \n\n Use 1 to search using number \n Use 2 to search using name \n use 3 to add new contact \n use 4 to exit  \n \t Select Number : "))

#  This while loop to keep the app running till you exit
while message != 4:
    if message == 1:
        uinput = input("enter phone number here : ")
        print(NumberSearch(contact_list,uinput))
    elif message == 2:
        uinput = input("enter the name here : ")
        print(NameSearch(contact_list,uinput))
    elif message == 3:
        uinput = input("enter the phone number here : ")
        username = input("enter username here : ")
        print(AddContact(contact_list,uinput,username))
    elif message == 4:
        exit()
    else:
        print("Error occured ; Please use one of options 1 , 2, 3 , 4")

    message = int(input("Welcome to Phone Book application  \n\n Use 1 to search using number \n Use 2 to search using name \n use 3 to add new contact \n use 4 to exit  \n \t Select Number : "))
