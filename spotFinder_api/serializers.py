from rest_framework import serializers
from spotFinder_api.models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id','coordinates','availability','capacity',
                'availableSpace','price','timeRestrictions')
