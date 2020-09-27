from django.utils import timezone
from django import template

register = template.Library()


@register.filter
def minutes_ago(time, minutes):
    return time + timezone.timedelta(minutes=minutes) > timezone.now()


@register.filter
def days_ago(time, days):
    return time + timezone.timedelta(days=days) < timezone.now()
