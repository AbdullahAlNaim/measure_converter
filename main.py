def fToC(t):
    c = (t -32)/ 1.8
    print(c, 'Celsius')

def cToF(t):
    f = (t * 1.8) + 32
    print(f, 'Fahrenheits')

def inchToCent(m):
    inches = m * 2.54
    print(inches, 'Centimeters')    

def centToInch(m):
    cm = m / 2.54
    print(cm, 'Inches')  

ans = input('What would you like to convert: \nA: Fahrenheit to Celsius \nB: Celsius to Fahrenheit \nC: Inches to Centemeters\nD: Centemeters to Inches\n')

if ans == 'a' or ans == 'A':  
    t = int(input('how many fahrenheits?\n'))
    fToC(t) 
elif ans == 'b' or ans == 'B':  
    t = int(input('how many celsius?\n'))
    cToF(t)   
elif ans == 'c' or ans == 'C':
    m = int(input('how many inches?\n'))
    inchToCent(m)
elif ans == 'd' or ans == 'D':
    m = int(input('how many centimeters?\n'))
    centToInch(m)