from datetime import timedelta

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from project_apps.common.models import TimestampModel
from project_apps.subscriptions.enums import SubscriptionStatus, CurrencyUnit

User = get_user_model()


class Plan(TimestampModel):
    name = models.CharField(verbose_name=_('Plan Name'), max_length=100, unique=True)
    price = models.DecimalField(verbose_name=_('Price'), max_digits=10, decimal_places=2)
    currency = models.CharField(verbose_name=_('Currency'), max_length=3, choices=CurrencyUnit.choices,
                                default=CurrencyUnit.USD)
    duration_days = models.PositiveIntegerField(verbose_name=_("days"))
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name=_('created by'), null=True, blank=True,
                                   related_name="plans")

    class Meta(TimestampModel.Meta):
        verbose_name = _('Plan')
        verbose_name_plural = _('Plans')

    def __str__(self):
        return f"{self.name} - ${self.price} ({self.duration_days} days)"


class Subscription(TimestampModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="subscriptions")
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name="subscriptions")
    start_date = models.DateTimeField(verbose_name=_("Start date"), default=timezone.now)
    end_date = models.DateTimeField(verbose_name=_("End date"), blank=True)
    status = models.CharField(verbose_name=_('status'), max_length=10, choices=SubscriptionStatus.choices,
                              default=SubscriptionStatus.ACTIVE)

    def save(self, *args, **kwargs):
        if not self.pk and not self.end_date:
            self.end_date = self.start_date + timedelta(days=self.plan.duration_days)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user} - {self.plan.name} ({self.status})"


class ExchangeRateLog(models.Model):
    base_currency = models.CharField(verbose_name=_("Base Currency"), max_length=3, choices=CurrencyUnit.choices,
                                     default=CurrencyUnit.USD)
    target_currency = models.CharField(verbose_name=_("Target Currency"), max_length=3, choices=CurrencyUnit.choices)
    rate = models.DecimalField(verbose_name=_("Rate"), max_digits=10, decimal_places=4)
    fetched_at = models.DateTimeField(verbose_name=_("Fetched at"), auto_now_add=True)

    class Meta:
        verbose_name = _("Exchange Rate Log")
        verbose_name_plural = _("Exchange Rate Logs")

    def __str__(self):
        return f"{self.base_currency} -> {self.target_currency}: {self.rate} @ {self.fetched_at}"
