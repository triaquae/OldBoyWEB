from django import template

register = template.Library()

@register.simple_tag
def convert_img_src(img_url):
    #if img_url.startswith("statics"):
    #print(img_url.name,dir(img_url))
    img_url = img_url.name.replace("statics","static")
    return img_url

