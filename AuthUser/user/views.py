from rest_framework.response import Response
from rest_framework.decorators import api_view
from cryptography.fernet import Fernet

@api_view(['POST'])
def authenticate(request):
    encrypted = request.data.get('encrypted')
    secret_key = request.data.get('secret_key')
    image = request.FILES.get('image')

    # Decrypt the encrypted data
    cipher_suite = Fernet(secret_key.encode())
    decrypted_data = cipher_suite.decrypt(encrypted.encode())

    # Extract username length from the first 4 bytes of the decrypted data
    username_length = int.from_bytes(decrypted_data[:4], 'big')

    # Extract username and token based on the username length
    username = decrypted_data[4:4 + username_length].decode()
    token = decrypted_data[4 + username_length:].decode()

    print(username, token)

    return Response({"message": "Data received successfully"})
