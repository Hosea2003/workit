from django import forms

from identity.models import WorkitUser


# <input type="file" class="form-control d-none" id="profile_image" onchange="displaySelectedImage(event, 'selectedAvatar')" name="profile_image" />
class ProfileForm(forms.ModelForm):
    class Meta:
        model = WorkitUser
        fields = ["first_name", "last_name", "gender", "profile_image"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
        }
