# #SINGLE BALEL INHERITANCE
# class telephone:
#     def voice_call(self):
#         print(" thios is a voice call")

# class mobile(telephone):
#     def text_msg(self):
#         print(" this is test msg")

# obj=mobile()
# obj.voice_call()
# obj.text_msg()

#=====================================================
# MULTI-LEVEL INHERITANCE
class telephone:
    def voice_call(self):
        print(" thios is a voice call")

class mobile(telephone):
    def text_msg(self):
        print(" this is test msg")

class smartphone(mobile):
    def vdc_call(self):
        PermissionError(" this is a vdc")

obj=mobile()
obj.voice_call()
obj.text_msg()
obj.vdc_call()
