from django.forms import ModelForm

from forum.models import Forum


class CreateInForum(ModelForm):
    class Meta:
        model = Forum
        fields = "__all__"
