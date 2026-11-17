import os
import codecs
from django.db import migrations
from django.core import serializers
from django.conf import settings

def cargar_datos(apps, schema_editor):
    ruta_json = os.path.join(settings.BASE_DIR, 'catalogo', 'fixtures', 'fixtures.json')
    
    with codecs.open(ruta_json, 'r', encoding='utf-8-sig') as f:
        objetos = serializers.deserialize('json', f)
        for obj in objetos:
            obj.save()

class Migration(migrations.Migration):
    dependencies = [
        ('catalogo', '0002_alter_articulo_id_alter_categoria_id'), 
    ]

    operations = [
        migrations.RunPython(cargar_datos),
    ]