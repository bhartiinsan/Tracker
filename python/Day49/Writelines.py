

file = open('players.txt', 'w')
li = ['sachin\n', 'viru\n', 'virat\n']
file.writelines(li)
print('done')
file.close()

# Naya concept — writelines()

# write() vs writelines():

# +----------+------------------------+----------------------------------+
# |          |       write()          |         writelines()             |
# +----------+------------------------+----------------------------------+
# | Input    |    Single string       |       List of strings            |
# | \n       |    Manually dalo       |   Manually dalo (auto nahi)      |
# | Example  | file.write('sachin\n') | file.writelines(['sachin\n',     |
# |          |                        |  'viru\n', 'virat\n'])           |
# +----------+------------------------+----------------------------------+


#===============================================================================================

# Flow:

# Step                    Code                     Kya hua
# 1                     open('w')               File khuli, purana data DELETE
# 2                     li = [...]              List bani 3 strings ke saath
# 3                     writelines(li)          Teeno strings ek saath file me likhi
# 4                     print('done')           done print hua5close()File band