# hospital/urls.py
from django.urls import path

from .forms import AppointmentBookingForm
from .views import viewpage, homepage, PatientListView, DoctorListView, MakeAppointmentView, AppointmentBookingView, logview

urlpatterns = [
    path('signup/',viewpage,name="viewpage"),
    path('login/',logview,name="logview"),
    path('', homepage, name='homepage'),
    path('patients/', PatientListView.as_view(), name='patient_list'),
    path('doctors/', DoctorListView.as_view(), name='doctor_list'),
    path('make-appointment/', MakeAppointmentView.as_view(), name='make_appointment'),


    path('book-appointment/', AppointmentBookingView.as_view(), name='book_appointment'),
]
