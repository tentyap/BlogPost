# from django.contrib.auth.base_user import BaseUserManager

# class UserManager(BaseUserManager):
#     use_in_migrations = True
    
#     def create_user(self, email, password, **extra_fields):
#         """
#         create and saves a user with the given email and pasword
#         """
#         if not email:
#             raise ValueError("The email must be given ")
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('A emil must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user
    
#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_staff ', True)
#         extra_fields.setdefault('is_superuser ', True)
#         extra_fields.setdefault('is_active ', True)
        
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError(("super_user must havee is_staff True"))
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError(('superuser must be superuser True'))
#         return self.create_user(email, password, **extra_fields)
    