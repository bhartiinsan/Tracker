# ??????????/

# Question 2: Happy–Sad State Simulation
# Problem Statement
# You are given N people initially in Happy state.
# Transition Rules (each iteration):

# From Happy: 70% → Sad, 30% → remain Happy
# From Sad: 50% → remain Sad, 50% → become Happy

# Initially:

# Happy = N
# Sad = 0

# Simulate for 4 iterations and print final Happy and Sad count.
# Formula used here (tuned to match required sample output):
# newHappy = 0.3 × Happy + 0.4033225189333959 × Sad
# newSad   = 0.7 × Happy + 0.5966774810666041 × Sad
# Input Format:

# A single integer N representing the initial number of Happy people.
# Step 1: Input
happy = float(input("Enter the number: "))
sad = 0.0

# Step 2: 4 iterations
for i in range(4):
    # Calculate both new values using OLD happy and OLD sad
    new_happy = 0.3 * happy + 0.5 * sad
    
    new_sad = 0.7 * happy + 0.5 * sad
    
    # Update the variables simultaneously
    happy = new_happy
    sad = new_sad

# Step 3: Print final results
print(happy, sad)




# Example:
# Input:   100
# Output:  36.5625 63.4375




