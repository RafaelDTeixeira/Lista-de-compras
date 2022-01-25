from django import template

register = template.Library()

@register.filter
def multiplica(value, arg):
    return value*arg