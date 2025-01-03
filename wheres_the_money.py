'''
Brielle Foster
CSC110
Project -3
This program is calculating tax and creating a financial breakdown.
'''

def calculate_tax(annual_salary):
    '''
    This function returns the calculated tax.
    Args:
        The argument is the annual salary
    Returns: 
        The calculated tax.
    '''
    
    tax_percentage = 0
    if 0 <= annual_salary and annual_salary <= 15000:
        tax_percentage = 0.1
    elif annual_salary <= 75000:
        tax_percentage = 0.2
    elif annual_salary <= 200000:
        tax_percentage = 0.25
    else:
        tax_percentage = 0.3
    if (annual_salary * tax_percentage ) > 75000:
        return 75000  
    return (annual_salary * tax_percentage)

def wheres_the_money(salary, mortgage, bills, food, travel):
    '''
    This function returns an organzied financial breakdown.
    Args:
        The arguments are numbers for the salary, mortgage, bills, food, and
        travel expenses.
    Returns: 
        The financial breakdown.
    '''
    # These are being used to calculate the percentages of each argument.
    mortgage_percentage = ((mortgage) * 12) / salary
    bills_percentage = ((bills) * 12) / salary
    food_percentage = ((food) * 52) / salary
    travel_percentage = (travel / salary)
    tax_percentage = (calculate_tax(salary)) / (salary)
    extra = salary - ((mortgage * 12)+ (bills * 12) + (food * 52) + travel +\
     calculate_tax(salary))
    extra_percentage =  extra / salary

    size = 0
    if (mortgage_percentage * 100) > size:
        size = (mortgage_percentage * 100)
    if (bills_percentage * 100) > size:
        size = (bills_percentage * 100)
    if (food_percentage * 100) > size:
        size = (food_percentage * 100)
    if (travel_percentage * 100) > size:
        size = (travel_percentage * 100)
    if (tax_percentage * 100) > size:
        size = (tax_percentage * 100)
    if (extra_percentage * 100) > size:
        size = (extra_percentage * 100)
    
    print("------------------------------------------" + "-" * int(size))
    
    print("See the financial breakdown below, based on a salary of $" + \
    str(salary)) 

    print("------------------------------------------" + "-" * int(size))
    
    print("| mortgage/rent | $" +'{:11,.2f}'.format((mortgage * 12)) + \
    " |  " + '{:4.1f}'.format((mortgage_percentage * 100)) + "%" + " | " + \
    ("#" * int(mortgage_percentage * 100)))
    print("|         bills | $" + '{:11,.2f}'.format((bills * 12)) + \
    " |  " + '{:4.1f}'.format((bills_percentage * 100)) + "%" + " | " + \
    ("#" * int(bills_percentage * 100)))
    print("|          food | $" + '{:11,.2f}'.format((food * 52)) + \
    " |  " + '{:4.1f}'.format((food_percentage * 100)) + "%" + " | " + \
    ("#" * int(food_percentage * 100)))
    print("|        travel | $" + '{:11,.2f}'.format((travel)) + " |  " + 
    '{:4.1f}'.format((travel_percentage * 100)) + "%" + " | " + \
    ("#" * int(travel_percentage * 100)))
    print("|           tax | $" + '{:11,.2f}'.format((calculate_tax(salary)))\
    + " |  " + '{:4.1f}'.format((tax_percentage * 100)) + "%" + " | " + \
    ("#" * int(tax_percentage * 100 )))
    print("|         extra | $" + '{:11,.2f}'.format((extra)) + " |  " + \
    '{:4.1f}'.format((extra_percentage * 100)) + "%" + " | " + \
    ("#" * int(extra_percentage * 100)))
    print("------------------------------------------" + "-" * int(size))
    
    total = mortgage + bills + food + travel 
    if calculate_tax(salary) >= 75000:
        print('>>> TAX LIMIT REACHED <<<')
    if extra < 0:
        print('>>> WARNING: DEFICIT <<<')

wheres_the_money(300000, 3000, 500, 500, 50000)
