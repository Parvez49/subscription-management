from rest_framework import serializers

from project_apps.subscriptions.models import Subscription, ExchangeRateLog


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = (
            'id',
            'plan',
            'start_date',
            'end_date',
            'status',
        )
        read_only_fields = ('end_date', 'status')


class ExchangeRateLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRateLog
        fields = (
            'id',
            'base_currency',
            'target_currency',
            'rate',
            'fetched_at',
        )
