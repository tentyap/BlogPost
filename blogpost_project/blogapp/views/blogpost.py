
import logging

from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


from rest_framework import status
from rest_framework.authentication import BaseAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated 

from blogapp.models import BlogPost
from blogapp import global_msg
from blogapp.serilizers import BlogPostSerializer

logger = logging.getLogger("django")



class BlogCreateAPIView(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self, request):
        if not request.body:
            msg = {
                global_msg.RESPONSE_CODE_KEY: global_msg.SUCESS_RESPONSE_CODE,
                global_msg.RESPONSE_MSG_KEY: "cannot blank"
            }
            return JsonResponse(msg, status=status.HTTP_200_OK)
        print(request.body)
        
        try:
            serializer = BlogPostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                msg = {
                    global_msg.RESPONSE_CODE_KEY: "1",
                    global_msg.RESPONSE_MSG_KEY: "Success"
                }
                return JsonResponse(msg, status=status.HTTP_201_CREATED)
            else:
                msg = {
                    global_msg.RESPONSE_CODE_KEY:"0",
                    global_msg.RESPONSE_MSG_KEY: "Invalid Data in serializer",
                    global_msg.ERROR_KEY: serializer.errors
                }
                return JsonResponse(msg, status=status.HTTP_400_BAD_REQUEST)
        except Exception as exe:
            logger.error(str(exe))
            msg = {
                global_msg.RESPONSE_CODE_KEY:'0',
                global_msg.RESPONSE_MSG_KEY: "Internal Server Error"
            }
            return JsonResponse(msg, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
class BlogListApiview(APIView):
    authentication_classes=[TokenAuthentication]
    premission_classes=[IsAuthenticated]
    '''This class shows the all the list of student'''
    def get(self,request):
        print(request.headers)
        try: 
            blogpost=BlogPost.objects.filter(is_delete=False)#model instance
            print("1111")
            serializers=BlogPostSerializer(blogpost,many=True)#model instance to python
            
            msg={
                    global_msg.RESPONSE_CODE_KEY:global_msg.SUCESS_RESPONSE_CODE,
                    global_msg.RESPONSE_MSG_KEY:"SUCESS OF  DATA ",
                    "data":serializers.data
                }
         
            return JsonResponse(msg, status = status.HTTP_200_OK)
            
        except Exception as exe:
            logger.error(str(exe),exc_info=True)
            msg={
                global_msg.RESPONSE_CODE_KEY:global_msg.UNSUCCESS_RESPONSE_CODE,
                global_msg.RESPONSE_MSG_KEY :"invalid  Data"
        }
        return JsonResponse(msg,status=status.HTTP_400_BAD_REQUEST)
    
# class BlogEditApiview(APIView):
#     authentication_classes=[TokenAuthentication]
#     premission_classes=[IsAuthenticated]
#     '''This class updated all the of student'''
#     def put(self,request,pk):
#         print("edit vieww blah blah ")
#         if not request.body:
#             msg={
#                 global_msg.RESPONSE_CODE_KEY:global_msg.SUCESS_RESPONSE_CODE,
#                 global_msg.RESPONSE_MSG_KEY:"sucess"
#             }
#             return JsonResponse(msg, status = status.HTTP_200_OK)
#         try: 
#             blogpost=BlogPost.objects.get(id=pk, is_delete=False)
#             print(blogpost, "hello manadhar")
#             serializer = BlogPostSerializer(blogpost, data=request.data)
#             user=User.objects.get(username="kamal")
#             if serializer.is_valid():
#                 serializer.save()
#                 msg={
#                     global_msg.RESPONSE_CODE_KEY:global_msg.SUCESS_RESPONSE_CODE,
#                     global_msg.RESPONSE_MSG_KEY:"data update sucessfully "
#                 }
#                 return JsonResponse(msg, status = status.HTTP_400_BAD_REQUEST)
#             msg={
#                 global_msg.RESPONSE_CODE_KEY:global_msg.UNSUCCESS_RESPONSE_CODE,
#                 global_msg.RESPONSE_MSG_KEY :"invalid  Data",
#                 global_msg.ERROR_KEY:serializer.errors
#         }
#             return JsonResponse(msg,status=status.HTTP_400_BAD_REQUEST)
#         except ObjectDoesNotExist as exe:
#             logger.error(str(exe), exc_info=True)
#             msg={
#                 global_msg.RESPONSE_CODE_KEY:global_msg.UNSUCCESS_RESPONSE_CODE,
#                 global_msg.RESPONSE_MSG_KEY :"Not Data Found"
#             }   
#         except Exception as exe:
#             logger.error(str(exe))
#             msg={
#                 global_msg.RESPONSE_CODE_KEY:global_msg.UNSUCCESS_RESPONSE_CODE,
#                 global_msg.RESPONSE_MSG_KEY :"invalid  Data"
#         }
#         return JsonResponse(msg,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    
    
class BLogDeleteApiView(APIView):
    '''This class delete all the  student'''
    def delete(self,request,pk):
        try:
            blogpost=BlogPost.objects.get(id=pk)
            blogpost.is_delete = True
            blogpost.save()
            msg={
                    global_msg.RESPONSE_CODE_KEY:global_msg.SUCESS_RESPONSE_CODE,
                    global_msg.RESPONSE_MSG_KEY:"Delete sucessfully "
                }
            return JsonResponse(msg,status=status.HTTP_200_OK)
        except ObjectDoesNotExist as exe:
            logger.error(str(exe), exc_info=True)
            msg={
                global_msg.RESPONSE_CODE_KEY:global_msg.UNSUCCESS_RESPONSE_CODE,
                global_msg.RESPONSE_MSG_KEY :"Not Data Found"
            }   
            return JsonResponse(msg,status=status.HTTP_400_BAD_REQUEST)
        except Exception as exe:
            logger.error(str(exe), exc_info=True)
            msg={
                global_msg.RESPONSE_CODE_KEY:global_msg.UNSUCCESS_RESPONSE_CODE,
                global_msg.RESPONSE_MSG_KEY :"invalid  Data"
            }
            return JsonResponse(msg,status=status.HTTP_400_BAD_REQUEST)

class BlogEditApiview(APIView): 
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] 
    def put(self, request,pk):
        if not request.body:
            msg = {
                global_msg.RESPONSE_CODE_KEY: global_msg.UNSUCCESS_RESPONSE_CODE,
                global_msg.RESPONSE_MSG_KEY: "Edit Scucessfully.!"
            }
            return JsonResponse(msg, status=status.HTTP_200_OK)

        try:
            blog= BlogPost.objects.get(id=pk, is_delete=False) #id 1 ko details
            serializers = BlogPostSerializer(blog, data=request.data)
            # user = User.objects.get(username='devi')
            if serializers.is_valid():
                serializers.save()
                serializers.save
                msg = {
                    global_msg.RESPONSE_CODE_KEY: global_msg.SUCCESS_RESPONSE_CODE,
                    global_msg.RESPONSE_MSG_KEY: "Data Update Successfully"
                }
                return JsonResponse(msg, status=status.HTTP_200_OK)
            msg = {
                global_msg.RESPONSE_CODE_KEY: global_msg.UNSUCCESS_RESPONSE_CODE,
                global_msg.RESPONSE_MSG_KEY: "Invalid Data",
                global_msg.ERROR_KEY: serializers.errors
            }
            return JsonResponse(msg, status=status.HTTP_400_BAD_REQUEST)
        
        except ObjectDoesNotExist as exe:
            logger.error(str(exe), exc_info=True)
            msg = {
                global_msg.RESPONSE_CODE_KEY:global_msg.UNSUCCESS_RESPONSE_CODE,
                global_msg.RESPONSE_MSG_KEY:"No data Found!"
            }
            return JsonResponse(msg, status=status.HTTP_400_BAD_REQUEST)
        except Exception as exe:
            logger.error(str(exe), exc_info=True)
            msg = {
                global_msg.RESPONSE_CODE_KEY:global_msg.UNSUCCESS_RESPONSE_CODE,
                global_msg.RESPONSE_MSG_KEY:"No data Found!"
            }
        return JsonResponse(msg, status=status.HTTP_400_BAD_REQUEST)