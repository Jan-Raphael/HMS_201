from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView
from .models import Patient, Doctor, Appointment
from .forms import AppointmentForm, AppointmentBookingForm

def homepage(request):
    return render(request, 'myapp/homepage.html')

def viewpage(request):
    return render(request, "myapp/form_validation.html")

def logview(request):
    return render(request, "myapp/login.html")

class PatientListView(ListView):
    model = Patient
    template_name = 'myapp/patient_list.html'
    context_object_name = 'patients'


class DoctorListView(ListView):
    model = Doctor
    template_name = 'myapp/doctor_list.html'
    context_object_name = 'doctors'


class MakeAppointmentView(FormView):
    template_name = 'myapp/make_appointment.html'
    form_class = AppointmentForm
    success_url = reverse_lazy('patient_list')

    def form_valid(self, form):
        # Extract patient and appointment details from cleaned data
        patient = form.cleaned_data.get('patient')
        appointment_date = form.cleaned_data.get('appointment_date')
        reason = form.cleaned_data.get('reason')

        if not patient:
            return self.form_invalid(form)

        # Create and save the appointment
        Appointment.objects.create(
            patient=patient,
            appointment_date=appointment_date,
            reason=reason
        )

        return super().form_valid(form)

    def form_invalid(self, form):
        # Print errors for debugging
        print("Form errors:", form.errors)
        return super().form_invalid(form)


class AppointmentBookingView(FormView):
    template_name = 'myapp/appointment_booking.html'
    form_class = AppointmentBookingForm
    success_url = '/patients/'  # Redirect to the patient list page after submission

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
