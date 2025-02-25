VALIDATION_MESSAGES = {
    "accepted": "The {attribute} must be accepted.",
    "accepted_if": "The {attribute} must be accepted when {other} is {value}.",
    "active_url": "The {attribute} is not a valid URL.",
    "after": "The {attribute} must be a date after {date}.",
    "after_or_equal": "The {attribute} must be a date after or equal to {date}.",
    "alpha": "The {attribute} must only contain letters.",
    "alpha_dash": "The {attribute} must only contain letters, numbers, dashes and underscores.",
    "alpha_num": "The {attribute} must only contain letters and numbers.",
    "array": "The {attribute} must be an array.",
    "ascii": "The {attribute} must only contain single-byte alphanumeric characters and symbols.",
    "before": "The {attribute} must be a date before {date}.",
    "before_or_equal": "The {attribute} must be a date before or equal to {date}.",
    "between": {
        "array": "The {attribute} must have between {min} and {max} items.",
        "file": "The {attribute} must be between {min} and {max} kilobytes.",
        "numeric": "The {attribute} must be between {min} and {max}.",
        "string": "Please enter the {attribute} in [{min} and {max}] characters or less."
    },
    "boolean": "The {attribute} field must be true or false.",
    "confirmed": "The {attribute} confirmation does not match.",
    "current_password": "The password is incorrect.",
    "date": "The {attribute} is not a valid date.",
    "email": "The {attribute} must be a valid email address.",
    "image": "The {attribute} must be an image.",
    "integer": "The {attribute} must be an integer.",
    "numeric": "The {attribute} must be a number.",
    "required": "The {attribute} field is required.",
    "unique": "The {attribute} has already been taken.",
    "regex": "The {attribute} format is invalid.",
    "password": {
        "nullable": "Password cannot be empty.",
        "min": "Password must contain at least 8 characters.",
        "confirmed": "Confirm password not correct."
    },
    "name": {
        "required": "Name is required.",
        "unique": "Name must be unique.",
        "max": "Name cannot be longer than 255 characters.",
        "regex": "The {attribute} must only contain letters and numbers.",
        "regex_space": "The {attribute} must only contain letters, numbers, and spaces."
    },
    "telephone": {
        "regex": "The {attribute} format is invalid."
    },
    "fax": {
        "regex": "The {attribute} format is invalid."
    },
    "database": {
        "exists": "The {attribute} value does not exist in database {database}."
    }
}
