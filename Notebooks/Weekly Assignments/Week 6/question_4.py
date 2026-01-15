"""
Encrypt a message by removing spaces and reversing the string.
"""
def encrypt_message(message):
    no_spaces = message.replace(" ", "")
    return no_spaces[::-1]  

print(encrypt_message("my name is Sadiksha"))   
print(encrypt_message("data science is fun"))   
print(encrypt_message("python programming"))    
 
  
