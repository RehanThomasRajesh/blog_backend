from rest_framework import serializers
from blog.models import user,post

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('id', 'name','profile','email','password')


class postSerializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = ('title', 'id','message')
