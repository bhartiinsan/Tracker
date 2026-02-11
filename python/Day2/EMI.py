# Step 1: Take input from user
loan = float(input("Enter loan amount: "))
rate = float(input("Enter annual interest rate (%): "))
years = int(input("Enter loan tenure (years): "))

# Step 2: Convert annual rate → monthly rate
monthly_rate = rate / 12 / 100

# Step 3: Convert years → months
months = years * 12

# Step 4: Apply EMI formula
emi = (loan * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)

# Step 5: Show result
print("\nLoan Details")
print("Loan Amount:", loan)
print("Interest Rate:", rate, "%")
print("Tenure:", years, "years")
print("Monthly EMI:", round(emi, 2))
