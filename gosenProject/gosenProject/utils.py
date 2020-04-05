from Admin.serializers.common import AdminListSerializer
from Admin.models import Admin


def my_jwt_response_handler(token, user=None, request=None):
    admin = Admin.objects.get(user=user)
    return {
        'token': token,
        'profile': AdminListSerializer(admin).data
    }
