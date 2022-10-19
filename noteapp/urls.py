from django.urls import path
from .views import  MyLoginView, NoteDelete, NoteList, NoteDetail, NoteCreate, NoteUpdate, RegisterPage
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/',MyLoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('',NoteList.as_view(), name='notes'),
    path('note/<int:pk>/',NoteDetail.as_view(), name='note'),
    path('create-note/',NoteCreate.as_view(), name='note-create'),
     path('note-update/<int:pk>/',NoteUpdate.as_view(), name='note-update'),
     path('note-delete/<int:pk>/',NoteDelete.as_view(), name='note-delete'),
]