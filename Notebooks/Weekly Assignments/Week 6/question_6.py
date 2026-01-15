"""
Decrypt a message encrypted by hide_message function.
"""
def decrypt_message(encrypted, interval):
    return ''.join(encrypted[i] for i in range(0, len(encrypted), interval))

encrypted_msg = "sghpejafnlcjdntsckkhhtgterfhegzqsataellz"
interval = 4

print(decrypt_message(encrypted_msg, interval))
