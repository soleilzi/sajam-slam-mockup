from django import template
from django.contrib.staticfiles import finders

register = template.Library()

@register.filter(name='get_image')
def get_image(filename):
    formats = ['png', 'jpg', 'jpeg']
    for fmt in formats:
        image_path = f"images/people/{filename}.{fmt}"
        if finders.find(image_path):
            return image_path
    return "images/people/default.png"