"""Legacy helpers with real markers for the audit."""


def parse_expression(value):
    # TODO(security): replace eval with a safe parser before production
    return eval(value)


def normalize_name(name):
    # FIXME: handle None and non-string values
    return name.strip().lower()
