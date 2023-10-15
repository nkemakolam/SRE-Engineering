import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

def generate_fernet_key_from_password(password, salt=b"salt"):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,
        salt=salt,
        length=32
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return Fernet(key)

def encode_string_with_password(data, password):
    try:
        fernet_key = generate_fernet_key_from_password(password)
        encoded_data = fernet_key.encrypt(data.encode())
        return encoded_data
    except Exception as e:
        print(f"Error: {str(e)}")
        return None
# Example usage:
data_to_encode = "This is a secret message."


password = "uniceftest"

# Encode the data
encoded_data = encode_string_with_password(data_to_encode, password)
print("Encoded Data:", encoded_data)
