# Generated by Django 2.1.7 on 2019-02-18 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('serialNumber', models.TextField(primary_key=True, serialize=False)),
                ('mac', models.TextField()),
                ('apGroupName', models.TextField(null=True)),
                ('deviceDescription', models.TextField(null=True)),
                ('deviceFullName', models.TextField(null=True)),
                ('deviceName', models.TextField(null=True)),
                ('firstSeen', models.TextField(null=True)),
                ('folder', models.TextField(null=True)),
                ('folderId', models.TextField(null=True)),
                ('inventoryDate', models.TextField(null=True)),
                ('lastAosVersion', models.TextField(null=True)),
                ('lastBootVersion', models.TextField(null=True)),
                ('lastSeen', models.TextField(null=True)),
                ('partCategory', models.TextField(null=True)),
                ('sourceIpAddress', models.TextField(null=True)),
                ('status', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('partNumber', models.TextField(primary_key=True, serialize=False)),
                ('image_path', models.TextField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='partNumber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search.Image'),
        ),
    ]