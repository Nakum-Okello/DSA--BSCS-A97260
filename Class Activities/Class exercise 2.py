# Number 1
count = 0
total = 0

while True:
    num = input("Enter a number: ")
    
    if num == "done":
        break
    
    try:
        num = float(num)
        count += 1
        total += num
    except:
        print("Invalid input")
        continue

if count > 0:
    average = total / count
    print("Total =", total, "Count =", count, "Average =", average)
else:
    print("No numbers entered")




#NUmber 2
name = input('Enter Client name:                  ')
loan = input('Enter the amount of the loan:       ')
days = input('Enter the days taken with the loan: ')

loan = int(loan)
days = int(days)

if days <= 30:
    amount = (loan)+(0.1*loan)
    print(f'The total amount from ',name,' is ',amount)
elif days > 30:
    amount = (loan)+(0.1*loan)+(0.01*loan)
    print(f'The total amount from ',name,' is ',amount)