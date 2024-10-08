from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import SignUpSerializer, UserSerializer

# Create your views here.


@api_view(["POST"])
def customerRegister(request):
    data = request.data

    user = SignUpSerializer(data=data)

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "customer"
        return super().get_context_data(**kwargs)

    if user.is_valid():
        if not User.objects.filter(username=data["email"]).exists():
            user = User.objects.create(
                first_name=data["first_name"],
                last_name=data["last_name"],
                username=data["email"],
                email=data["email"],
                password=make_password(data["password"]),
            )

            user.is_customer = True
            user.save()

            return Response({"message": "User registered."}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "User already exists"}, status=status.HTTP_400_BAD_REQUEST
            )

    else:
        return Response(user.errors)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def currentUser(request):

    user = UserSerializer(request.user)

    return Response(user.data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def updateUser(request):
    user = request.user

    data = request.data

    user.first_name = data["first_name"]
    user.last_name = data["last_name"]
    user.username = data["email"]
    user.email = data["email"]

    if data["password"] != "":
        user.password = make_password(data["password"])

    user.save()

    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)
