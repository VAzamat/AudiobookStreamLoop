# AudiobookStreamLoop
Добро пожаловать в Audiobook Stream Loop. Здесь границы между реальностями стираются, а одна история становится началом следующей. Исследуй бесконечный поток лучших книг в цифровом воплощении. Это твоя личная подборка легенд «Тысячи и одной ночи», которая станет идеальным спутником твоего дня.

### fill database
dump into backup file
```bash
python manage.py dumpdata sonicgrid --indent 3 -o sonicgrid/db/sonicgrid_backup.json 
```

load into database from backup file
```bash
python manage.py loaddata sonicgrid/db/sonicgrid_backup.json
```

fill the database with parsing sonicgrid/db/*/*.html using
 code written in sonicgrid/management/commands/fill.py
```bash
python manage.py fill
```

