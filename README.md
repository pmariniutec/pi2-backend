# Smithsonian Backend

## For now, we only have a production environment

## Dependencies
- PostgreSQL
- Python 3.6
- Django 2.2
- Zappa

## Initial Setup
```bash
# Create user role
psql -U postgres
create role smithsonian with login encrypted password 'smithsonian';
alter user smithsonian createdb;

# Create db
python manage.py create_db
zappa manage production create_db
```

## Create Superuser
```bash
python manage.py createsuperuser
zappa invoke --raw production "from smithsonian.users.models import CustomUser; CustomUser.objects.create_superuser('admin@admin.com', 'admin')"
```

## Deploy
```bash
zappa update production
zappa manage production migrate (if needed)
```
