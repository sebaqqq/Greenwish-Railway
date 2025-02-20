from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def index(List, i):
    try:
        return List[int(i)]
    except (IndexError, ValueError, TypeError):
        return None