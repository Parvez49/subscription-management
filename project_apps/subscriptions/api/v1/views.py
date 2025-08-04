from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from project_apps.subscriptions.api.v1.serializers import SubscribeSerializer, ExchangeRateLogSerializer
from project_apps.subscriptions.api.v1.utils import fetch_exchange_rate
from project_apps.subscriptions.enums import SubscriptionStatus
from project_apps.subscriptions.models import Subscription, ExchangeRateLog


class SubscribeCreateAPIView(CreateAPIView):
    serializer_class = SubscribeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )


class SubscriptionListAPIView(ListAPIView):
    serializer_class = SubscribeSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)


class CancelSubscriptionAPIView(APIView):
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


class ExchangeRateRetrieveAPIView(APIView):
    permission_classes = [AllowAny]
    queryset = ExchangeRateLog.objects.none()

    def get(self, request):
        base_currency = request.query_params.get('base', 'USD')
        target_currency = request.query_params.get('target', 'BDT')

        try:
            rate = fetch_exchange_rate(base_currency, target_currency)

            # Save to DB
            log = ExchangeRateLog.objects.create(
                base_currency=base_currency,
                target_currency=target_currency,
                rate=rate,
            )

            return Response(ExchangeRateLogSerializer(log).data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
