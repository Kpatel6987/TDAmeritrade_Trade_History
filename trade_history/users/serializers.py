from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(label='Email Address')
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'positions',
            'password',
        ]
        extra_kwargs = {
            "password": {"write_only": True}
            #"accounts": {"read_only": True}
        }

    def validate(self, data):
        user_qs = User.objects.filter(email=data['email'])
        if user_qs.exists():
            raise serializers.ValidationError("This email is already in use")
        return data

    def create(self, validated_data):
        user_obj = User(username = validated_data['username'], email = validated_data['email'])
        user_obj.set_password(validated_data['password'])
        user_obj.save()
        return validated_data



# class UserLoginSerializer(ModelSerializer):
#     token = serializers.CharField(allow_blank=True, read_only=True)
#     username = serializers.CharField()
#     email = serializers.EmailField(label='Email Address')
#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'email',
#             'password',
#             'token',

#         ]
#         extra_kwargs = {"password": {"write_only": True}}

#     def validate(self, data):
#         email = data['email']
#         user_qs = User.objects.filter(email=email)
#         if user_qs.exists():
#             raise serializers.ValidationError("This user has already registered.")
#         return data