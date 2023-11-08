from django import forms
from app2.models import Ignitz
from app2.models import Attendance
from app2.models import Login,StudentPassword
from django.contrib.auth.forms import AuthenticationForm



class RegistrationForm(forms.ModelForm):
    class Meta:
        model=Ignitz
        fields='__all__'

        
class AttendanceForm(forms.ModelForm):

    class Meta:
        model=Attendance
        fields='__all__'


# class LoginForm(forms.ModelForm):

#     class Meta:
#         model=Login
#         fields='__all__'

class LoginForm(AuthenticationForm):
    class Meta:
        model=Login
        fields='__all__'
class StdPasswordForm(forms.ModelForm):
    class Meta:
        model=StudentPassword
        fields='__all__'
    def clean(self):
        total_cleaned_data=super().clean()
        passw=total_cleaned_data['password']
        cPassw=total_cleaned_data['confim_password']
        if passw!=cPassw:
            raise forms.ValidationError("both password must be same")        
        if len(passw)<7:
            raise forms.ValidationError("password must be min 8characters")

# class LoginForm(forms.Form):
#     Mail_Id = forms.EmailField()
#     Password = forms.CharField(max_length=100, widget=forms.PasswordInput)
# class StdLoginForm(forms.ModelForm):
#     class Meta:
#         model=StdLogin
#         fields='__all__'