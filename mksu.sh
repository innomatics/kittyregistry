python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin@local.test', password='password123', email='')" | python manage.py shell
