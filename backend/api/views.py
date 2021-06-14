from rest_framework import viewsets, routers
from react_app.models import User_Models
from .serializers import UserSerializer


class UserApi(viewsets.ModelViewSet):
    queryset = User_Models.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User_Models.objects.all()
        L_id = self.request.query_params.get('id')

        if L_id:
            queryset = queryset.filter(user_id=L_id)

        return queryset


router = routers.DefaultRouter()
router.register(r'user', UserApi)
