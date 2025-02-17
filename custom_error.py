class UserNameNonCharError(ValueError):
    """Raised when username does not contain at least one letter."""
    def __init__(self, message="Username must contain at least one letter."):
        super().__init__(message)

class UserNameTooShortError(ValueError):
    """Raised when username is shorter than 4 characters."""
    def __init__(self, message="Username must be at least 4 characters long."):
        super().__init__(message)

class IllegalEmailFormatError(ValueError):
    """Raised when the email format is invalid."""
    def __init__(self, message="Email must contain '@' and at least one period ('.')."):
        super().__init__(message)

class IllegalPasswordFormatError(ValueError):
    """Raised when the password does not meet the required complexity."""
    def __init__(self, message="Password does not meet complexity requirements."):
        super().__init__(message)

class IllegalBirthdayError(ValueError):
    """Raised when the birthday is in the future."""
    def __init__(self, message="Birthday must be in the past."):
        super().__init__(message)

class UserTooYoungError(ValueError):
    """Raised when the user is under 20 years old."""
    def __init__(self, message="User must be at least 20 years old."):
        super().__init__(message)
