# change from celcius to fahrenheit
def main():
   converter(float(input('Enter the temperature in celcius:')))


def converter(celcius):
   fahrenheit = (celcius*(9/5)) + 32
   print('The temperature in fahrenheit is '+str(fahrenheit)) 

main()

