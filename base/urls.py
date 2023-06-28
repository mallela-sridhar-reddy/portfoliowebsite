from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name="home"),
    path('project/<str:pk>', views.projectPage, name="project"),
    path('createProject/', views.createProject, name="createProject"),
    path('editproject/<str:pk>/', views.editProject, name="edit-project"),
    path('inbox/', views.inbox, name="inbox"),
    path('message/<str:pk>/', views.messagePage, name="message"),
    path('skills/', views.addSkills, name="skills"),
    path('endorsements/', views.addEndorsements, name="endorsements"),
    path('donation/', views.buyMeCoffee, name="donation"),
    # path('deleteproject/<str:pk>/', views.deleteProject, name="delete-project"),
]
