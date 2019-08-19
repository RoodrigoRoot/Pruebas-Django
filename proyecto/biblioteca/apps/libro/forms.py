from django.db import form
from .models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['nombre','apellidos','nacionalidad','descripcion']