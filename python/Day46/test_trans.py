# from deep_translator import GoogleTranslator
# text = "Hello, how are you?"
# translated_text = GoogleTranslator(source='en', target='es').translate(text)
# print(translated_text)

# from deep_translator import GoogleTranslator

# text = "Hello, how are you?"
# translated_text = GoogleTranslator(source='en', target='hi').translate(text)
# print(translated_text)

from deep_translator import GoogleTranslator
t= GoogleTranslator(source="auto", target="hi")   
text= input("enter text=")
res = t.translate(text)
print(res)

#====================================
# var.method()
# var is object of class and method is function defined in that class
