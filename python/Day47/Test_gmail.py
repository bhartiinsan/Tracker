#Bharti
#Password Generator
# unvn rhfq ueel pylz

# from gmail import GMail ,Message
# con=GMail("Bhartii1017@gmail.com", "unvn rhfq ueel pylz")

# to_mail= input("Enter  to mail address: ")
# subject= input("Enter subject: ")
# body= input("Enter body: ")

# msg=Message( to= to_mail, subject= subject , text= body,)
# con.send(msg)
# print("Mail sent successfully")

##=============================================================================================

#  attachments= "C:/Users/BHARTI/Downloads/py.jpg"

# WHEN WE HAVE TO SEND A MAIL WITH ATTACHMENT THEN WE HAVE TO USE THIS CODE
# THE CODE IS 
from gmail import GMail ,Message
con=GMail("Bhartii1017@gmail.com", "unvn rhfq ueel pylz")
to_mail= input("Enter  to mail address: ")
subject= input("Enter subject: ")   
body= input("Enter body: ")
attachments= "C:/Users/BHARTI/OneDrive/Desktop/cat_download.jfif"
msg=Message( to= to_mail, subject= subject , text= body, attachments= attachments)
con.send(msg)


# Cats are fascinating and independent animals known for their playful and curious nature. They love cozy spaces, soft cushions, and warm sunlight, often spending hours napping peacefully. Most cats enjoy chasing toys, especially moving objects like strings or laser lights. Their favorite foods usually include fish, chicken, and specially prepared cat food. Cats communicate through meows, purring, 
# and body language, showing affection in subtle ways. 
# # aditya25datascience@gmail.com, dukeprofessional@gmail.com