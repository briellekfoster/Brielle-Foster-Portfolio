'''
Brielle Foster
CSC110
Project -4
This program is calculating how many months it will take to save enough money
to make a downpayment while increasing the salary every 6 months.
'''
def calculate_months(annual_salary, portion_saved, total_cost,\
 semi_annual_raise):
    '''
    This function returns the amount of months.
    Args:
        The arguments are the annual salary, portion saved, total cost
        and the semi annual raise which are needed to find out how many
        months it will take to make the downpayment.
    Returns: 
        The months.
    '''
    portion_down_payment = 0.25 * total_cost
    current_savings = 0
    r = 0.04
    months = 0
    while current_savings < portion_down_payment:
        current_savings += current_savings * r/12
        current_savings += portion_saved * (annual_salary/12)
        months += 1
        # This if statement is being used to make sure that the salary only 
        # increases every 6 months
        if months % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise
    return months