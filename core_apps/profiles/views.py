from rest_framework import mixins , viewsets, generics, status, permissions, authentication
from rest_framework_simplejwt import authentication as jwt_auth
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from core_apps.profiles import models, serializers, pagination

class ProfilesApiView(generics.ListAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfilesSerializer
    pagination_class = pagination.StandardPagination

class ProfileApiView(generics.RetrieveAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [authentication.TokenAuthentication, jwt_auth.JWTAuthentication]
    
    def retrieve(self, request, username,*args, **kwargs):
        try:
            profile = models.Profile.objects.get(username=username)
        except models.Profile.DoesNotExist:
            return Response({"message" : "Profile with this username does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        serailizer = self.serializer_class(profile, many=False)
        
        return Response(serailizer.data, status=status.HTTP_200_OK)
    
class UpdateProfileApiView(generics.UpdateAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [authentication.TokenAuthentication, jwt_auth.JWTAuthentication]
    
    def get_queryset(self):
        return self.queryset.get(user=self.request.user)
    
    def partial_update(self, request, username, *args, **kwargs):
        if username != self.request.user.profile.username:
            return Response({"message" : "This is not your profile"}, status=status.HTTP_403_FORBIDDEN)
        
        try:
            profile = models.Profile.objects.get(username=username)
        except models.Profile.DoesNotExist:
            return Response({"message" : "Profile with this username does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        serailizer = self.serializer_class(instance=profile, data=request.data, many=False)
        
        if serailizer.is_valid():
            serailizer.save()
            return Response(serailizer.data, status=status.HTTP_200_OK)
        
        return Response(serailizer.errors, status=status.HTTP_400_BAD_REQUEST)