from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from smithsonian.sightings.models import Sighting
from smithsonian.sightings.serializers import SightingSerializer


class SightingView(APIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = SightingSerializer

    def get_queryset(self):
        return get_object_or_404(Sighting, user=self.request.user)

    def get(self, request):
        sighting = self.get_queryset()
        serializer = self.serializer_class(sighting)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
