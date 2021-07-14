from django.contrib import admin
from .models import Feedback
from .models import contact

from .models import maruti_arena
from .models import maruti_nexa
from .models import tata_moter
from .models import jaguar_moter
from .models import mahindra_moter

from.models import Sell_Car_details
from.models import hundai_moter
from.models import honda_moter
from.models import ford_moter
from.models import renult_moter
from.models import nissan_moter



# Register your models here.
admin.site.register(contact)
admin.site.register(Feedback)

admin.site.register(Sell_Car_details)

admin.site.register(maruti_arena)
admin.site.register(maruti_nexa)
admin.site.register(tata_moter)
admin.site.register(jaguar_moter)
admin.site.register(mahindra_moter)
admin.site.register(hundai_moter)
admin.site.register(honda_moter)
admin.site.register(ford_moter)
admin.site.register(renult_moter)
admin.site.register(nissan_moter)
