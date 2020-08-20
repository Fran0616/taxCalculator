#this code calculate the tax of citizen. If the citizen income is less than 85528 the tax charge will be equal to 18% of the citizen income minus 556
#If the income is higher than 85,528 the tax is the income subtracted by 855528 times 32% plus 14839.02.
#the code also has a nested if statment to display the tax as zero and not a negative number
#there is also the round() function that will be rounding the tax.
#Sample input: 10000
#Output: The tax is: 1244.0 dollars
#Sample input: -100
#Output: The tax is: 0 dollars
income = float(input("Enter the annual income do not include any comma: "))


if income < 85528:
    tax = (0.18 * income) - 557.02
    if tax < 0:
        tax = 0
elif income > 85528:
    tax = (income - 85528)* 0.32 + (14839.02)


tax = round(tax, 0)
print("The tax is:", tax, "dollars")   
