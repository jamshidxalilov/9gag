from django import forms
from django.utils.translation import gettext_lazy as _
from main.models import PostComment


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ['comment', 'image']
        labels = {
            'comment': _("Izoh"),
            'image': _("Rasm")
        }
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 2})
        }