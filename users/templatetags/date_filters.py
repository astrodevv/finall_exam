from datetime import timedelta
from django import template
from datetime import datetime

register = template.Library()

@register.filter
def date_add(value, days):

    try:
        value = datetime.strptime(value, "%d.%m.%Y")
        new_date = value + timedelta(days=int(days))
        return new_date.strftime("%d.%m.%Y") 
    except (ValueError, TypeError):
        return value
