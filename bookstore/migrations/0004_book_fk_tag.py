# Generated by Django 5.0.2 on 2024-02-26 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0003_tag_order_fk_book_order_fk_customer_order_fk_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='fk_tag',
            field=models.ManyToManyField(to='bookstore.tag'),
        ),
    ]