#Wavelength or frequency or photon energy

unit = ""
maximum = -1
minumum = -1
r = {'w' : round(((750-625) / 2) + 625, 4),
    'f' : round(((480-400) / 2) + 400, 4),
    'e' : round(((1.98-1.65) / 2) + 1.65, 4)}
g = {'w' : round(((565-500) / 2) + 500, 4),
    'f' : round(((600-530) / 2) + 530, 4),
    'e' : round(((2.48-2.19) / 2) + 2.19, 4)}
b = {'w' : round(((485-450) / 2) + 450, 4),
    'f' : round(((670-620) / 2) + 620, 4),
    'e' : round(((2.75-2.56) / 2) + 2.56, 4)}

print("Which would you like to translate? ")
while(True):
    print("Type 'w' for wavelength, 'f' for frequency, or 'e' for photon energy:")
    t = input("> ")
    
    match t:
        case 'w' | ' w': 
            unit = 'nm'
            maximum = 750
            minimum = 380
            break
        case 'f' | ' f':
            unit = "THz"
            maximum = 790
            minimum = 400
            break
        case 'e' | ' e': 
            unit = "eV"
            maximum = 3.26
            minimum = 1.65
            break
        case '_': 
            print("Not an option. Try again.")
            continue
            
while(True):
    print("What is your number in " + unit + "s?")
    n = int(input("> "))
    
    if(n < minimum):
        print("Number is too small. Try again.")
        continue
    elif (n > maximum):
        print("Number is too big. Try Again.")
        continue
    else:
        break
        

