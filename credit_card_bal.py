balance = 999999
#setting variables
annualInterestRate = 0.18
MinMonthlyPayment = 0
new_balance = balance
count = 0
interest_rate = (annualInterestRate)/12.0
lower_bound = balance / 12
upper_bound = (balance * (1 + interest_rate)*12) / 12.0

while round(new_balance,0) != 0:
   
    MinMonthlyPayment = (lower_bound + upper_bound)/2
        
    new_balance = balance
    old_balance = balance
    print(MinMonthlyPayment)
    print(new_balance)
    for n in range(12):
        MonthlyInterestRate= (annualInterestRate) / 12.0
        MonUnpaidBal = (old_balance) - (MinMonthlyPayment)
        UpdatedMonthlyBal = MonUnpaidBal + (MonthlyInterestRate * MonUnpaidBal)
        old_balance = UpdatedMonthlyBal
        print(UpdatedMonthlyBal)
        count += 1    
#        if UpdatedMonthlyBal <= 0:
#            break
    new_balance = UpdatedMonthlyBal
    print(new_balance)
    if new_balance > 0:
        lower_bound = MinMonthlyPayment
    elif new_balance < 0:
        upper_bound = MinMonthlyPayment
        
print("Total no. of iterations: " + str(count))    
print("Minimum monthly payment: " + str(round(MinMonthlyPayment,2)))