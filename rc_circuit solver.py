#Calculator RC circuit
import math
import os

def volt(t, tension, tao, state):
    if state == 1:
        voltage = tension*(1- math.pow(math.e,(-t/tao)))
    elif state == 2:
        voltage = tension*math.pow(math.e,(-t/tao))
    return voltage

def charge(t, q_max, tao, state):
    if state == 1:
        Q = q_max*(1- math.pow(math.e,(-t/tao)))
    elif state == 2:
        Q = q_max*math.pow(math.e,(-t/tao))
    return Q

def intensity(t, I_max, tao):
    I = I_max*math.pow(math.e,(-t/tao))
    return I

def t_from_Vc(Vc, tension, tao, state): #tension = E
    if state == 1:
        t = -tao*math.log(1- Vc/tension)
    elif state == 2:
        t = -tao*math.log(Vc/tension)
    return t

def t_from_I(I, I_max, tao):
    t = -tao*math.log(I/I_max)
    return t

def t_from_Qc(Qc, q_max, tao, state):
    if state == 1:
        t = -tao*math.log(1 - Qc/q_max)
    elif state == 2:
        t = -tao*math.log(Qc/q_max)
    return t


print("Welcome")
os.system('cls' if os.name == 'nt' else 'clear')

print("Insert some dates")
capacity = eval(input("Capacity of the capacitor [F] (use 'e' to use the scientific notation es: 1e10=100):\n"))
resistance = eval(input("Value of the resistor [Ω] (use 'e' to use the scientific notation es: 1e10=100):\n"))
tension = eval(input("The value of the generator [V] (use 'e' to use the scientific notation es: 1e10=100):\n"))
os.system('cls' if os.name == 'nt' else 'clear')

tao = resistance * capacity
i_max = tension / resistance
q_max = tension * capacity

print("States of the circuit:")
print("1 - charge")
print("2 - discharge")
state = eval(input("Select the number of the state of the circuit:\n"))
if state != 1 and state != 2:
    while state != 1 and state != 2:
        state = eval(input("Select the number of the state of the circuit:\n"))
os.system('cls' if os.name == 'nt' else 'clear')

print("Possibilities:")
print("1 - Calculate Vc, Ic, Qc from t")
print("2 - Calculate t from Vc")
print("3 - Calculate t from Ic")
print("2 - Calculate t from Qc")
operation = eval(input("Select the number of the operation to do:\n"))
if operation != 1 and operation != 2 and operation != 3 and operation != 4:
    while operation != 1 and operation != 2 and operation != 3 and operation != 4:
        operation = eval(input("Select the number of the operation to do:\n"))
os.system('cls' if os.name == 'nt' else 'clear')

if operation == 1:
    t = eval(input("Insert the time [s] (use 'e' to use the scientific notation es: 1e10=100):\n"))
    if t <= 0:
        while t <=0:
            t = eval(input("Insert the time [s] (use 'e' to use the scientific notation es: 1e10=100):\n"))
    print("Volt:", volt(t, tension, tao, state), "V")
    print("Charge:", charge(t, q_max, tao, state), "C")
    print("Intensity:", intensity(t, q_max, tao), "A")
elif operation == 2:
    Vc = eval(input("Insert Vc [V] (use 'e' to use the scientific notation es: 1e10=100):\n"))
    if Vc < 0:
        while Vc < 0:
            Vc = eval(input("Insert Vc [V] (use 'e' to use the scientific notation es: 1e10=100):\n"))
    elif Vc == 0:
        if state == 1:
            print("The result is 0")
        elif state == 2:
            print("The result is t = 5*tao or t = ∞")
    else:
        print("The result is:\n", t_from_Vc(Vc, tension, tao, state), "s")
elif operation == 3:
    Ic = eval(input("Insert Ic [A] (use 'e' to use the scientific notation es: 1e10=100):\n"))
    print("The result is:\n", t_from_I(Ic, i_max, tao), "s")
elif operation == 4:
    Qc = eval(input("Insert Qc [C] (use 'e' to use the scientific notation es: 1e10=100):\n"))
    if Qc < 0:
        while Qc < 0:
            Qc = eval(input("Insert Qc [C] (use 'e' to use the scientific notation es: 1e10=100):\n"))
    print("The result is:\n", t_from_Qc(Qc, q_max, tao, state),"C")
t=input("\n\n ### press enter to exit ###")