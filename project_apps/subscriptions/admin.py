from django.contrib import admin

from project_apps.subscriptions.models import Plan, Subscription, ExchangeRateLog


def is_superuser_or_staff(request):
    user = request.user
    return user.is_superuser or user.is_staff


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'currency', 'duration_days', 'created_at')
    search_fields = ('name',)
    list_filter = ('currency', 'created_at')
    ordering = ('-created_at',)
    readonly_fields = ('created_by',)

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

    def has_module_permission(self, request):
        return is_superuser_or_staff(request)

    def has_view_permission(self, request, obj=None):
        return is_superuser_or_staff(request)

    def has_add_permission(self, request):
        return is_superuser_or_staff(request)

    def has_change_permission(self, request, obj=None):
        return is_superuser_or_staff(request)

    def has_delete_permission(self, request, obj=None):
        return is_superuser_or_staff(request)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'start_date', 'end_date', 'status', 'created_at')
    list_filter = ('status', 'plan', 'start_date')
    search_fields = ('user__email', 'plan__name')
    readonly_fields = ('created_at', 'modified_at')
    ordering = ('-created_at',)

    def has_module_permission(self, request):
        return is_superuser_or_staff(request)

    def has_view_permission(self, request, obj=None):
        return is_superuser_or_staff(request)


@admin.register(ExchangeRateLog)
class ExchangeRateLogAdmin(admin.ModelAdmin):
    list_display = ('base_currency', 'target_currency', 'rate', 'fetched_at')
    list_filter = ('base_currency', 'target_currency')
    search_fields = ('base_currency', 'target_currency')
    ordering = ('-fetched_at',)

    def has_module_permission(self, request):
        return is_superuser_or_staff(request)

    def has_view_permission(self, request, obj=None):
        return is_superuser_or_staff(request)
