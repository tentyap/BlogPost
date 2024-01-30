import logging

from django.http import JsonResponse


from rest_framework.views import APIView
from rest_framework import status
from blogapp.models  import Comment
from blogapp.serilizers import CommentSerilaizer



logger=logging.getLogger('django') 


class CreateComment(APIView):
    authentication_classes = []
    permission_classes = []
    
    def post(self, request):

        if not request.body:
            msg = {
                "error": "cannot blank"
            }
            return JsonResponse(msg, status=200)
        print(request.body)
        print("123455555555555555555555555555555555555555555555555555555555555555")
        try:
            serializer = CommentSerilaizer(data=request.data)
            print(serializer)
            if serializer.is_valid():
                serializer.save()
            msg = {
                    "sucess message": "Success"
                }
            return JsonResponse(msg, status=200)
        except Exception as exe:
            logger.error(str(exe))
            message= {
                "error": "Internal Server Error"
            }
        return JsonResponse(message, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
class ListComment(APIView):
    permission_classes = []
    authentication_classes = []
    
    def get(self,request):
        try: 
            blogpost=Comment.objects.filter(is_delete=False)#model instance
            print("1111")
            serializers=CommentSerilaizer(blogpost,many=True)#model instance to python
            msg={
                    "message Response":"SUCESS OF  DATA ",
                    "data":serializers.data
            }
        
            return JsonResponse(msg, status = 200)
        except Exception as exe:
            logger.error(str(exe),exc_info=True)
            msg={
              "erro Message":"invalid  Data"
        }
        return JsonResponse(msg,status=400)
    