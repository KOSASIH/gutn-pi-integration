import cryptography
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

def encrypt_data(data, public_key):
    """
    Encrypt data using RSA encryption.

    Parameters:
    data (str): Data to be encrypted
    public_key (str): Public key

    Returns:
    str: Encrypted data
    """
    public_key = serialization.load_pem_public_key(public_key.encode(), backend=default_backend())
    encrypted_data = public_key.encrypt(data.encode(), padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    return encrypted_data.decode()

def decrypt_data(encrypted_data, private_key):
    """
    Decrypt data using RSA decryption.

    Parameters:
    encrypted_data (str): Encrypted data
    private_key (str): Private key

    Returns:
    str: Decrypted data
    """
    private_key = serialization.load_pem_private_key(private_key.encode(), password=None, backend=default_backend())
    decrypted_data = private_key.decrypt(encrypted_data.encode(), padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    return decrypted_data.decode()
