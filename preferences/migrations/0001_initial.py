# Generated by Django 3.1.1 on 2020-09-19 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('recette', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aimeOuPas', models.BooleanField()),
                ('ingrediants', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='recette.ingredient')),
            ],
        ),
    ]
