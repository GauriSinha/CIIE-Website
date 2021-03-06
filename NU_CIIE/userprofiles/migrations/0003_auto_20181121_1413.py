# Generated by Django 2.0 on 2018-11-21 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0002_auto_20181121_0808'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('event_date', models.DateTimeField()),
                ('time', models.TimeField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='events/media')),
                ('venue', models.CharField(max_length=1024)),
                ('content', models.TextField()),
                ('slug', models.SlugField(max_length=2024, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='events_registered',
            field=models.ManyToManyField(blank=True, to='userprofiles.Event'),
        ),
    ]
