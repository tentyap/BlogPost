from rest_framework import serializers
# from blogapp.models import Comment
# from blogapp.serilizers import BlogPostSerializer


# class CommentSerilaizer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = fields = ['reference_id', 'comment', 'comment_user', 'created_by', 'updated_by', 'created_at', 'is_delete']
        
#     def create(self, validate_data):
#         return Comment.objects.create(**validate_data)