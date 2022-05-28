from django.forms import ModelForm, CharField, DateTimeField
from .models import Task


class AddTodoForm(ModelForm):
    description = CharField(max_length=255)

    class Meta:
        model = Task
        fields = ['name', 'description', 'expire_date', 'priority', 'is_completed']

