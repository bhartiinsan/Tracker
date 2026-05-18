class calculator:
    x=3
    y=4

    @classmethod                            # possible but not recommended
    def add(cls):
        print(calculator.x+calculator.y)

    @classmethod                            # recommended way to access class data
    def mul(cls):
        print(cls.x+cls.y)

calculator.add() # calc.add (calc)

calculator.mul() #calc.mul (calc)