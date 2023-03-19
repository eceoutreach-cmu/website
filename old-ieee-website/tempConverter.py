##############################################
###### Write the function tempConverter ######
##############################################

# six helper functions come first

# this first helper function is done for you
def CtoF(start): # converts from Celsius to Fahrenheit
    converted = start * (9/5) + 32
    return converted

def FtoC(start): # converts from Fahrenheit to Celsius
    # do stuff
    return converted

def CtoK(start): # converts from Celsius to Kelvin
    # do stuff
    return converted

def KtoC(start): # converts from Kelvin to Celsius
    # do stuff
    return converted

def FtoK(start): # converts from Fahrenheit to Kelvin
    # do stuff
    return converted

def KtoF(start): # converts from Kelvin to Fahrenheit
    # do stuff
    return converted

# then comes the main function
def tempConverter(inUnit, outUnit, num):
    # You will be calling different functions depending on the input.
    # For example, if inUnit is Kelvin and outUnit is Celsius,
    # you call the function KtoC and save the output in out

    # this first if statement is done for you
    if ((inUnit == "Celsius") and (outUnit == "Fahrenheit")):
        out = CtoF(num) # you call the function CtoF, giving num
        # as the start value of the function. Then,
        # the return value of CtoF is stored in out
        
    elif (something2):
        out = something
    elif (something3):
        out = something
    elif (something4):
        out = something
    elif (something5):
        out = something
    elif (something6):
        out = something
    else: # meaning that it's none of the 6 conversions we have available
        out = "error: unknown conversion"
    return out

# now that we wrote the function, we want to call it!
# this is an example
print tempConverter("Celsius", "Kelvin", 18)

