from django.core.exceptions import ValidationError


def min_length_validator(value):
    if len(value) != 16:
        raise ValidationError("length is not 16")