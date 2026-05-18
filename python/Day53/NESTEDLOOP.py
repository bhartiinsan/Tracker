def show():                    #top level(outer) fun
    print('this is show')
    def disp():                #nested(inner) fun
        print('this is disp')
    
    disp()

show()


# # show()          ← outer/top level function
# │
# ├── print('this is show')
# # │
# ├── disp()      ← inner/nested function (defined INSIDE show)
# │   └── print('this is disp')
# │
# └── disp()      ← disp ko yahan call kiya


# +----------------------------------------+
# | disp() sirf show() ke ANDAR call hogi  |
# | show() ke BAHAR disp() call → ERROR ❌ |
# +----------------------------------------+