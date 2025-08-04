from django.db import models
from django.utils.translation import gettext_lazy as _


class SubscriptionStatus(models.TextChoices):
    ACTIVE = "active", _('Active')
    CANCELLED = "cancelled", _('Cancelled')
    EXPIRED = "expired", _('Expired')


class CurrencyUnit(models.TextChoices):
    USD = 'USD', _('US Dollar')
    EUR = 'EUR', _('Euro')
    BDT = 'BDT', _('Taka')
