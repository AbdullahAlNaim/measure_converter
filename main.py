def fToC(t):
    c = round((t -32)/ 1.8, 2)
    print(c, 'Celsius')

def cToF(t):
    f = round((t * 1.8) + 32)
    print(f, 'Fahrenheits')

def inchToCent(m):
    inches = round(m * 2.54,2)
    print(inches, 'Centimeters')    

def centToInch(m):
    cm = round(m / 2.54, 2)
    print(cm, 'Inches') 

def footToMeter(m):
    meter = round(m * .3048, 2)
    print(meter)    

ans = input('What would you like to convert: \nA: Fahrenheit to Celsius \nB: Celsius to Fahrenheit \nC: Inches to Centemeters\nD: Centemeters to Inches\nE: Foot to Meters\n')

if ans == 'a' or ans == 'A':  
    t = int(input('how many fahrenheits would you like to convert?\n'))
    fToC(t) 
elif ans == 'b' or ans == 'B':  
    t = int(input('how many celsius would you like to convert?\n'))
    cToF(t)   
elif ans == 'c' or ans == 'C':
    m = int(input('how many inches would you like to convert?\n'))
    inchToCent(m)
elif ans == 'd' or ans == 'D':
    m = int(input('how many centimeters would you like to convert?\n'))
    centToInch(m)
elif ans == 'E' or ans == 'e':
    m = int(input('how many feet would you like to convert?\n'))    
    footToMeter(m)
