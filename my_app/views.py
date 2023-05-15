# from django.shortcuts import render

# Create your views here.
import json
from rest_framework import generics
from .models import Score
from .serializers import ScoreSerializer
from rest_framework import status
from rest_framework.response import Response

class GetScore(generics.CreateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        input_value = data.get('input', 0)
        return self.perform_create(input_value)

    def perform_create(self, input_value):
        user_id = self.request.data.get('user_id')
        value = int(input_value) + 1
        serializer = self.get_serializer(data={'user_id': user_id, 'value': value})
        serializer.is_valid(raise_exception=True)
        self.perform_save(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_save(self, serializer):
        serializer.save()
