from rest_framework import serializers
from .models import Song, Singer

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id','title', 'singer', 'duration']

class SingerSerializer(serializers.ModelSerializer):
    # song = serializers.StringRelatedField(many=True, read_only=True) # read_only by default and many = true if more relations applied
    # song = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # song = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='song-detail') # create hyperlink for song
    # song = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title') # To show specific field in song
    song = serializers.HyperlinkedIdentityField(many=True,view_name='song-detail') #to show only one hyper link of song if many is not true
    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'song']
