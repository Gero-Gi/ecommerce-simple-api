from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer
from .models import User


class GetTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {'token': token.key,
             'user_id': user.id,
             'first_name': user.first_name,
             'last_name': user.last_name,
             'email': user.email,
             'is_superuser':user.is_superuser,
             })


class SignupView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    http_method_names = ['post']
    