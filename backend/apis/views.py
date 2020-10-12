from rest_framework import generics

from timesheets import models
from .serializers import TimeSheetSerializer

from datetime import datetime

class ListTimeSheet(generics.ListCreateAPIView):
    queryset = models.TimeSheet.objects.all()
    serializer_class = TimeSheetSerializer


class DetailTimeSheet(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.TimeSheet.objects.all()
    serializer_class = TimeSheetSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(data={'end_time': datetime.now()})
        serializer.is_valid(raise_exception=True)
        serializer.save()
