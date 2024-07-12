from typing import Any
from django import forms
from identity.models import WorkitUser
from django.utils.translation import gettext_lazy as _


# <input type="file" class="form-control d-none" id="profile_image" onchange="displaySelectedImage(event, 'selectedAvatar')" name="profile_image" />
class ProfileForm(forms.ModelForm):
    class Meta:
        model = WorkitUser
        fields = ["first_name", "last_name", "gender", "profile_image"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
        }


class ChangePasswordForm(forms.ModelForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "id": "old_password"}
        )
    )
    new_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "id": "new_password"}
        )
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "id": "confirm_password"}
        )
    )

    class Meta:
        model = WorkitUser
        fields = ["old_password", "new_password", "confirm_password"]

    def clean_old_password(self):
        old_password = self.cleaned_data.get("old_password")
        user: WorkitUser = self.instance
        if not user.check_password(old_password):
            raise forms.ValidationError(_("Ancien mot de passe incorrect"))
        return old_password

    def clean(self) -> dict[str, Any]:
        confirm_password = self.cleaned_data.get("confirm_password")
        new_password = self.cleaned_data.get("new_password")

        if confirm_password != new_password:
            raise forms.ValidationError({"new_password": _("Confirmer mot de passe")})

    def save(self, commit: bool = ...) -> Any:
        new_password = self.cleaned_data.get("new_password")
        user: WorkitUser = self.instance
        user.set_password(new_password)
        user.save()
        return user
