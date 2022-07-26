from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer



from allauth.account.adapter import get_adapter


from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'us_studen', 'is_teacher')


class CustomRegisterSerializer(RegisterSerializer):
    us_studen =  serializers.BooleanField()
    is_teacher =  serializers.BooleanField()
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'is_student', 'is_teacher')




    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'us_studen': self.validated_data.get('us_studen', ''),
            'is_teacher': self.validated_data.get('is_teacher', '')
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.us_studen = self.cleaned_data.get('us_studen')
        user.is_teacher = self.cleaned_data.get('is_teacher')
        user.save()
        adapter.save_user(request, user, self)
        return user




