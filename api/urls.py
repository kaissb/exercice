from django.urls import path
from knox import views as knox_views
from . import views

urlpatterns = [
    path('',views.apiOverview, name='api-overview'),
    path('userlogin/',views.userlogin, name="userlogin"),
    path('userregister/',views.userregister, name="userregister"),
    path('userlogout/',knox_views.LogoutView.as_view(), name="userlogout"),
    path('listenote/',views.NoteList, name="listnote"),
    path('detailnote/<str:pk>',views.NoteDetail, name="detailnote"),
    path('addnote',views.addNote, name="addnote"),
    path('updatenote',views.updateNote, name="updatenote"),
    path('deletenote/<str:pk>',views.NoteDetail, name="deletenote"),

]