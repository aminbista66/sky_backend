from rest_framework import generics
from ..serializers import ShortNoticeSerializer
from rest_framework import permissions
from ..models import ShortNotice
from ..filters import shortNoticeFilterset

class ShortNoticeListAPIView(generics.ListAPIView):
    serializer_class = ShortNoticeSerializer
    permission_classes = [permissions.AllowAny]
    filterset_class = shortNoticeFilterset
    model = ShortNotice


class ShortNoticeCreateAPIView(generics.CreateAPIView):
    serializer_class = ShortNoticeSerializer
    permission_classes = [permissions.AllowAny]


class ShortNoticeUpdateDestroyAPIView(
    generics.UpdateAPIView, generics.DestroyAPIView
):
    serializer_class = ShortNoticeSerializer
    permission_classes = [permissions.IsAdminUser]
