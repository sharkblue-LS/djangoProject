from django.test import TestCase
from sign.models import Event,Guest
from django.contrib.auth.models import User


class ModelTest(TestCase):
	def setUp(self):
		Event.objects.create(id=3,name='oneplus 9 event',status=True,limit=2000,address='shenzhen',start_time='2021-07-20 14:00:00')
		Guest.objects.create(id=9,event_id=3,realname='alen',phone='12300000010',email='alen@Django.com',sign=False)
		
	def test_event_models(self):
		result = Event.objects.get(name='oneplus 9 event')
		self.assertEqual(result.address,'beijing')
		self.assertTrue(result.status)
		
	def test_guest_models(self):
		result = Guest.objects.get(phone='12300000010')
		self.assertEqual(result.realname,'alen')
		self.assertFalse(result.sign)
		
class IndexPageTest(TestCase):
	'''测试index登录首页'''
	def test_index_page_renders_index_template(self):
		'''测试index视图'''
		response = self.client.get('/index/')
		self.assertEqual(response.status_code,200)
		self.assertTemplateUsed(response,'index.html')
	
class LoginActionTest(TestCase):
	'''测试登录动作'''
	def setUp(self):
		User.objects.create_user('admin1','admin@mail.com','admin123456')
		
	def test_add_admin(self):
		'''测试添加用户'''
		user = User.objects.get(username='admin1')
		self.assertEqual(user.username,'admin1')
		self.assertEqual(user.email,'admin@mail.com')
		
	def test_login_action_username_password_null(self):
		'''用户名密码为空'''
		test_data = {'username':'','password':''}
		response = self.client.post('/login_action/',data=test_data)
		self.assertEqual(response.status_code,200)
		self.assertIn('username or password error!',response.content)
		
	def test_login_action_username_password_error(self):
		'''用户名密码错误'''
		test_data = {'username':'abc','password':'123'}
		response = self.client.post('/login_action/',data=test_data)
		self.assertEqual(response.status_code,200)
		self.assertIn('username or password error!',response.content)
		
	def test_login_action_success(self):
		'''登录成功'''
		test_data = {'username':'admin1','password':'admin123456'}
		response = self.client.post('/login_action/',data=test_data)
		self.assertEqual(response.status_code,302)

#Create your tests here
