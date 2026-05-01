from rest_framework.response import Response
from rest_framework import status
from . serializers import RegisterSerializer , LoginSerilizer
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import AllowAny , IsAuthenticated
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def RegisterView(request):
    if request.method=="POST":
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)        
    


@api_view(['POST'])
@permission_classes([AllowAny])
def LoginView(request):
    if request.method=='POST':
        ser=LoginSerilizer(data=request.data)
        if ser.is_valid():
            uemail=ser.validated_data['email']
            upass=ser.validated_data['password']
            user=authenticate(request , username=uemail , password=upass)
            if user is not None:
                login(request , user)
                refresh = RefreshToken.for_user(user)
                return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }, status=200)
        return Response(ser.errors , status=status.HTTP_400_BAD_REQUEST ) 


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def LogOutView(request):
    try:
        refresh_token = request.data.get("refresh")
        token=RefreshToken(refresh_token)
        token.blacklist()
        return Response(
            {"message": "User logged out successfully"},
            status=status.HTTP_205_RESET_CONTENT
        )    
    except:
        return Response(
        {"error": "Invalid token"},
            status=status.HTTP_400_BAD_REQUEST
        ) 