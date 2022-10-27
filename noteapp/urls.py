from django.urls import path,include
from .views import  MyLoginView, NoteDelete, NoteList, NoteDetail, NoteCreate, NoteUpdate, RegisterPage
from django.contrib.auth.views import LogoutView
from .api import RegisterAPI, LoginAPI, UserAPI
from knox import views as knox_views
from rest_framework import routers
from .api import NoteViewSet


router = routers.DefaultRouter()
router.register('notes', NoteViewSet, 'notes')


urlpatterns = [
    path('login/',MyLoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('',NoteList.as_view(), name='notes'),
    path('note/<int:pk>/',NoteDetail.as_view(), name='note'),
    path('create-note/',NoteCreate.as_view(), name='note-create'),
    path('note-update/<int:pk>/',NoteUpdate.as_view(), name='note-update'),
    path('note-delete/<int:pk>/',NoteDelete.as_view(), name='note-delete'),

    path('auth', include('knox.urls')),
    path('auth/register', RegisterAPI.as_view()),
    path('auth/login', LoginAPI.as_view()),
    path('auth/user', UserAPI.as_view()),
    path('auth/logout', knox_views.LogoutView.as_view(), name="knox_logout")
]

urlpatterns += router.urls
