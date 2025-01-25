import re
import CustomError as ce
from datetime import datetime
from dateutil.relativedelta import relativedelta

class User:
    def __init__(self, name: str, email: str, password: str,
                 birthday: datetime, created_at: datetime):

        self.name = name
        self.email = email
        self.password = password
        self.birthday = birthday
        self.__created_at = created_at

    @property
    def name(self): # getter
        return 'Fruit name is: ' + self.__name.upper()

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Username must be a string.")
        if len(value) < 4:
            raise ce.UserNameTooShortError()
        if not any(char.isalpha() for char in value):
            raise ce.UserNameNonCharError()
        self.__name = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if not isinstance(value, str):
            raise TypeError("Email must be a string.")
        if "@" not in value or "." not in value:
            raise ce.IllegalEmailFormatError()
        self.__email = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError("Password must be a string.")
        if len(value) < 8:
            raise ce.IllegalPasswordFormatError("Password must be at least 8 characters long.")
        if not re.search(r"[A-Z]", value):
            raise ce.IllegalPasswordFormatError("Password must contain at least one uppercase letter.")
        if not re.search(r"[a-z]", value):
            raise ce.IllegalPasswordFormatError("Password must contain at least one lowercase letter.")
        if not re.search(r"[~!@%$#^&*]", value):
            raise ce.IllegalPasswordFormatError("Password must contain at least one special character (~!@%$#^&*).")
        self.__password = value

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, value):
        if not isinstance(value, datetime):
            raise TypeError("Birthday must be a datetime object.")
        today = datetime.today().date()
        if value.date() >= today:
            raise ce.IllegalBirthdayError()
        age = relativedelta(today, value.date()).years
        if age < 20:
            raise ce.UserTooYoungError()
        self.__birthday = value

    @property
    def age(self):
        return relativedelta(datetime.today().date(), self.__birthday.date()).years

    @property
    def created_at(self):
        return self.__created_at

    def __str__(self) -> str:
        return (f"Product name:{self.__name} email:{self.__email} password:{self.__password} "
                f"birthdate:{self.__birthday} created_at:{self.__created_at} age:{self.age}")







