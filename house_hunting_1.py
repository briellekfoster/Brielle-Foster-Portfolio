'''
Brielle Foster
CSC110
Project -4
This program is calculating how many months it will take to save enough money
to make a downpayment.
'''
def calculate_months(annual_salary, portion_saved, total_cost):
    '''
    This function returns the amount of months.
    Args:
        The arguments are the annual salary, portion saved, and total cost
        which are needed to find out how many months it will take to make
        the downpayment.
    Returns: 
        The months.
    '''
    # This is being used to calculate the portion down payment.
    portion_down_payment = 0.25 * total_cost
    current_savings = 0
    r = 0.04
    months = 0
    while current_savings < portion_down_payment:
        current_savings += current_savings*r/12
        current_savings += portion_saved * (annual_salary/12)
        months += 1
    return months

