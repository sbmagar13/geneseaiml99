from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import re


def validate_MAC(value):
    pattern = re.compile(
        "^(([a-fA-F0-9]{2}-){5}[a-fA-F0-9]{2}|([a-fA-F0-9]{2}:){5}[a-fA-F0-9]{2}|([0-9A-Fa-f]{4}\.){2}[0-9A-Fa-f]{4})?$")
    if not pattern.match(value):
        raise ValidationError(_("Not Valid MAC Address"))
    return value
