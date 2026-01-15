"""
Encrypt a message by spacing letters randomly with random letters in between.
Returns encrypted message and the interval used.
"""
import random
import string

def hide_message(message):
    interval = random.randint(2, 20)
    message = message.replace(" ", "")  
    encrypted = ""
    for char in message:
        encrypted += char
        encrypted += ''.join(random.choice(string.ascii_lowercase) for _ in range(interval - 1))
    return encrypted, interval

encrypted_msg, interval = hide_message("send cheese")
print(encrypted_msg)
print("Interval:", interval)
