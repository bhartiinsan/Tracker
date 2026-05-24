#method overriding

class parent:
    def study(self):
        print('books & teachers')

class child(parent):
    def study(self):
        print('chatgpt,youtube,etc.')

obj=child()
obj.study()

class parent:
    def study(self):
        print('books & teachers')

class child(parent):
    def study(self):
        print('chatgpt,youtube,etc.')
        super().study()

obj=child()
obj.study()