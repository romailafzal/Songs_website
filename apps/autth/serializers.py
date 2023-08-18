from django.urls import reverse
from rest_framework import serializers
from apps.autth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import threading
from apps.autth.utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import get_object_or_404


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['email','name', 'password', 'password2','tc']
        extra_kwargs = {'password': {'write_only': True}}


    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserLoginSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(max_length=255)
  class Meta:
    model = User
    fields = ['email', 'password']


class UserProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'email', 'name']

class UserChangePasswordSerializer(serializers.Serializer):
  password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  password2 = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  class Meta:
    fields = ['password', 'password2']

  def validate(self, attrs):
    password = attrs.get('password')
    password2 = attrs.get('password2')
    user = self.context.get('user')
    if password != password2:
      raise serializers.ValidationError("Password and Confirm Password doesn't match")
    user.set_password(password)
    user.save()
    return attrs



class SendPasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    
    class Meta:
        fields = ['email']

    def validate(self, attrs):
        email = attrs.get('email')

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            #current_site = get_current_site(self.context.get('request'))
            current_site = "http://127.0.0.1:8000/"
            link = reverse('password-reset', kwargs={'uidb64': uid, 'token': token})
            reset_link = f"{current_site}{link}"
            print(reset_link)
          
            """
            email_subject = 'Reset your password'
            email_body = reset_link
            
            email = EmailMessage(
                email_subject,
                email_body,
                settings.EMAIL_HOST_USER,
                [user.email],
            )

            #send email
            email.send(fail_silently=False)

            #EmailThread(email).start()
            """

        else:
            raise serializers.ValidationError("Email address not found.")
        
        return attrs

class UserPasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)
    
    def validate(self, attrs):
      password = attrs.get('password')
      password2 = attrs.get('password2')
      uidb64 = self.context.get('uidb64')
      token = self.context.get('token')

      if password != password2:
          raise serializers.ValidationError(("Password and Confirm Password don't match"))

      if uidb64 is not None:
          id = smart_str(urlsafe_base64_decode(uidb64))
          user = User.objects.get(id=id)

          if not PasswordResetTokenGenerator().check_token(user, token):
              raise serializers.ValidationError(("Token is not valid or expired"))

          user.set_password(password)
          user.save()
          return attrs
      else:
          raise serializers.ValidationError(("Token is not valid or expired"))


class EmailThread(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)
    
    def run(self):
        self.email.send()



"""
from rest_framework import serializers
from apps.autth.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'name', 'tc', 'password')

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'name', 'tc', 'created_at', 'updated_at')

class UserChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()

class SendPasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

class UserPasswordResetSerializer(serializers.Serializer):
    new_password = serializers.CharField()
"""


