from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_mealdonation'),
    ]

    operations = [
        migrations.CreateModel(
            name='MealDonationRecipient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('address', models.TextField(blank=True)),
                # add more fields if needed
            ],
        ),
    ]
