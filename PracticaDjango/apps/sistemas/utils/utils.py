from django.core.validators import RegexValidator

phone_regex = RegexValidator(regex=r'^\d{8,14}((,\d{8,14})?)*$',
                             message="El formato del teléfono debe ser: '9998888777', sin código de país. De 8-14 "
                                       "dígitos permitidos. Puede agregar más telefonos seperados por coma.")

