from rest_framework import serializers
from blogapp.models import BlogPost
from blogapp.models import Comment

class BlogPostSerializer(serializers.ModelSerializer):
    BlogTitle = serializers.CharField(source="title", error_messages={"blank": "Title cannot be blank"})
    BlogDescription = serializers.CharField(source="description", error_messages={"blank": "Description cannot be blank"})
    
    class Meta:
        model = BlogPost
        fields = ['BlogTitle', 'BlogDescription']  # Use the corrected field names

    def create(self, validated_data):
        return BlogPost.objects.create(**validated_data)

    def validate_BlogTitle(self, title):
        if BlogPost.objects.filter(title=title).exists():
            raise serializers.ValidationError("Title is already exist")
        return title


class CommentSerilaizer(serializers.ModelSerializer):
    blog=BlogPostSerializer(many=True)
    class Meta:
        model = Comment
        fields = ["comment", "comment_user",'blog']
    def create(self, validate_data):
        return Comment.objects.create(**validate_data)