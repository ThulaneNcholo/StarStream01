
from django.urls import path
from .import views

urlpatterns = [
    path('',views.LandingPage,name='landing-page'),
    path('index',views.IndexView,name='index'),
    path('category',views.CategoryResults,name='category'),
    path('profile/<int:id>',views.Profile,name='profile'),
    path('user-profile',views.UserProfile,name='user-profile'),
    path('trending',views.TrendingCelebs,name='trending'),
    path('sign-up',views.SignUpPage,name='sign-up'),
    path('complete',views.successfulPage,name='complete'),
]

