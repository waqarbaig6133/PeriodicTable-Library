from elements import symbols
print("_______________________")
print("DIGITAL PERIODIC TABLE")
print("_______________________")

Options = {
    "1": "Element Name",
    "2": "Formula",
    "3": "Atomic Number",
    "4": "Molar Mass"

}

def element():
    print("1. Element Name \n 2. Formula \n 3. Atomic Number \n 4. Molar Mass")
    enter = input("Hi, what information do you already have (Enter Number):")
    if enter == "2":
        symb = input("Enter your symbol: ")
        print(symbols[symb])
        
    elif enter == "1":
        elem = input("Enter the element: ")
        for key, value in symbols.items():
            if elem in value:
                print("symbol: ", key,"\n", value)
                
    elif enter == "4":
        mass = input("Enter the atomic mass of the element (If possible, include 3 decimals): ")
        for key, value in symbols.items():
            if ("Molar Mass: " +mass)  in value:
                print("symbol: ", key, "\n", value)
                
    else:
        number = input("What is the atomic number: ")
        for key, value in symbols.items():
            if ("Atomic Number: "+ number + " \n") in value:
                print("symbol: ", key, "\n", value)
    retake = input("Click R if search another element or another button to exit ")
    if retake == "r" or retake == "R":
        element()
    

element()

    
