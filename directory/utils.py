import re

class EmailValidatorMixin(object):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    def validate_email(self, regex=None, email=None):
        if email is not None:
            regx = self.regex if regex is None else regex
            return re.search(regx,email)
        return False


class FilterMixin(object):

    @property
    def filter_dict(self):
        raise NotImplementedError("filter_dict is not implemented")

    def get_filter_dict(self):
        return self.filter_dict.items()

    def get_filters(self):
        qs_filter_set = {}
        for filtr, filter_meta in self.get_filter_dict():
            qry = self.request.GET.get(filtr, "")
            if qry:
                fltr_method = filter_meta.get("method", "")
                if filter_meta.get("method", ""):
                    qry = fltr_method(qry)
                qs_filter_set.update({filter_meta["lookup"]:qry})

        return qs_filter_set

def trim_str(count):
    def trim(strng):
        return strng.strip()[:count]
    return trim
