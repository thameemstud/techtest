import re

class EmailValidatorMixin(object):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    def validate_email(self, regex=None, email=None):
        if email is not None:
            regx = self.regex if regex is None else regex
            return re.search(regx,email)
        return False