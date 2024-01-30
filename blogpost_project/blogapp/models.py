from django.db import models
import uuid
from django.contrib.auth.models import User




def uuid_generate():
    return uuid.uuid4().hex



class BaseModel(models.Model):
    reference_id=models.CharField(max_length=32,unique=True , default=uuid_generate)
    created_by=models.ForeignKey(User,on_delete=models.PROTECT, db_column ="created_by", null=True, related_name="+")
    updated_by=models.ForeignKey(User,on_delete=models.PROTECT, db_column ="updated_by", null=True, related_name="+")
    created_at=models.DateTimeField(auto_now=False)
    created_at=models.DateTimeField(auto_now=True)
    is_delete=models.BooleanField(default=False)
    
    class Meta:
        abstract=True
    
class BlogPost(BaseModel):
    title=models.CharField(max_length=100)
    description=models.TextField()
    file=models.ImageField(upload_to="image")
    
    class Meta:
        db_table="BlogPost"
    
    
class Comment(BaseModel):
    comment=models.CharField(max_length=50)
    comment_user=models.ForeignKey(BlogPost, on_delete=models.PROTECT, related_name="Comment")
    class Meta:
        db_table="Comment"