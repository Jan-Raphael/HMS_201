# hospital/forms.py
from django import forms
from .models import Patient, Appointment


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'middle_name', 'last_name', 'date_of_birth', 'gender', 'phone_number', 'address']


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['appointment_date', 'reason']


class AppointmentBookingForm(forms.Form):
    # Patient fields
    first_name = forms.CharField(max_length=100, label='First Name')
    middle_name = forms.CharField(max_length=100, required=False, label='Middle Name')
    last_name = forms.CharField(max_length=100, label='Last Name')
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Date of Birth')
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')], label='Gender')
    phone_number = forms.CharField(max_length=15, label='Phone Number')
    address = forms.CharField(widget=forms.Textarea, label='Address')

    # Appointment fields
    appointment_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
                                           label='Appointment Date and Time')
    reason = forms.CharField(widget=forms.Textarea, label='Reason for Appointment')

    def save(self):
        # Extract patient details and create a new Patient object
        patient_data = {
            'first_name': self.cleaned_data['first_name'],
            'middle_name': self.cleaned_data['middle_name'],
            'last_name': self.cleaned_data['last_name'],
            'date_of_birth': self.cleaned_data['date_of_birth'],
            'gender': self.cleaned_data['gender'],
            'phone_number': self.cleaned_data['phone_number'],
            'address': self.cleaned_data['address'],
        }

        patient, created = Patient.objects.get_or_create(**patient_data)

        # Create the appointment
        Appointment.objects.create(
            patient=patient,
            appointment_date=self.cleaned_data['appointment_date'],
            reason=self.cleaned_data['reason']
        )
