from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Post, Comment, Tag


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
    # free-text comma-separated input
    tags_csv = forms.CharField(
        required=False,
        help_text="Comma-separated tags, e.g. django, api, tips",
        widget=forms.TextInput(attrs={'placeholder': 'e.g. django, api, tips'})
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags_csv']  # 'tags' handled via tags_csv

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Prefill tags_csv on edit
        if self.instance.pk:
            current = self.instance.tags.values_list('name', flat=True)
            self.fields['tags_csv'].initial = ', '.join(current)

    def clean_tags_csv(self):
        raw = self.cleaned_data.get('tags_csv', '')
        # normalize: split, strip, remove empties & dedupe (case-insensitive)
        parts = [t.strip() for t in raw.split(',') if t.strip()]
        dedup = []
        seen = set()
        for p in parts:
            key = p.lower()
            if key not in seen:
                seen.add(key)
                dedup.append(p)
        return dedup

    def save(self, commit=True):
        instance = super().save(commit=commit)
        # Attach tags after instance exists
        tags_list = self.cleaned_data.get('cleaned_tags', None)
        if tags_list is None:
            tags_list = self.cleaned_data.get('tags_csv', [])
        tag_objs = []
        for name in tags_list:
            tag, _ = Tag.objects.get_or_create(name=name)
            tag_objs.append(tag)
        # set many-to-many
        # If commit=False on first save, we need instance.save() before m2m
        if not instance.pk:
            instance.save()
        instance.tags.set(tag_objs)
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