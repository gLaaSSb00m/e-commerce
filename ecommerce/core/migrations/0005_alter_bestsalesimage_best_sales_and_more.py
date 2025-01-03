# Generated by Django 5.1.1 on 2024-11-22 10:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_bestsales_bestsalesimage_blog_firstbanner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bestsalesimage',
            name='best_sales',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='core.bestsales'),
        ),
        migrations.AlterField(
            model_name='newarivalimage',
            name='new_arival',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='core.newarival'),
        ),
        migrations.AlterField(
            model_name='secondbannerimage',
            name='second_banner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='core.secondbanner'),
        ),
        migrations.AlterField(
            model_name='thirdbannerimage',
            name='third_banner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='core.thirdbanner'),
        ),
    ]
