from rest_framework import serializers

from smithsonian.sightings.models import Sighting, SightingImage


class SightingImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SightingImage
        fields = ['url', 'sighting']


class SightingSerializer(serializers.ModelSerializer):

    images = SightingImageSerializer(many=True)

    class Meta:
        model = Sighting
        fields = ['user', 'images', 'cause_of_death', 'is_alive',
                  'latitude', 'longitude', 'comment', 'species']

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
