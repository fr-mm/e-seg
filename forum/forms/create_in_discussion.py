from django.forms import ModelForm

from forum.models import Discussion


class CreateInDiscussion(ModelForm):
    class Meta:
        model = Discussion
        fields = "__all__"
