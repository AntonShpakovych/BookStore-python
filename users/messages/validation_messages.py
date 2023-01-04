EMAIL = """ Should not be not empty. Has a localpart on the left of an @,
                    the domain on the right. Neither the localpart nor the domain can be empty.
                    The localpart can consist of labels separated by dots but it cannot have two successive dots,
                    nor can it start or end with a dot. Labels consist of a-z, A-Z, 0-9, or one of !#$%&'*+-/=?^_`{|}~.
                    Labels must be less than 63 characters. Labels must not start with a hyphen, end with a hyphen,
                    or contain two successive hyphens. The right-most label must be all alphabetic."""
PASSWORD = """Minimum 8 letters, at least 1 uppercase, at least 1 lowercase,
              at least 1 number. Mustn't contain spaces inside. Spaces at the beginning and at the end should be cut off."""
PASSWORD_MISSMATCH = "The two password fields didn't match."
ADDRESS_FIRST_NAME = "Cannot be not empty. Must consist of only a-z and A-Z characters without special symbols. Must be less than 50 characters."
ADDRESS_LAST_NAME = "Should not be not empty. Consist of a-z, A-Z only, no special symbols. Must be less than 50 characters."
ADDRESS_ADDRESS = "Should not be not empty. Consist of a-z, A-Z, 0-9,’,’, ‘-’, ‘ ’ only, no special symbols. Must be less than 50 characters."
ADDRESS_CITY = "Should not be not empty. Consist of a-z, A-Z only, no special symbols. Must be less than 50 characters."
ADDRESS_ZIP = "Should not be empty. Consist of 0-9 only,’-’ no special symbols. Max Length should be 10 characters."
ADDRESS_PHONE = "Should not be empty.Plus (+) at the beginning.After should contain country code of chosen country in Country drop down list. Consist of 0-9 only no special symbols. Must be 15 characters or less."
