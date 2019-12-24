from rest_framework import serializers
from .models import Account
from products.serializers import ProductSerializer


class RegistrationSerializer(serializers.ModelSerializer):

	password2 				= serializers.CharField(style={'input_type': 'password'}, write_only=True)

	class Meta:
		model = Account
		fields = ['email', 'username', 'password', 'password2', 'nik', 'name','address','phone']
		extra_kwargs = {
				'password': {'write_only': True},
		}	


	def	save(self):

		account = Account(
					email=self.validated_data['email'],
					username=self.validated_data['username']
				)
		password = self.validated_data['password']
		password2 = self.validated_data['password2']
		if password != password2:
			raise serializers.ValidationError({'password': 'Passwords must match.'})
		account.set_password(password)
		account.phone = self.validated_data['phone']
		account.name = self.validated_data['name']
		account.address = self.validated_data['address']
		account.nik = self.validated_data['nik']
		account.role = 1
		account.save()
		return account

class RegistrationVendorSerializer(serializers.ModelSerializer):

	password2 				= serializers.CharField(style={'input_type': 'password'}, write_only=True)

	class Meta:
		model = Account
		fields = ['email', 'username', 'password', 'password2', 'nik', 'name','address','phone','role']
		extra_kwargs = {
				'password': {'write_only': True},
		}	


	def	save(self):

		account = Account(
					email=self.validated_data['email'],
					username=self.validated_data['username']
				)
		password = self.validated_data['password']
		password2 = self.validated_data['password2']
		if password != password2:
			raise serializers.ValidationError({'password': 'Passwords must match.'})
		account.set_password(password)
		account.phone = self.validated_data['phone']
		account.name = self.validated_data['name']
		account.address = self.validated_data['address']
		account.nik = self.validated_data['nik']
		account.role = 2
		account.save()
		return account

class RegistrationStoreSerializer(serializers.ModelSerializer):

	password2 				= serializers.CharField(style={'input_type': 'password'}, write_only=True)

	class Meta:
		model = Account
		fields = ['email', 'username', 'password', 'password2', 'nik', 'name','address','phone']
		extra_kwargs = {
				'password': {'write_only': True},
		}	


	def	save(self):

		account = Account(
					email=self.validated_data['email'],
					username=self.validated_data['username']
				)
		password = self.validated_data['password']
		password2 = self.validated_data['password2']
		if password != password2:
			raise serializers.ValidationError({'password': 'Passwords must match.'})
		account.set_password(password)
		account.phone = self.validated_data['phone']
		account.name = self.validated_data['name']
		account.address = self.validated_data['address']
		account.nik = self.validated_data['nik']
		account.role = 3
		account.save()
		return account


class AccountPropertiesSerializer(serializers.ModelSerializer):
	allProduct = ProductSerializer(many=True, read_only=True)
	class Meta:
		model = Account
		fields = ['id', 'email', 'role','username', 'date_joined','last_login','nik','name','address','phone','image','allProduct']

class AccountAllPropertiesSerializer(serializers.ModelSerializer):

	allProduct = ProductSerializer(many=True, read_only=True)
	class Meta:
		model = Account
		fields = ['id', 'email','nik','name','address','phone','image', 'allProduct']




class ChangePasswordSerializer(serializers.Serializer):

	old_password 				= serializers.CharField(required=True)
	new_password 				= serializers.CharField(required=True)
	confirm_new_password 		= serializers.CharField(required=True)