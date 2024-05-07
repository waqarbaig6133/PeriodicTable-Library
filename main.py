print("_______________________")
print("DIGITAL PERIODIC TABLE")
print("_______________________")

Options = {
    "1": "Element Name",
    "2": "Formula",
    "3": "Atomic Number",
    "4": "Molar Mass"

}
symbols = {
    "H": "Name: Hydrogen \n Atomic Number: 1 \n Molar Mass: 1.008g/mol \n Valence Electrons: 1 \n Orbitals: 1s",
    "He": "Name: Helium \n Atomic Number: 2 \n Molar Mass: 4.003g/mol \n Valence Electrons: 2 \n Orbitals: 1s",
    "Li": "Name: Lithium \n Atomic Number: 3 \n Molar Mass: 6.941g/mol \n Valence Electrons: 1 \n Orbitals: 2s",
    "Be": "Name: Beryllium \n Atomic Number: 4 \n Molar Mass: 9.012g/mol \n Valence Electrons: 2 \n Orbitals: 2s",
    "B": "Name: Boron \n Atomic Number: 5 \n Molar Mass: 10.811g/mol \n Valence Electrons: 3 \n Orbitals: 2p",
    "C": "Name: Carbon \n Atomic Number: 6 \n Molar Mass: 12.011g/mol \n Valence Electrons: 4 \n Orbitals: 2p",
    "N": "Name: Nitrogen \n Atomic Number: 7 \n Molar Mass: 14.007g/mol \n Valence Electrons: 5 \n Orbitals: 2p",
    "O": "Name: Oxygen \n Atomic Number: 8 \n Molar Mass: 15.999g/mol \n Valence Electrons: 6 \n Orbitals: 2p",
    "F": "Name: Fluorine \n Atomic Number: 9 \n Molar Mass: 18.998g/mol \n Valence Electrons: 7 \n Orbitals: 2p",
    "Ne": "Name: Neon \n Atomic Number: 10 \n Molar Mass: 20.180g/mol \n Valence Electrons: 8 \n Orbitals: 2p",
    "Na": "Name: Sodium \n Atomic Number: 11 \n Molar Mass: 22.990g/mol \n Valence Electrons: 1 \n Orbitals: 3s",
    "Mg": "Name: Magnesium \n Atomic Number: 12 \n Molar Mass: 24.305g/mol \n Valence Electrons: 2 \n Orbitals: 3s",
    "Al": "Name: Aluminum \n Atomic Number: 13 \n Molar Mass: 26.982g/mol \n Valence Electrons: 3 \n Orbitals: 3p",
    "Si": "Name: Silicon \n Atomic Number: 14 \n Molar Mass: 28.085g/mol \n Valence Electrons: 4 \n Orbitals: 3p",
    "P": "Name: Phosphorus \n Atomic Number: 15 \n Molar Mass: 30.974g/mol \n Valence Electrons: 5 \n Orbitals: 3p",
    "S": "Name: Sulfur \n Atomic Number: 16 \n Molar Mass: 32.06g/mol \n Valence Electrons: 6 \n Orbitals: 3p",
    "Cl": "Name: Chlorine \n Atomic Number: 17 \n Molar Mass: 35.45g/mol \n Valence Electrons: 7 \n Orbitals: 3p",
    "Ar": "Name: Argon \n Atomic Number: 18 \n Molar Mass: 39.948g/mol \n Valence Electrons: 8 \n Orbitals: 3p",
    "K": "Name: Potassium \n Atomic Number: 19 \n Molar Mass: 39.098g/mol \n Valence Electrons: 1 \n Orbitals: 4s",
    "Ca": "Name: Calcium \n Atomic Number: 20 \n Molar Mass: 40.078g/mol \n Valence Electrons: 2 \n Orbitals: 4s",
    "Sc": "Name: Scandium \n Atomic Number: 21 \n Molar Mass: 44.956g/mol \n Valence Electrons: 3 \n Orbitals: 3d",
    "Ti": "Name: Titanium \n Atomic Number: 22 \n Molar Mass: 47.867g/mol \n Valence Electrons: 4 \n Orbitals: 3d",
    "V": "Name: Vanadium \n Atomic Number: 23 \n Molar Mass: 50.942g/mol \n Valence Electrons: 5 \n Orbitals: 3d",
    "Cr": "Name: Chromium \n Atomic Number: 24 \n Molar Mass: 51.996g/mol \n Valence Electrons: 6 \n Orbitals: 3d",
    "Mn": "Name: Manganese \n Atomic Number: 25 \n Molar Mass: 54.938g/mol \n Valence Electrons: 7 \n Orbitals: 3d",
    "Fe": "Name: Iron \n Atomic Number: 26 \n Molar Mass: 55.845g/mol \n Valence Electrons: 8 \n Orbitals: 3d",
    "Co": "Name: Cobalt \n Atomic Number: 27 \n Molar Mass: 58.933g/mol \n Valence Electrons: 9 \n Orbitals: 3d",
    "Ni": "Name: Nickel \n Atomic Number: 28 \n Molar Mass: 58.693g/mol \n Valence Electrons: 10 \n Orbitals: 3d",
    "Cu": "Name: Copper \n Atomic Number: 29 \n Molar Mass: 63.546g/mol \n Valence Electrons: 11 \n Orbitals: 3d",
    "Zn": "Name: Zinc \n Atomic Number: 30 \n Molar Mass: 65.38g/mol \n Valence Electrons: 12 \n Orbitals: 3d",
    "Ga": "Name: Gallium \n Atomic Number: 31 \n Molar Mass: 69.723g/mol \n Valence Electrons: 13 \n Orbitals: 4p",
    "Ge": "Name: Germanium \n Atomic Number: 32 \n Molar Mass: 72.63g/mol \n Valence Electrons: 14 \n Orbitals: 4p",
    "As": "Name: Arsenic \n Atomic Number: 33 \n Molar Mass: 74.922g/mol \n Valence Electrons: 15 \n Orbitals: 4p",
    "Se": "Name: Selenium \n Atomic Number: 34 \n Molar Mass: 78.971g/mol \n Valence Electrons: 16 \n Orbitals: 4p",
    "Br": "Name: Bromine \n Atomic Number: 35 \n Molar Mass: 79.904g/mol \n Valence Electrons: 17 \n Orbitals: 4p",
    "Kr": "Name: Krypton \n Atomic Number: 36 \n Molar Mass: 83.798g/mol \n Valence Electrons: 18 \n Orbitals: 4p",
    "Rb": "Name: Rubidium \n Atomic Number: 37 \n Molar Mass: 85.468g/mol \n Valence Electrons: 1 \n Orbitals: 5s",
    "Sr": "Name: Strontium \n Atomic Number: 38 \n Molar Mass: 87.62g/mol \n Valence Electrons: 2 \n Orbitals: 5s",
    "Y": "Name: Yttrium \n Atomic Number: 39 \n Molar Mass: 88.906g/mol \n Valence Electrons: 3 \n Orbitals: 4d",
    "Zr": "Name: Zirconium \n Atomic Number: 40 \n Molar Mass: 91.224g/mol \n Valence Electrons: 4 \n Orbitals: 4d",
    "Nb": "Name: Niobium \n Atomic Number: 41 \n Molar Mass: 92.906g/mol \n Valence Electrons: 5 \n Orbitals: 4d",
    "Mo": "Name: Molybdenum \n Atomic Number: 42 \n Molar Mass: 95.95g/mol \n Valence Electrons: 6 \n Orbitals: 4d",
    "Tc": "Name: Technetium \n Atomic Number: 43 \n Molar Mass: 98.0g/mol \n Valence Electrons: 7 \n Orbitals: 4d",
    "Ru": "Name: Ruthenium \n Atomic Number: 44 \n Molar Mass: 101.07g/mol \n Valence Electrons: 8 \n Orbitals: 4d",
    "Rh": "Name: Rhodium \n Atomic Number: 45 \n Molar Mass: 102.91g/mol \n Valence Electrons: 9 \n Orbitals: 4d",
    "Pd": "Name: Palladium \n Atomic Number: 46 \n Molar Mass: 106.42g/mol \n Valence Electrons: 10 \n Orbitals: 4d",
    "Ag": "Name: Silver \n Atomic Number: 47 \n Molar Mass: 107.87g/mol \n Valence Electrons: 11 \n Orbitals: 4d",
    "Cd": "Name: Cadmium \n Atomic Number: 48 \n Molar Mass: 112.41g/mol \n Valence Electrons: 12 \n Orbitals: 4d",
    "In": "Name: Indium \n Atomic Number: 49 \n Molar Mass: 114.82g/mol \n Valence Electrons: 13 \n Orbitals: 5p",
    "Sn": "Name: Tin \n Atomic Number: 50 \n Molar Mass: 118.71g/mol \n Valence Electrons: 14 \n Orbitals: 5p",
    "Sb": "Name: Antimony \n Atomic Number: 51 \n Molar Mass: 121.76g/mol \n Valence Electrons: 15 \n Orbitals: 5p",
    "Te": "Name: Tellurium \n Atomic Number: 52 \n Molar Mass: 127.6g/mol \n Valence Electrons: 16 \n Orbitals: 5p",
    "I": "Name: Iodine \n Atomic Number: 53 \n Molar Mass: 126.9g/mol \n Valence Electrons: 17 \n Orbitals: 5p",
    "Xe": "Name: Xenon \n Atomic Number: 54 \n Molar Mass: 131.29g/mol \n Valence Electrons: 18 \n Orbitals: 5p",
    "Cs": "Name: Cesium \n Atomic Number: 55 \n Molar Mass: 132.91g/mol \n Valence Electrons: 1 \n Orbitals: 6s",
    "Ba": "Name: Barium \n Atomic Number: 56 \n Molar Mass: 137.33g/mol \n Valence Electrons: 2 \n Orbitals: 6s",
    "La": "Name: Lanthanum \n Atomic Number: 57 \n Molar Mass: 138.91g/mol \n Valence Electrons: 3 \n Orbitals: 5d",
    "Ce": "Name: Cerium \n Atomic Number: 58 \n Molar Mass: 140.12g/mol \n Valence Electrons: 4 \n Orbitals: 4f",
    "Pr": "Name: Praseodymium \n Atomic Number: 59 \n Molar Mass: 140.91g/mol \n Valence Electrons: 5 \n Orbitals: 4f",
    "Nd": "Name: Neodymium \n Atomic Number: 60 \n Molar Mass: 144.24g/mol \n Valence Electrons: 6 \n Orbitals: 4f",
    "Pm": "Name: Promethium \n Atomic Number: 61 \n Molar Mass: 145.0g/mol \n Valence Electrons: 7 \n Orbitals: 4f",
    "Sm": "Name: Samarium \n Atomic Number: 62 \n Molar Mass: 150.36g/mol \n Valence Electrons: 8 \n Orbitals: 4f",
    "Eu": "Name: Europium \n Atomic Number: 63 \n Molar Mass: 151.96g/mol \n Valence Electrons: 9 \n Orbitals: 4f",
    "Gd": "Name: Gadolinium \n Atomic Number: 64 \n Molar Mass: 157.25g/mol \n Valence Electrons: 10 \n Orbitals: 4f",
    "Tb": "Name: Terbium \n Atomic Number: 65 \n Molar Mass: 158.93g/mol \n Valence Electrons: 11 \n Orbitals: 4f",
    "Dy": "Name: Dysprosium \n Atomic Number: 66 \n Molar Mass: 162.5g/mol \n Valence Electrons: 12 \n Orbitals: 4f",
    "Ho": "Name: Holmium \n Atomic Number: 67 \n Molar Mass: 164.93g/mol \n Valence Electrons: 13 \n Orbitals: 4f",
    "Er": "Name: Erbium \n Atomic Number: 68 \n Molar Mass: 167.26g/mol \n Valence Electrons: 14 \n Orbitals: 4f",
    "Tm": "Name: Thulium \n Atomic Number: 69 \n Molar Mass: 168.93g/mol \n Valence Electrons: 15 \n Orbitals: 4f",
    "Yb": "Name: Ytterbium \n Atomic Number: 70 \n Molar Mass: 173.05g/mol \n Valence Electrons: 16 \n Orbitals: 4f",
    "Lu": "Name: Lutetium \n Atomic Number: 71 \n Molar Mass: 174.97g/mol \n Valence Electrons: 17 \n Orbitals: 4f",
    "Hf": "Name: Hafnium \n Atomic Number: 72 \n Molar Mass: 178.49g/mol \n Valence Electrons: 18 \n Orbitals: 5d",
    "Ta": "Name: Tantalum \n Atomic Number: 73 \n Molar Mass: 180.95g/mol \n Valence Electrons: 1 \n Orbitals: 5d",
    "W": "Name: Tungsten \n Atomic Number: 74 \n Molar Mass: 183.84g/mol \n Valence Electrons: 2 \n Orbitals: 5d",
    "Re": "Name: Rhenium \n Atomic Number: 75 \n Molar Mass: 186.21g/mol \n Valence Electrons: 3 \n Orbitals: 5d",
    "Os": "Name: Osmium \n Atomic Number: 76 \n Molar Mass: 190.23g/mol \n Valence Electrons: 4 \n Orbitals: 5d",
    "Ir": "Name: Iridium \n Atomic Number: 77 \n Molar Mass: 192.22g/mol \n Valence Electrons: 5 \n Orbitals: 5d",
    "Pt": "Name: Platinum \n Atomic Number: 78 \n Molar Mass: 195.08g/mol \n Valence Electrons: 6 \n Orbitals: 5d",
    "Au": "Name: Gold \n Atomic Number: 79 \n Molar Mass: 196.97g/mol \n Valence Electrons: 7 \n Orbitals: 5d",
    "Hg": "Name: Mercury \n Atomic Number: 80 \n Molar Mass: 200.59g/mol \n Valence Electrons: 8 \n Orbitals: 5d",
    "Tl": "Name: Thallium \n Atomic Number: 81 \n Molar Mass: 204.38g/mol \n Valence Electrons: 9 \n Orbitals: 6p",
    "Pb": "Name: Lead \n Atomic Number: 82 \n Molar Mass: 207.2g/mol \n Valence Electrons: 10 \n Orbitals: 6p",
    "Bi": "Name: Bismuth \n Atomic Number: 83 \n Molar Mass: 208.98g/mol \n Valence Electrons: 11 \n Orbitals: 6p",
    "Po": "Name: Polonium \n Atomic Number: 84 \n Molar Mass: 209.0g/mol \n Valence Electrons: 12 \n Orbitals: 6p",
    "At": "Name: Astatine \n Atomic Number: 85 \n Molar Mass: 210.0g/mol \n Valence Electrons: 13 \n Orbitals: 6p",
    "Rn": "Name: Radon \n Atomic Number: 86 \n Molar Mass: 222.0g/mol \n Valence Electrons: 14 \n Orbitals: 6p",
    "Fr": "Name: Francium \n Atomic Number: 87 \n Molar Mass: 223.0g/mol \n Valence Electrons: 1 \n Orbitals: 7s",
    "Ra": "Name: Radium \n Atomic Number: 88 \n Molar Mass: 226.0g/mol \n Valence Electrons: 2 \n Orbitals: 7s",
    "Ac": "Name: Actinium \n Atomic Number: 89 \n Molar Mass: 227.0g/mol \n Valence Electrons: 3 \n Orbitals: 6d",
    "Th": "Name: Thorium \n Atomic Number: 90 \n Molar Mass: 232.04g/mol \n Valence Electrons: 4 \n Orbitals: 6d",
    "Pa": "Name: Protactinium \n Atomic Number: 91 \n Molar Mass: 231.04g/mol \n Valence Electrons: 5 \n Orbitals: 5f",
    "U": "Name: Uranium \n Atomic Number: 92 \n Molar Mass: 238.03g/mol \n Valence Electrons: 6 \n Orbitals: 5f",
    "Np": "Name: Neptunium \n Atomic Number: 93 \n Molar Mass: 237.0g/mol \n Valence Electrons: 7 \n Orbitals: 5f",
    "Pu": "Name: Plutonium \n Atomic Number: 94 \n Molar Mass: 244.0g/mol \n Valence Electrons: 8 \n Orbitals: 5f",
    "Am": "Name: Americium \n Atomic Number: 95 \n Molar Mass: 243.0g/mol \n Valence Electrons: 9 \n Orbitals: 5f",
    "Cm": "Name: Curium \n Atomic Number: 96 \n Molar Mass: 247.0g/mol \n Valence Electrons: 10 \n Orbitals: 5f",
    "Bk": "Name: Berkelium \n Atomic Number: 97 \n Molar Mass: 247.0g/mol \n Valence Electrons: 11 \n Orbitals: 5f",
    "Cf": "Name: Californium \n Atomic Number: 98 \n Molar Mass: 251.0g/mol \n Valence Electrons: 12 \n Orbitals: 5f",
    "Es": "Name: Einsteinium \n Atomic Number: 99 \n Molar Mass: 252.0g/mol \n Valence Electrons: 13 \n Orbitals: 5f",
    "Fm": "Name: Fermium \n Atomic Number: 100 \n Molar Mass: 257.0g/mol \n Valence Electrons: 14 \n Orbitals: 5f",
    "Md": "Name: Mendelevium \n Atomic Number: 101 \n Molar Mass: 258.0g/mol \n Valence Electrons: 15 \n Orbitals: 5f",
    "No": "Name: Nobelium \n Atomic Number: 102 \n Molar Mass: 259.0g/mol \n Valence Electrons: 16 \n Orbitals: 5f",
    "Lr": "Name: Lawrencium \n Atomic Number: 103 \n Molar Mass: 266.0g/mol \n Valence Electrons: 17 \n Orbitals: 5f",
    "Rf": "Name: Rutherfordium \n Atomic Number: 104 \n Molar Mass: 267.0g/mol \n Valence Electrons: 18 \n Orbitals: 6d",
    "Db": "Name: Dubnium \n Atomic Number: 105 \n Molar Mass: 268.0g/mol \n Valence Electrons: 1 \n Orbitals: 6d",
    "Sg": "Name: Seaborgium \n Atomic Number: 106 \n Molar Mass: 269.0g/mol \n Valence Electrons: 2 \n Orbitals: 6d",
    "Bh": "Name: Bohrium \n Atomic Number: 107 \n Molar Mass: 270.0g/mol \n Valence Electrons: 3 \n Orbitals: 6d",
    "Hs": "Name: Hassium \n Atomic Number: 108 \n Molar Mass: 269.0g/mol \n Valence Electrons: 4 \n Orbitals: 6d",
    "Mt": "Name: Meitnerium \n Atomic Number: 109 \n Molar Mass: 278.0g/mol \n Valence Electrons: 5 \n Orbitals: 6d",
    "Ds": "Name: Darmstadtium \n Atomic Number: 110 \n Molar Mass: 281.0g/mol \n Valence Electrons: 6 \n Orbitals: 6d",
    "Rg": "Name: Roentgenium \n Atomic Number: 111 \n Molar Mass: 282.0g/mol \n Valence Electrons: 7 \n Orbitals: 6d",
    "Cn": "Name: Copernicium \n Atomic Number: 112 \n Molar Mass: 285.0g/mol \n Valence Electrons: 8 \n Orbitals: 6d",
    "Nh": "Name: Nihonium \n Atomic Number: 113 \n Molar Mass: 286.0g/mol \n Valence Electrons: 9 \n Orbitals: 7p",
    "Fl": "Name: Flerovium \n Atomic Number: 114 \n Molar Mass: 289.0g/mol \n Valence Electrons: 10 \n Orbitals: 7p",
    "Mc": "Name: Moscovium \n Atomic Number: 115 \n Molar Mass: 290.0g/mol \n Valence Electrons: 11 \n Orbitals: 7p",
    "Lv": "Name: Livermorium \n Atomic Number: 116 \n Molar Mass: 293.0g/mol \n Valence Electrons: 12 \n Orbitals: 7p",
    "Ts": "Name: Tennessine \n Atomic Number: 117 \n Molar Mass: 294.0g/mol \n Valence Electrons: 13 \n Orbitals: 7p",
    "Og": "Name: Oganesson \n Atomic Number: 118 \n Molar Mass: 294.0g/mol \n Valence Electrons: 14 \n Orbitals: 7p"
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

    
