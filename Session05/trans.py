dict = {
"Monday": "Thu 2",
"Tuesday": "Thu 3"

}

code = input ("Enter code:")
if code in dict:
    print(dict[code])
else:
    user_choice = input("Wish to contribute (Y/N)? ").upper()
    if user_choice == "Y":
        trans = input ("Enter translation")
        dict[code] = trans
        print(code)              
                                                                                                                                                          
