# django-admin
for microservice admin

- name: path to django-app
- db: db-alias-name, {db.upper}_DATABASE_URL reffered

``` yaml
version: '3.5'

services:
  ...

  django-admin-db:
    image: postgres:14
    environment:
      - POSTGRES_USER=psqluser
      - POSTGRES_PASSWORD=psqlpass
      - POSTGRES_DB=admin
      - PGDATA=/postgres/data
    volumes:
      - admin-pg-data:/postgres/data

  django-admin:
    image: s1s5/django-admin
    environment:
      DATABASE_URL: psql://psqluser:psqlpass@django-admin-db/admin
      MICROSERVICE_DATABASE_URL: psql://psqluser:psqlpass@microservice-db/ms
      APPS: |
        - name: mymod.myapp0
          db: microservice
        - name: mymod.myapp1
          db: microservice
    volumes:
      - .:/app/admin/mymod
    ports:
      - "15301:8000"
    depends_on:
      - ms-db
      - django-admin-db

volumes:
  ...
  admin-pg-data:
```
