from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('CreateAccount/',views.register,name='register'),
    path('options',views.options),
    path('upload/',views.upload,name='upload'),
    path('upload/sendvac',views.sendvac),
    path('viewvac',views.viewvac,name='viewvacancies'),
    path('select',views.select,name='selectapplicants'),
    path('upload/viewvac',views.viewvac),
    path('recruitedfaculty/',views.recruitedfaculty,name='recruitedfaculty'),
    path('upload/recruitedfaculty',views.recruitedfaculty),
]