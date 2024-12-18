import hashlib

def crack_sha1_hash(hash_to_crack, use_salts=False):
    # Load the password file
    with open("top-10000-passwords.txt", "r") as password_file:
        passwords = [line.strip() for line in password_file]
    
    # If salts are used, load them
    salts = []
    if use_salts:
        with open("known-salts.txt", "r") as salt_file:
            salts = [line.strip() for line in salt_file]
    
    # Check each password
    for password in passwords:
        # Compute hash without salts
        if hashlib.sha1(password.encode()).hexdigest() == hash_to_crack:
            return password
        
        # Compute hash with salts if use_salts is True
        if use_salts:
            for salt in salts:
                # Prepend salt
                salted_password = salt + password
                if hashlib.sha1(salted_password.encode()).hexdigest() == hash_to_crack:
                    return password
                
                # Append salt
                salted_password = password + salt
                if hashlib.sha1(salted_password.encode()).hexdigest() == hash_to_crack:
                    return password
    
    # If no match found
    return "PASSWORD NOT IN DATABASE"
