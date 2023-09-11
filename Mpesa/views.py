from rest_framework import views, response, status

from .serializers import SendSTKPushSerializer

class SendSTKPushView(views.APIView):
    def post(self, request, format=None):
        serializer = SendSTKPushSerializer(data=request.data)
        if serializer.is_valid():
            res = serializer.save()
            return response.Response(res, status=status.HTTP_200_OK)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        