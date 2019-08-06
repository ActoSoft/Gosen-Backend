from core.serializers import ProfileSerializer
from Admin.serializers import AdminSerializerOnlyIdAndUser
from Admin.models import Admin


def my_jwt_response_handler(token, user=None, request=None):
    admin = Admin.objects.get(user=user)
    return {
        'token': token,
        'profile': AdminSerializerOnlyIdAndUser(admin).data
    }
