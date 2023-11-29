from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework import mixins, viewsets, generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import CustomUser
from .serializers import UserModelSerializer, UserModelSerializerFull, \
    UserRegisterSerializer

from users import tasks as users_tasks

# Create your views here.
class UserCustomViewSet(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet, ):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = CustomUser.objects.all()
    serializer_class = UserModelSerializerFull

    def get_queryset(self):
        return CustomUser.objects.filter(is_active=True)


class UserListAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserModelSerializer

    def get_serializer_class(self):
        if self.request.version == '0.2':
            return UserModelSerializerFull
        return UserModelSerializer


class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        # Extract the necessary data from the request
        email = request.data.get('email')
        password = request.data.get('password')
        extra_fields = {
            'user_name': request.data.get('user_name'),
            # Add any additional fields you need for user creation
        }

        # Validate the data
        if not email or not password:
            return Response({'error': 'Email and password are required.'},
                            status=status.HTTP_400_BAD_REQUEST)

        # Create a new user
        try:
            user = CustomUser.objects.create_user(email=email,
                                                  password=password,
                                                  **extra_fields)
            if user:
                users_tasks.send_welcome_email(user.id)

        except ValueError as e:
            return Response({'error': str(e)},
                            status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'User registered successfully.'},
                        status=status.HTTP_201_CREATED)
