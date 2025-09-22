from django.contrib import admin

# Register your models here.
from .models import Child,Sponsor
from .models import OldAgePerson,OldAgeNeed
from .models import MealDonation
from .models import DemoClassRegistration
from .models import GeneralChildNeed
class DemoClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'skills')
from .models import GeneralChildNeed

admin.site.register(GeneralChildNeed)
from .models import GeneralDonation
class GeneralDonationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'delivery', 'submitted_at')
admin.site.register(GeneralDonation)


admin.site.register(DemoClassRegistration, DemoClassAdmin)

admin.site.register(MealDonation)

admin.site.register(Child)
admin.site.register(OldAgePerson)
admin.site.register(Sponsor)
admin.site.register(OldAgeNeed)

from .models import ContactMessage

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'contact_number', 'submitted_at')

admin.site.register(ContactMessage, ContactMessageAdmin)


from .models import GalleryImage

admin.site.register(GalleryImage)
