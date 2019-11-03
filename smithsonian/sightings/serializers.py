from rest_framework import serializers

from smithsonian.sightings.models import Sighting, SightingImage


class SightingImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SightingImage
        fields = ['url', 'sighting']


class SightingSerializer(serializers.ModelSerializer):

    images = SightingImageSerializer(many=True, read_only=True)

    class Meta:
        model = Sighting
        fields = ['user', 'images', 'cause_of_death', 'is_alive',
                  'latitude', 'longitude', 'comment', 'species']

    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES
        sighting = Sighting.objects.create(**validated_data)
        for image_data in images_data.values():
            SightingImage.objects.create(sighting=sighting, url=image_data)

        return sighting
