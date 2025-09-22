from django.db import models



class Child(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    admission_date = models.DateField()
    photo = models.ImageField(upload_to='children/')
    background_info = models.TextField(blank=True)

    def __str__(self):
        return self.name


class OldAgePerson(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='elders/')
    description = models.TextField(blank=True)
    suffering_from = models.CharField(max_length=255, help_text="Health issues or conditions")
    medical_expenses = models.DecimalField(max_digits=10, decimal_places=2, help_text="Monthly medicine expenses (INR)")

    def __str__(self):
        return self.name



class MealDonation(models.Model):
    donor_name = models.CharField(max_length=100)
    donor_email = models.EmailField()
    donor_phone = models.CharField(max_length=15)
    donation_date = models.DateField()
    occasion = models.CharField(max_length=100, blank=True)
    meal_time = models.CharField(max_length=20)
    combo = models.CharField(max_length=200)
    recipient = models.TextField(blank=True)

    class Meta:
        unique_together = ('donation_date', 'meal_time')  # ✅ prevents duplicates

    def __str__(self):
        return f"{self.donor_name} - {self.meal_time} on {self.donation_date}"

class Sponsor(models.Model):
    child = models.ForeignKey(Child, on_delete=models.SET_NULL, null=True, blank=True)
    donor_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15) 
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    message = models.TextField(blank=True)
    donated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.donor_name} → {self.child if self.child else 'General'}"

# models.py

class OldAgeNeed(models.Model):
    item = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50, blank=True)
    note = models.TextField(blank=True)

    def __str__(self):
        return f"{self.item} - {self.quantity}"

class DemoClassRegistration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    skills = models.TextField()
    message = models.TextField()
    registered_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class GeneralChildNeed(models.Model):
    item_name = models.CharField(max_length=200)
    description = models.TextField()
    quantity_needed = models.CharField(max_length=100)

    def __str__(self):
        return self.item_name



class GeneralDonation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField(blank=True, null=True)  # used only in DonationForm
    phone = models.CharField(max_length=15, blank=True, null=True)  # optional, for later use
    items = models.TextField()
    image = models.ImageField(upload_to='donation_images/', blank=True, null=True)
    delivery = models.CharField(max_length=100)  # e.g., "Pickup", "Drop-off"
    amount = models.DecimalField(max_digits=8, decimal_places=2, default=0)  # optional field
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.items}"



class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"



class GalleryImage(models.Model):
    CATEGORY_CHOICES = [
        ('infrastructure', 'Infrastructure'),
        ('children', 'Our Child Pictures'),
        ('oldage', 'Old Age Picks'),
        ('donations', 'Donations'),
    ]

    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='gallery_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.category}"
