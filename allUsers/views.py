from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
from api.permissions import IsOwnerOrReadOnly, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from rest_framework.parsers import FileUploadParser
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from api.helper import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# from rest_framework.permissions import AllowAny
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
	HTTP_203_NON_AUTHORITATIVE_INFORMATION,
	HTTP_201_CREATED,
	HTTP_202_ACCEPTED,
)

from .serializers import (
	RegistrationSerializer, 
	RegistrationStoreSerializer,
	RegistrationVendorSerializer,
	AccountPropertiesSerializer,
	AccountAllPropertiesSerializer, 
	ChangePasswordSerializer,
	ImagesSerializer
)
from .models import Account, ImageUser
from rest_framework.authtoken.models import Token

# Register
# Url: https://<your-domain>/api/register
@api_view(['POST', ])
@permission_classes([])
@authentication_classes([])
def registration_view(request):

	if request.method == 'POST':
		data = {}
		email = request.data.get('email', '0').lower()
		if validate_email(email) != None:
			data['status'] = 0
			data['message'] = 'Email Sudah Ada.'
			data['response'] = 'Error'
			return Response(data)

		username = request.data.get('username', '0')
		if validate_username(username) != None:
			data['status'] = 0
			data['message'] = 'Username Sudah Ada.'
			data['response'] = 'Error'
			return Response(data)

		serializer = RegistrationSerializer(data=request.data)
		
		if serializer.is_valid():
			allUsers = serializer.save()
			data['status'] = 1
			data['response'] = 'success'
			data['email'] = allUsers.email
			data['username'] = allUsers.username
			data['name'] = allUsers.name
			data['address'] = allUsers.address
			data['phone'] = allUsers.phone
			data['nik'] = allUsers.nik
			data['pk'] = allUsers.pk
			token = Token.objects.get(user=allUsers).key
			data['token'] = token
			
		else:
			data = serializer.errors
		return Response(data)

# Url: https://<your-domain>/api/vendor/register
@api_view(['POST', ])
@permission_classes([])
@authentication_classes([])
def registration_vendor_view(request):

	if request.method == 'POST':
		data = {}
		email = request.data.get('email', '0').lower()
		if validate_email(email) != None:
			data['status'] = 0
			data['message'] = 'Email Sudah Ada.'
			data['response'] = 'Error'
			return Response(data)

		username = request.data.get('username', '0')
		if validate_username(username) != None:
			data['status'] = 0
			data['message'] = 'Username Sudah Ada.'
			data['response'] = 'Error'
			return Response(data)

		serializer = RegistrationVendorSerializer(data=request.data)
		
		if serializer.is_valid():
			allUsers = serializer.save()
			data['status'] = 1
			data['response'] = 'success'
			data['email'] = allUsers.email
			data['username'] = allUsers.username
			data['name'] = allUsers.name
			data['address'] = allUsers.address
			data['phone'] = allUsers.phone
			data['nik'] = allUsers.nik
			data['pk'] = allUsers.pk
			token = Token.objects.get(user=allUsers).key
			data['token'] = token
		else:
			data = serializer.errors
		return Response(data)

# Url: https://<your-domain>/api/toko/register
@api_view(['POST', ])
@permission_classes([])
@authentication_classes([])
def registration_store_view(request):

	if request.method == 'POST':
		data = {}
		email = request.data.get('email', '0').lower()
		if validate_email(email) != None:
			data['status'] = 0
			data['message'] = 'Email Sudah Ada.'
			data['response'] = 'Error'
			return Response(data)

		username = request.data.get('username', '0')
		if validate_username(username) != None:
			data['status'] = 0
			data['message'] = 'Username Sudah Ada.'
			data['response'] = 'Error'
			return Response(data)

		serializer = RegistrationStoreSerializer(data=request.data)
		
		if serializer.is_valid():
			allUsers = serializer.save()
			data['status'] = 1
			data['response'] = 'success'
			data['email'] = allUsers.email
			data['username'] = allUsers.username
			data['name'] = allUsers.name
			data['address'] = allUsers.address
			data['phone'] = allUsers.phone
			data['nik'] = allUsers.nik
			data['pk'] = allUsers.pk
			token = Token.objects.get(user=allUsers).key
			data['token'] = token
		else:
			data = serializer.errors
		return Response(data)


def validate_email(email):
	allUsers = None
	try:
		allUsers = Account.objects.get(email=email)
	except Account.DoesNotExist:
		return None
	if allUsers != None:
		return email

def validate_username(username):
	allUsers = None
	try:
		allUsers = Account.objects.get(username=username)
	except Account.DoesNotExist:
		return None
	if allUsers != None:
		return username


# Account properties
# Response: https://gist.github.com/mitchtabian/4adaaaabc767df73c5001a44b4828ca5
# Url: https://<your-domain>/api/profile/me
# Headers: Authorization: Token <token>
@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def account_properties_view(request):

	try:
		allUsers = request.user
	except Account.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = AccountPropertiesSerializer(allUsers)
		return Response(serializer.data)

# Url: https://<your-domain>/api/toko/
@permission_classes((IsAuthenticated, ))
class toko_properties_all_view(ListCreateAPIView):
	serializer_class = AccountAllPropertiesSerializer

	def get_queryset(self):
		account = Account.objects.filter(role=3)
		return account
	
	from api.helper import get_all as get
	# try:
	# 	allUsers = request.user
	# except Account.DoesNotExist:
	# 	return Response(status=status.HTTP_404_NOT_FOUND)

@permission_classes((IsAuthenticated, ))
class toko_properties_all_view_specific(RetrieveUpdateDestroyAPIView):
	serializer_class = AccountAllPropertiesSerializer
	content = {
                'status': 0,
				'message':'Tidak ditemukan'
            }
	def get_queryset(self, pk):
		
		# account = Account.objects.filter(pk=pk).filter(role=3).values()
		# account = Account.objects.filter(pk=5).values()
		account = Account.objects.get(pk=pk, role=3)
		return account
	
	from api.helper import get_specific as get

@permission_classes((IsAuthenticated, ))
class vendor_properties_all_view(ListCreateAPIView):
	serializer_class = AccountAllPropertiesSerializer

	def get_queryset(self):
		account = Account.objects.filter(role=2)
		return account
	
	from api.helper import get_all as get
	# try:
	# 	allUsers = request.user
	# except Account.DoesNotExist:
	# 	return Response(status=status.HTTP_404_NOT_FOUND)

@permission_classes((IsAuthenticated, ))
class vendor_properties_all_view_specific(ListCreateAPIView):
	serializer_class = AccountAllPropertiesSerializer
	content = {
                'status': 0,
				'message':'Tidak Ditemukan'
            }
	def get_queryset(self, pk):
		account = Account.objects.get(pk=pk, role=2)
		return account
	
	from api.helper import get_specific as get



# Account update properties
# Response: https://gist.github.com/mitchtabian/72bb4c4811199b1d303eb2d71ec932b2
# Url: https://<your-domain>/api/allUsers/properties/update
# Headers: Authorization: Token <token>
@api_view(['PUT',])
@permission_classes((IsAuthenticated, ))
def update_account_view(request):

	try:
		allUsers = request.user
	except Account.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
		
	if request.method == 'PUT':
		serializer = AccountPropertiesSerializer(allUsers, data=request.data)
		data = {}
		if serializer.is_valid():
			serializer.save()
			data['status'] = 1
			data['response'] = 'success'
			data['data'] = serializer.data
			return Response(data=data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# LOGIN
# Response: https://gist.github.com/mitchtabian/8e1bde81b3be342853ddfcc45ec0df8a
# URL: http://127.0.0.1:8000/api/allUsers/login

# @csrf_exempt
# @api_view(["POST"])
# @permission_classes((AllowAny,))
# def login(request):
#     username = request.data.get("username")
#     password = request.data.get("password")
#     if username is None or password is None:
#         return Response({'error': 'Please provide both username and password'},
#                         status=HTTP_400_BAD_REQUEST)
#     user = authenticate(username=username, password=password)
#     if not user:
#         return Response({'error': 'Invalid Credentials'},
#                         status=HTTP_404_NOT_FOUND)
#     token, _ = Token.objects.get_or_create(user=user)
#     return Response({'token': token.key},
#                     status=HTTP_200_OK)

class ObtainAuthTokenView(APIView):

	def post(self, request):
		context = {}

		email = request.data.get('email')
		password = request.data.get('password')
		allUsers = authenticate(username=email, password=password)
		if allUsers:
			try:
				token = Token.objects.get(user=allUsers)
			except Token.DoesNotExist:
				token = Token.objects.create(user=allUsers)
			context['status'] = 1
			context['response'] = 'Success'
			context['pk'] = allUsers.pk
			context['username'] = allUsers.username
			context['email'] = allUsers.email
			context['token'] = token.key
		else:
			context['status'] = 0
			context['message'] = 'Invalid Credentials.'
			context['response'] = 'Error'
			return Response(context,status=HTTP_203_NON_AUTHORITATIVE_INFORMATION)

		return Response(context,status=HTTP_202_ACCEPTED)




@api_view(['GET', ])
@permission_classes([])
@authentication_classes([])
def does_account_exist_view(request):
	data = {}	
	email = request.data.get('email')
	try:
		try:
			allUsers = Account.objects.get(email=email)
			data['status'] = 1
			data['email'] = email
			data['username'] = allUsers.username
			data['id'] = allUsers.pk
		except Account.DoesNotExist:
			data['response'] = 0
			return Response(data)
		return Response(data)
	except:
		data['response'] = "Error"
		return Response(data)



class ChangePasswordView(UpdateAPIView):

	serializer_class = ChangePasswordSerializer
	model = Account
	permission_classes = (IsAuthenticated,)
	authentication_classes = (TokenAuthentication,)

	def get_object(self, queryset=None):
		obj = self.request.user
		return obj

	def update(self, request, *args, **kwargs):
		self.object = self.get_object()
		serializer = self.get_serializer(data=request.data)

		if serializer.is_valid():
			# Check old password
			if not self.object.check_password(serializer.data.get("old_password")):
				return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

			# confirm the new passwords match
			new_password = serializer.data.get("new_password")
			confirm_new_password = serializer.data.get("confirm_new_password")
			if new_password != confirm_new_password:
				return Response({"new_password": ["New passwords must match"]}, status=status.HTTP_400_BAD_REQUEST)

			# set_password also hashes the password that the user will get
			self.object.set_password(serializer.data.get("new_password"))
			self.object.save()
			return Response({"response":"successfully changed password"}, status=status.HTTP_200_OK)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileAccountUploadView(APIView):
    parser_class = (FileUploadParser,)
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)

    def post(self, request, *args, **kwargs):
        data = {}
        file_serializer = ImagesSerializer(data=request.data)
        idProd = request.data.get('AccId')
		
        pkInProduk = Account.objects.get(id=idProd)
        if(pkInProduk.id == request.user.id):
			
            if file_serializer.is_valid():
                file_serializer.save()
                data["status"] = 1
                data["response"] = "succes upload"
                return Response(data, status=status.HTTP_201_CREATED)
            else:
                return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            data["status"] = 0
            data["response"] = "UNAUTHORIZED"
            return Response(data,status=status.HTTP_401_UNAUTHORIZED)