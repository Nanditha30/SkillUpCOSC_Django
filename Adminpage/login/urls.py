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
<<<<<<< HEAD
    path('optionsP',views.optionsp),
=======
    path('recruitedfaculty/',views.recruitedfaculty,name='recruitedfaculty'),
    path('upload/recruitedfaculty',views.recruitedfaculty),
>>>>>>> ad45de80bb0e98a64be364d61edaf3ddbf0ddc65
]