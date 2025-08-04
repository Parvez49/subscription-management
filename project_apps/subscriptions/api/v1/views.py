from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from project_apps.subscriptions.api.v1.serializers import SubscribeSerializer
from project_apps.subscriptions.enums import SubscriptionStatus
from project_apps.subscriptions.models import Subscription


class SubscribeCreateAPIVIEW(CreateAPIView):
    serializer_class = SubscribeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )


class SubscriptionListAPIVIEW(ListAPIView):
    serializer_class = SubscribeSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)


class CancelSubscriptionAPIVIEW(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            subscription = Subscription.objects.filter(user=request.user, status=SubscriptionStatus.ACTIVE).latest(
                'start_date')
        except Subscription.DoesNotExist:
            return Response({"detail": "No active subscription found."}, status=status.HTTP_404_NOT_FOUND)

        subscription.status = SubscriptionStatus.CANCELLED
        subscription.save()

        return Response({"detail": "Subscription cancelled successfully."}, status=status.HTTP_200_OK)
