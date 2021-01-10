#!/usr/local/bin/python3
# Made by @swisscoding on Instagram

from colored import stylize, fg
import hashlib

# decoration
print(stylize("\n---- | Password hash comparison (Database) | ----\n", fg("red")))

# Database (visible for Instagram post)
database = {
    "swisscoding": "02084a76222d1af7424bb496ad3c6f2f35065eeb54ab22328defbb289f792787",
    "swisscodingassistant": "247ddf07e2b3d45e2bbeda35fb34b38bd4dc398638b16eaa63a4254addacc7e1" # try to crack ;)
}

# class
class PasswordHash:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # output magic method
    def __repr__(self):
        self.hashed_pw = self.hash(self.password)
        if database[self.username] == self.hashed_pw:
            return stylize(f"\nPassword \"{self.password}\" for user \"{self.username}\" is identical\nwith the password in the database.\n", fg("green"))
        return stylize(f"\nPassword \"{self.password}\" for user \"{self.username}\" is wrong.\n", fg("red"))

    # method
    def hash(self, s):
        # encode
        input_encoded = s.encode("utf-8")
        # hash with sha256
        input_hashed = hashlib.sha256(input_encoded).hexdigest()

        return input_hashed


# main execution
if __name__ == "__main__":
    # user interaction
    username = input("Username: ").lower()
    password = input("Password: ")

    if not username in database.keys():
        exit("\nUsername is not in the database.\n")
    print(PasswordHash(username, password))
