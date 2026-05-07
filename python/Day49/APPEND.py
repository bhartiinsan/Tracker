file = open('players.txt', 'a')    #create or append
file.write('rohit\n')
file.write('virat\n')
file.close()
print('done')





#===============================================================================================

# **`'w'` vs `'a'` — Most Important Difference:**

# | Condition |                  `'w'` (write) |                     `'a'` (append) |
# |-----------|--------------|----------------|
# | File exist **nahi** hai      | ✅ Nayi file banao |            ✅ Nayi file banao |
# | File exist **hai*           |   ❌ Purana content **DELETE** | ✅ Purana content **RAKH** ke end me add karo |
# | Cursor position                 | Position **0** (Start) |       Position **END** of file |