from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect
import random
import string
from api.models import URLMapping


def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))


class ShortenURLAPIView(APIView):
    def post(self, request):
        long_url = request.data.get("long_url")
        if not long_url.startswith("http://") and not long_url.startswith("https://"):
            return Response({"error": "Invalid URL format. Must start with http:// or https://"}, status=status.HTTP_400_BAD_REQUEST)
        
        mapping, created = URLMapping.objects.get_or_create(long_url=long_url, defaults={"short_code": generate_short_code()})
        return Response({"short_url": f"http://short.ner/{mapping.short_code}"}, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)


class RedirectURLAPIView(APIView):
    def get(self, request, short_code):
        try:
            mapping = URLMapping.objects.get(short_code=short_code)
            return redirect(mapping.long_url)
        except URLMapping.DoesNotExist:
            return Response({"error": "Short URL not found"}, status=status.HTTP_404_NOT_FOUND)