# import hashlib
import hashlib

def hash_password(password):

    #create an object for MD-5

    hasher = hashlib.md5()
    #encode the password

    hasher.update(password.encode('utf-8'))

    #create a hexadecimal representation of the password

    hashed_password = hasher.hexdigest()
    return hash_password

    

# def hash_password_salt(password):
    