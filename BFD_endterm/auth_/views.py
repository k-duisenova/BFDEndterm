from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from auth_.models import User
from auth_.serializers import UserSerializer


class UserSignup(viewsets.ViewSet):

    @action(methods=['POST'], detail=False)
    def signup(self, request):
        if request.method == 'POST':
            user_data = request.data
            new_user = User.objects.create(email=user_data['email'], full_name=user_data['full_name'],
                                           address=user_data['address'], phone=user_data['phone'])
            new_user.set_password(user_data['password'])
            new_user.save()
            serializer = UserSerializer(new_user)
            return Response(serializer.data)

    @action(methods=['POST'], detail=False, permissions=(IsAdminUser,))
    def create_manager(self, request):
        if request.method == 'POST':
            user_data = request.data

            new_user = User.objects.create(email=user_data['email'], full_name=user_data['full_name'],
                                           address=user_data['address'], phone=user_data['phone'],
                                           is_staff=True)
            new_user.save()
            serializer = UserSerializer(new_user)
            return Response(serializer.data)
