from rest_framework import serializers

from core_apps.profiles import models

class ProfilesSerializer(serializers.ModelSerializer):
    """Profile List Serialier"""
    
    class Meta:
        model = models.Profile
        fields = ["id","username","country","gender"]
        
        
class ProfileSerializer(serializers.ModelSerializer):
    """Profile Serializer"""
    
    class Meta:
        model = models.Profile
        fields = "__all__"
        read_only_fields = ["id","pkid","user","follows"]
        
class FollowUnFollowSerializer(serializers.ModelSerializer):
    """Follow UnFollow Serializer"""
    
    class Meta:
        model = models.Profile
        fields = ["id", "username", "gender", "user"]