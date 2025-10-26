from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_blank(value):
    if value == "" or not value.strip():
        raise ValidationError(
            _("El nombre no puede estar vacío o contener solo espacios ❗."),
            params={"value": value},
        )
    
def validate_character(value):
    if len(value.strip()) < 30:
        raise ValidationError(
            _("El resumen como mínimo debe poseer 30 caracteres 🥀."),
            params={"value": value},
        )
    
def validate_calification(value):
    if value < 1 or value > 5:
        raise ValidationError(
            _("Solo se puede calificar en el rango de 1 a 5 estrellas 🌟."),
            params={"value": value},
        )