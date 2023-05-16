import hashlib

stored_hash = "6B8C22651B3089DDA5A0D48A5E586C0F5DE6A7A1"
salt = bytes.fromhex("64894AA6")

# Specify the possible encodings to try
encodings = ["utf-8", "latin-1", "windows-1252"]

# Iterate through each encoding and attempt to open the file
for encoding in encodings:
    try:
        with open("passwords.txt", "r", encoding=encoding) as file:
            passwords = file.readlines()
        break
    except UnicodeDecodeError:
        continue
else:
    print("Failed to decode the file with any available encoding.")
    exit(1)

# Iterate through each password in the file
for password in passwords:
    # Remove newline characters from the password
    password = password.strip()

    # Create a new SHA-1 hash object for each password
    hash_algorithm = hashlib.sha1()

    # Concatenate the salt and the candidate password
    hash_algorithm.update(salt + password.encode("utf-8"))

    # Obtain the resulting hash in hexadecimal format
    hashed_password = hash_algorithm.hexdigest()

    # Compare the hashed password with the stored hash
    if hashed_password == stored_hash:
        print(f"Password found: {password}")
        break
    else:
        print(f"Password {password} is not a match.")

else:
    print("Password not found.")
