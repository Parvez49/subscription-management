from django.core.management.base import BaseCommand

from project_apps.subscriptions.models import Plan


class Command(BaseCommand):
    def handle(self, *args, **options):
        plans = [
            {'name': 'Free', 'price': 0, 'duration_days': 14},
            {'name': 'Monthly', 'price': 49, 'duration_days': 30},
            {'name': 'Yearly', 'price': 99, 'duration_days': 365},
        ]
        for plan in plans:
            Plan.objects.update_or_create(
                name=plan['name'],
                defaults={
                    'price': plan['price'],
                    'duration_days': plan['duration_days']
                })
        self.stdout.write(self.style.SUCCESS('Default plans loaded.'))
