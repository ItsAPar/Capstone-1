###Importing maths module for later in the program
import math


###Requesting user input for whether they want an investment or bond calculation
user_choice=input("Choose either 'investment' or 'bond' from the menu below to proceed\n \ninvestment - to calculate the amount of interest you'll earn on your investment\nbond       - to calculate the amount you'll have to pay on a home loan\n\n")
user_choice=str.lower(user_choice)


###Checking if the user choice is investment or bond and then requesting the relevant inputs from the user 
if user_choice == 'investment':
    money_quant=int(input("How much money are you depositing? "))
    int_rate=int(input("What is the interest rate (do not include %) "))
    time_span=int(input("How many years are you investing for? "))
    interest=(input("Would you like simple or compound interest? (simple/compound) "))
    interest=str.lower(interest)
    int_rate_decimal=int_rate/100
elif user_choice == 'bond':
    house_value=int(input("What is the current value of the house "))
    interest_rate=int(input("What is the interest rate? (Anual) "))
    repayment_duration=int(input("How many months do you plan to take to repay the bond? "))
    m_interest_rate=interest_rate/12
else:
    print('We were unable to process your choice, sorry.')


###Checking if the user choice is simple or compound and doing the relevant calculations
if user_choice == 'investment':
    if interest == 'simple':
        final_amount=money_quant*(1+int_rate_decimal*time_span)
        print(f"Your total ammount is: {final_amount}")
    elif interest == 'compound':
        final_amount=money_quant*math.pow((1+int_rate_decimal),time_span)
        print(f"Your total ammount is: {final_amount}")
    else:
        print("We couldnt figure out your choice for simlpe or compound interest. ")


###For this section i could not get the provided formula as the (i.P) section wouldnt recognise the P as a variable and i am unsure what the period does in the calculation. 
###To work and another one that i tester was returning the wrong values so the one i have ended up using i am unsure if it is correct or not
###I have left the attempts in comments underneath the working calculation
elif user_choice == 'bond':
    rate_month=interest_rate/100./12.
    term=(1+rate_month)**repayment_duration
    monthly_repayment=house_value*rate_month*term/(term-1)
    ### monthly_repayment=(interest_rate/12)*(1/(1-(1+interest_rate/12)**(-repayment_duration)))*house_value
    ### monthly_repayment=(m_interest_rate.house_value)/(1-(1+m_interest_rate)^(-repayment_duration))
    print(f"The monthly repayment is: {monthly_repayment}.")
