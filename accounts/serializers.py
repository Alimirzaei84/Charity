from rest_framework import serializers

from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'phone', 'address' , 'gender' , 'age' , 'description' , 'first_name' , 'last_name' , 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone=validated_data['phone'],
            address=validated_data['address'],
            gender = validated_data['gender'],
            age = validated_data['age'],
            description = validated_data['description']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user