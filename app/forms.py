
from django import forms
from .models import Article, Profile
from django.contrib.auth.models import User

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article

        fields = [
            "title",
            "text"
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": (
                        "w-full px-4 py-3 "
                        "bg-white "
                        "border-2 border-[#101010] "
                        "rounded-xl "
                        "font-['Inter'] "
                        "text-[#101010] "
                        "outline-none "
                        "transition-all duration-300 "
                        "focus:border-[#DDF918] "
                        "focus:ring-2 focus:ring-[#DDF918]"
                    ),
                    "placeholder": "Enter article title",
                }
            ),

            "text": forms.Textarea(
                attrs={
                    "class": (
                        "w-full px-4 py-3 "
                        "bg-white "
                        "border-2 border-[#101010] "
                        "rounded-xl "
                        "font-['Inter'] "
                        "text-[#101010] "
                        "outline-none "
                        "min-h-40 "
                        "resize-y "
                        "transition-all duration-300 "
                        "focus:border-[#DDF918] "
                        "focus:ring-2 focus:ring-[#DDF918]"
                    ),
                    "placeholder": "Enter article text",
                }
            ),
        }

class RegistrationForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": (
                    "w-full px-4 py-3 "
                    "bg-white "
                    "border-2 border-[#101010] "
                    "rounded-xl "
                    "font-['Inter'] "
                    "text-[#101010] "
                    "outline-none "
                    "transition-all duration-300 "
                    "focus:border-[#DDF918] "
                    "focus:ring-2 focus:ring-[#DDF918]"
                ),
                "placeholder": "Enter username",
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": (
                    "w-full px-4 py-3 "
                    "bg-white "
                    "border-2 border-[#101010] "
                    "rounded-xl "
                    "font-['Inter'] "
                    "text-[#101010] "
                    "outline-none "
                    "transition-all duration-300 "
                    "focus:border-[#DDF918] "
                    "focus:ring-2 focus:ring-[#DDF918]"
                ),
                "placeholder": "Enter email",
            }
        )
    )

    password = forms.CharField(
        min_length=4,
        widget=forms.PasswordInput(
            attrs={
                "class": (
                    "w-full px-4 py-3 "
                    "bg-white "
                    "border-2 border-[#101010] "
                    "rounded-xl "
                    "font-['Inter'] "
                    "text-[#101010] "
                    "outline-none "
                    "transition-all duration-300 "
                    "focus:border-[#DDF918] "
                    "focus:ring-2 focus:ring-[#DDF918]"
                ),
                "placeholder": "Enter password",
            }
        )
    )

    password_confirmation = forms.CharField(
        min_length=4,
        widget=forms.PasswordInput(
            attrs={
                "class": (
                    "w-full px-4 py-3 "
                    "bg-white "
                    "border-2 border-[#101010] "
                    "rounded-xl "
                    "font-['Inter'] "
                    "text-[#101010] "
                    "outline-none "
                    "transition-all duration-300 "
                    "focus:border-[#DDF918] "
                    "focus:ring-2 focus:ring-[#DDF918]"
                ),
                "placeholder": "Confirm password",
            }
        )
    )

    def clean(self):
        password = self.cleaned_data.get("password")
        password_confirmation = self.cleaned_data.get("password_confirmation")

        if password != password_confirmation:
            raise forms.ValidationError("Пароли не совпадают")

        return self.cleaned_data

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists!")
        return username

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50,
                               widget=forms.TextInput(
                                   attrs={
                                       "class": (
                                           "w-full px-4 py-3 "
                                           "bg-white "
                                           "border-2 border-[#101010] "
                                           "rounded-xl "
                                           "font-['Inter'] "
                                           "text-[#101010] "
                                           "outline-none "
                                           "transition-all duration-300 "
                                           "focus:border-[#DDF918] "
                                           "focus:ring-2 focus:ring-[#DDF918]"
                                       ),
                                       "placeholder": "Enter username",
                                   }
                               )
                               )
    password = forms.CharField(min_length=4,
                               widget=forms.PasswordInput(
                                   attrs={
                                       "class": (
                                           "w-full px-4 py-3 "
                                           "bg-white "
                                           "border-2 border-[#101010] "
                                           "rounded-xl "
                                           "font-['Inter'] "
                                           "text-[#101010] "
                                           "outline-none "
                                           "transition-all duration-300 "
                                           "focus:border-[#DDF918] "
                                           "focus:ring-2 focus:ring-[#DDF918]"
                                       ),
                                       "placeholder": "Enter password",
                                   }
                               )
                               )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["avatar", "bio"]

        widgets = {
            "avatar": forms.ClearableFileInput(
                attrs={
                    "id": "id_avatar",
                    "accept": "image/*",
                    "class": "hidden",
                }
            ),

            "bio": forms.Textarea(
                attrs={
                    "class": (
                        "w-full px-4 py-3 "
                        "bg-white "
                        "border-2 border-[#101010] "
                        "rounded-xl "
                        "font-['Inter'] "
                        "text-[#101010] "
                        "outline-none "
                        "min-h-40 "
                        "resize-y "
                        "transition-all duration-300 "
                        "focus:border-[#DDF918] "
                        "focus:ring-2 focus:ring-[#DDF918]"
                    ),
                    "placeholder": "Tell something about yourself...",
                }
            ),
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username"]
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": (
                    "w-full px-4 py-3 "
                    "bg-white "
                    "border-2 border-[#101010] "
                    "rounded-xl "
                    "font-['Inter'] "
                    "text-[#101010] "
                    "outline-none "
                    "transition-all duration-300 "
                    "focus:border-[#DDF918] "
                    "focus:ring-2 focus:ring-[#DDF918]"
                    ),
                    "placeholder": "Enter username",

                }
            )
        }