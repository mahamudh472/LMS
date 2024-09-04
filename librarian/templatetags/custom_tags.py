from django import template
from django.db.models import ManyToOneRel, ManyToManyRel, OneToOneRel

register = template.Library()

@register.filter
def get_fields(obj):
    # Filter out relationship fields
    return [
        (field.verbose_name, field.value_from_object(obj))
        for field in obj._meta.get_fields()
        if not isinstance(field, (ManyToOneRel, ManyToManyRel, OneToOneRel))
    ]
