
#using dictionary
def convert(number):
    output = ''
    factors = {
        3 : 'pling',
        5 : 'plong',
        7 : 'plang',
    }
    for key,value in factors.items():
        if (number % key == 0):
            output = output + value
    return output if output else str(number)

