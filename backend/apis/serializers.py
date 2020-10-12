from rest_framework import serializers
from timesheets import models


class TimeSheetSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.TimeSheet
        read_only_fields = ('description', 'start_time', 'id')