# Password Guessing Script

This script is designed to guess passwords by comparing them with a stored hash. It reads a list of passwords from a text file and performs a hash comparison to find a matching password.

## Usage

1. Ensure you have Python installed on your system. This script is compatible with Python 3.

2. Download the script file and the text file containing the list of passwords you want to test.

3. Open a terminal or command prompt and navigate to the directory where the script file is located.

4. Run the script by executing the following command:



```shell 
python password_sa.py
```


Note: Replace `password_sa.py` with the actual filename if you have renamed the script.

5. The script will attempt to open the text file, iterate through each password, and compare it with a stored hash. It will print a message for each password tested, indicating whether it is a match or not.

6. Once the script finishes running, it will display the result indicating whether a password match was found or not.

## Requirements

- Python 3.x

## File Structure

- `password_sa.py`: The main script file.
- `passwords.txt`: A text file containing the list of passwords to be tested.

## Hash example

```
FULL HASH:     0x010064894AA66B8C22651B3089DDA5A0D48A5E586C0F5DE6A7A1

Version: 0100 (SHA-1)

SALT: 64894AA6

Hash (20 bytes): 6B8C22651B3089DDA5A0D48A5E586C0F5DE6A7A1
```

## SQL Query to extract the Sa Hash

```SQL
SELECT name, CONVERT(VARCHAR(MAX), password_hash, 1) AS password_hash
FROM sys.sql_logins
WHERE name = 'sa';
```



## Troubleshooting

- If you encounter any issues, make sure you have the necessary permissions to access the files and that the file paths are correct.

## Disclaimer

This project is for educational purposes only. Please ensure that you have the necessary authorization and permissions before using this script. Password guessing or cracking activities may be subject to legal restrictions and should only be performed with proper authorization or for legitimate purposes, such as security testing or research.

Use this script responsibly and in accordance with the applicable laws and regulations in your jurisdiction.

## License

This project is licensed under the [MIT License](LICENSE). Please see the `LICENSE` file for more details.
