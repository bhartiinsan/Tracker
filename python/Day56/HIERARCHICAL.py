#hierarchical
class person:
    def eating(self):
        print('this is eating')

    def thinking(self):
        print('this is thinking')

class student(person):
    def study(self):
        print('this is study')

class actor(person):
    def acting(self):
        print('this is acting')

s=student()
s.thinking()
s.eating()
s.study()

a=actor()
a.thinking()
a.eating()
a.acting()


# DIAGRAM

#          person
#         (eating)
#        (thinking)
#         /       \
#        /         \
#   student        actor
#   (study)       (acting)







# +------+---------------+----------------+------------------+
# | Step |     Code      |  Dhundha kahan |     Output       |
# +------+---------------+----------------+------------------+
# |  1   | s.thinking()  | student❌→     | this is thinking |
# |      |               | person✅       |                  |
# |  2   | s.eating()    | student❌→     | this is eating   |
# |      |               | person✅       |                  |
# |  3   | s.study()     | student✅      | this is study    |
# |  4   | a.thinking()  | actor❌→       | this is thinking |
# |      |               | person✅       |                  |
# |  5   | a.eating()    | actor❌→       | this is eating   |
# |      |               | person✅       |                  |
# |  6   | a.acting()    | actor✅        | this is acting   |
# +------+---------------+----------------+------------------+

##=========================================================================

# +---------------+------------------+----------------------+
# |     Type      |    Structure     |      Example         |
# +---------------+------------------+----------------------+
# | Single        | A → B            | person → student     |
# | Multiple      | A,B → C          | telephone,camera→    |
# |               |                  | mobile               |
# | Multilevel    | A → B → C        | A→B→D (chain)        |
# | Hierarchical  | A → B            | person → student     |
# |               | A → C            | person → actor ✅    |
# | Hybrid        | Mix of above     | Multiple+Multilevel  |
# +---------------+------------------+----------------------+