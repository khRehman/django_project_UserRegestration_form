from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from platformdirs import user_cache_dir

class Sign_up(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email':'Email'}
