from my_auth.models import User

# Create a superuser
User.objects.create_superuser(
    username='Admin',
    email='ole.karlsen@gmail.com',
    password='adminadmin')

# Create test users
User.objects.create_user(
    username = 'ole',
    password = 'Tonsberg01!',
    email = 'ole.karlsen@gmail.com',
    is_superuser = False,
    is_active = True,
    is_staff = True
)