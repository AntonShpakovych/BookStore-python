from django import template
from shop.models import Category

register = template.Library()


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def get_category(id):
    return Category.objects.get(id = id)
