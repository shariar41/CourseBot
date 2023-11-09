from django.contrib.auth.views import LoginView
from django.urls import include, path

from knox import views as knox_views
from .views import CreateUserView, LoginView, ManageUserView

urlpatterns = [
    path('',include('rest_framework.urls', namespace='rest_framework')),
    # path('register/', RegisterAPI.as_view()),
    # path('user/', UserAPI.as_view()),
    # path('login/',
    #      LoginView.as_view
    #      (
    #          template_name='app/login.html',
    #          authentication_form= forms.BootstrapAuthenticationForm,
    #          extra_context=
    #          {
    #              'title': 'Log in',
    #              'year' : datetime.now().year,
    #          }
    #      ),
    #      name='login'),
    # path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    # path('auth-token/', views.obtain_auth_token)
    path('create/', CreateUserView.as_view(), name="create"),
    path('profile/', ManageUserView.as_view(), name='profile'),
    path('login/', LoginView.as_view(), name='knox_login'),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
]