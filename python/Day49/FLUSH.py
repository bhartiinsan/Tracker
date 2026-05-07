file = open('players.txt', 'w')    #create or replace
file.write('sachin\n')
file.flush()
file.write('viru\n')
file.close()
print('done')






# ##===============================================================================================
# Short Summary:

# 'w' = write mode → create or replace
# write() = data likhta hai, \n khud dalo
# flush() = buffer ko forcefully disk pe likh do
# close() = flush + file band (isliye normally flush() ki zarurat nahi)