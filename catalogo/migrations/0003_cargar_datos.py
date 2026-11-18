from django.db import migrations, models
from django.core.management import call_command

def cargar_datos(apps, schema_editor):
    call_command('loaddata', 'fixtures', verbosity=0)

class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_alter_articulo_id_alter_categoria_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='articulos/'),
        ),
        migrations.RunPython(cargar_datos),
    ]