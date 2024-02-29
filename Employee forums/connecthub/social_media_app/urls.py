from django.urls import path
from  social_media_app import views



urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login_view,name='login_view'),
    path('logout/',views.logout_view,name='logout_view'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('upload_post/', views.upload_posts, name='upload_posts'),
    path('delete_post/<int:post_id>/', views.delete_post_view, name='delete_post_view'),
]

