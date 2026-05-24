#multiple inheritance
class telephone:
    def voice_call(self):
        print('this is voice call')

class camera:
    def picture(self):
        print('this is picture')

class mobile(telephone, camera):
    def msg(self):
        print('this is msg')

obj = mobile()
obj.voice_call()
obj.picture()
obj.msg()