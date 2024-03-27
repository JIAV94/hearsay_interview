from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SortPayloadSerializer


class SortKeysView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = SortPayloadSerializer(data=request.data)
        if serializer.is_valid():
            sort_keys = serializer.validated_data["sortKeys"]
            payload = serializer.validated_data["payload"]

            # Sorting the specified keys
            for key in sort_keys:
                try:
                    # If the values are integers, sort them as integers
                    int_list = [int(item) for item in payload[key]]
                    payload[key] = sorted(int_list)
                except ValueError:
                    # If the values are not integers, sort them as strings
                    payload[key].sort()
                except KeyError:
                    return Response(
                        {"error": f"Key '{key}' not found in payload"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            return Response(payload, status=status.HTTP_200_OK)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )
