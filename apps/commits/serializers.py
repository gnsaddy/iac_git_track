from rest_framework import serializers
from .models import GitCommits


# serializer class for GitCommits model
class GitCommitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GitCommits
        fields = '__all__'
