from rest_framework import serializers

from .models import PageView


class PageViewSerializer(serializers.ModelSerializer):
    class Meta:
        """Metadata for PageViewSerializer."""

        model = PageView
        fields='__all__'
        read_only_fields = ['timestamp']
