from my_auth.models import User

# Create a superuser
User.objects.create_superuser(
    username='Admin',
    email='ole.karlsen@gmail.com',
    password='adminadmin')

# Create test users
User.objects.create_user(
    username = 'ole',
    password = 'Tonsberg01',
    email = 'ole.karlsen@gmail.com',
    is_superuser = False,
    is_active = True,
    is_staff = True
)

User.objects.create_user(
    username = 'Test1',
    password = 'test1test1',
    email = 'ole.karlsen@gmail.com',
    is_superuser = False,
    is_active = True,
    is_staff = True
)

User.objects.create_user(
    username = 'Test2',
    password = 'test2test2',
    email = 'ole.karlsen@gmail.com',
    is_superuser = False,
    is_active = True,
    is_staff = True
)

User.objects.create_user(
    username = 'Test3',
    password = 'test3test3',
    email = 'ole.karlsen@gmail.com',
    is_superuser = False,
    is_active = True,
    is_staff = True
)