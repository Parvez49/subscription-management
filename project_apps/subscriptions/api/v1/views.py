from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from project_apps.subscriptions.api.v1.serializers import SubscribeSerializer
from project_apps.subscriptions.models import Subscription


class SubscribeCreateAPIVIEW(generics.CreateAPIView):
    serializer_class = SubscribeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )


class SubscriptionListAPIVIEW(generics.ListAPIView):
    serializer_class = SubscribeSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)
