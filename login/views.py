# pylint: disable=C0111
'''
Vista del archivo login
'''

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings


class LoginView(APIView):
    '''
    Metodo para iniciar sesión.
    '''

    authentication_classes = ()
    permission_classes = ()

    def post(self, request):

        errors = {}

        username = request.data.get('username')
        password = request.data.get('password')
        user_data = {
            'user': username,
            'password': password
        }

        if username == '' or username is None:
            errors['username'] = ['El campo usuario es obligatorio.']
        if password == '' or password is None:
            errors['password'] = ['El campo contraseña es obligatorio.']

        if len(errors) > 0:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(username=username, is_active=True)
        except ObjectDoesNotExist:
            return Response({'detail': ['Acceso denegado']}, status=status.HTTP_401_UNAUTHORIZED)
        
        try:
            user = authenticate(username=username, password=password)
            login(request, user)
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            full_name = user.first_name + ' ' + user.last_name if user.first_name and user.last_name else ''
            return Response({'token': token,'username': user.username, 'full_name': full_name , 'is_superuser': user.is_superuser}, status=status.HTTP_202_ACCEPTED)
        # except Token.DoesNotExist:
        #     return Response({'detail': ['Acceso denegado']}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({'detail': ['Actualmente no se puede ingresar a la aplicación, por favor intente más tarde']}, status=status.HTTP_404_NOT_FOUND)


class LogoutView(APIView):
    '''
    Metodo para cerrar la sesión.
    '''

    def get(self, request):

        # El token llega con el formato "Toke <numero_token>" se ejecuta el split y se toma la segunda posicion...
        token_number = request.META.get('Autorization').split(' ')[1]
        try:
            token = Token.objects.get(key=token_number)
            user = token.user
            token.delete()

            Token.objects.create(user=user)
        except Token.DoesNotExist:
            return Response({'detail':['Token incorrecto']}, status=status.HTTP_401_UNAUTHORIZED)

        response = Response({}, status=status.HTTP_202_ACCEPTED)
        return response