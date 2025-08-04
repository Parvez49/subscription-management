from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from project_apps.subscriptions.api.v1.serializers import SubscribeSerializer


class SubscribeAPIVIEW(generics.CreateAPIView):
    serializer_class = SubscribeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )
