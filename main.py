from User import User
from datetime import datetime
import CustomError as ce

def main():
          user_data = [
          {"name": "Joe", "email": "joe@example.com", "password": "Weak1!",
           "birthday": datetime(2005, 5, 15)},
          {"name": "1234", "email": "valid@example.com", "password": "Strong1@",
           "birthday": datetime(1995, 6, 10)},
          {"name": "ValidUser", "email": "invalidemail.com", "password": "Strong1@",
           "birthday": datetime(1995, 6, 10)},
          {"name": "ValidUser", "email": "valid@example.com", "password": "Valid1@",
           "birthday": datetime(1995, 6, 10)},
          {"name": "ValidUser", "email": "valid@example.com", "password": "weakpass",
           "birthday": datetime(1995, 6, 10)},
          {"name": "ValidUser", "email": "valid@example.com", "password": "WEAKPASS",
           "birthday": datetime(1995, 6, 10)},
          {"name": "ValidUser", "email": "valid@example.com", "password": "Weakpass",
           "birthday": datetime(1995, 6, 10)},
         {"name": "ValidUser", "email": "valid@example.com", "password": "Weakpass@",
          "birthday": datetime(1995, 6, 10)}

     ]

     for data in user_data:
          try:
               user = User(data["name"], data["email"], data["password"], data["birthday"])
               print(f"Successfully created: {user}")
          except ce.UserNameTooShortError as e:
               print(f"Username Error: {e}")
          except ce.UserNameNonCharError as e:
               print(f"Username Error: {e}")
          except ce.IllegalEmailFormatError as e:
               print(f"Email Error: {e}")
          except ce.IllegalPasswordFormatError as e:
               print(f"Password Error: {e}")
          except ce.IllegalBirthdayError as e:
               print(f"Birthday Error: {e}")
          except ce.UserTooYoungError as e:
               print(f"Age Restriction Error: {e}")
          except Exception as e:
               print(f"Unexpected Error: {e}")

if __name__ == "__main__":
     main()
