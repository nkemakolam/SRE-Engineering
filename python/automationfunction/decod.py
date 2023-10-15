
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

def decode_string_with_password(encoded_data, password):
    try:
        fernet_key = generate_fernet_key_from_password(password)
        decoded_data = fernet_key.decrypt(encoded_data).decode()
        return decoded_data
    except Exception as e:
        print(f"Error: {str(e)}")
        return None



# Example usage:
data_to_decode = b'gAAAAABlJou3AtJniRoGHmLDwtMiQCEk0BK31qqR9sq7ecdjrmdE6_l2Abcd77XNmClPkBI78w8PcInrYRfRghkiIpbxVtlZJBjdxvhdSrIg2V_WdnOUY37uBGZMBhF1asYWeK62OnCW'
password = "Unicef01!*"

decoded_data = decode_string_with_password(data_to_decode, password)
print("Decoded Data:", decoded_data)
