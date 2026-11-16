"""Synthetic module for the TODO/FIXME audit sandbox."""


def calculate_total(items):
    # TODO: validate that prices are non-negative
    total = sum(item["price"] for item in items)
    # FIXME: handle empty items and missing "price" key
    return total


class StatusType:
    # This enum value is not a marker, even though the identifier is TODO.
    TODO = "todo"
    DONE = "done"


NOT_A_MARKER = "TODO: this is a string literal, not a comment"
