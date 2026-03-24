# LIST IS MUTUABLE- WE CAN ADD OR REMOVE ELEMENTS(MODIFY)
li=[10,20,30]
print(li)

# METHODS OF LIST
# FOR ONE ITEM
li.append(100)
print(li)

# FOR MULTIPLE VALUES
li.extend([100,200,300]) # ADD ALLL ELEMENTS IN THE LAST
print(li)

# FOR SPECIFIC INDEX
# shifting of elements
li.insert(1,25) # index, element
print(li)

#FOR REPLACING
li[0]=11      # assign/replace
print(li)

li[:2]=[101,102] # it assign to the first and second index , 2 is excluded
print(li)


