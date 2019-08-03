
from django.contrib.auth import authenticate
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

...

class LoginView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request, *args, **kwargs):
        data = request.data
        print (data, data.get('username'), data.get('password'))
        user = authenticate(username=data.get('username'), password=data.get('password'))
        print (user)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'access_token': token.key}, status=200)
        return Response({'error':'usuario no encontrado'})
