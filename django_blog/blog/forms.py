from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Post, Comment
from taggit.models import Tag


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Email is already in use.")
        return email
    



class PostForm(forms.ModelForm):
    tags_csv = forms.CharField(
        required=False,
        help_text="Comma-separated tags, e.g. django, api, tips",
        widget=forms.TextInput(attrs={'placeholder': 'e.g. django, api, tips'})
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags_csv']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            # Prefill tags_csv with tag names
            current_tags = self.instance.tags.names()
            self.fields['tags_csv'].initial = ', '.join(current_tags)

    def clean_tags_csv(self):
        raw = self.cleaned_data.get('tags_csv', '')
        # Split, strip, remove empties, dedupe
        parts = [t.strip() for t in raw.split(',') if t.strip()]
        seen = set()
        dedup = []
        for p in parts:
            key = p.lower()
            if key not in seen:
                seen.add(key)
                dedup.append(p)
        return dedup  # list of tag strings

    def save(self, commit=True):
        instance = super().save(commit=commit)
        tags_list = self.cleaned_data.get('tags_csv', [])

        if tags_list:
            # Correctly set tags with a list of strings
            instance.tags.set(tags_list)
        else:
            instance.tags.clear()

        if commit:
            instance.save()
        return instance

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio", "image"]




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a comment...'}),
        }