from rest_framework import serializers


class SortPayloadSerializer(serializers.Serializer):
    sortKeys = serializers.ListField(
        child=serializers.CharField(),
        allow_empty=False,
    )
    payload = serializers.DictField(
        child=serializers.ListField(child=serializers.CharField()),
        allow_empty=False,
    )
