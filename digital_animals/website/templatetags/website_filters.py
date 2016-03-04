from datetime import datetime

from django import template

register = template.Library()


@register.filter
def interpolate(value, arg):
    return value % arg


@register.filter
def interpolate_with_timeline(value, start_year):
    current_year = str(datetime.now().year)

    if start_year != current_year:
        timeline = ''.join([start_year, ' - ', current_year])
    else:
        timeline = current_year

    return value % timeline


@register.filter
def sift_digits(value):
    return ''.join(i for i in value if i.isdigit())
