# OpenUpgrade from Odoo 9.0 to Odoo 10.0 Docky template

## Install Docker, then docky and ak
```
sudo pip install git+https://github.com/akretion/docky.git@master --upgrade
sudo pip install git+https://github.com/akretion/ak.git@master --upgrade
```

## Clone the project and build it

Clone the repo and then use ak to fetch the required dependencies:
```
git clone https://github.com/akretion/docky-odoo-template.git -b 10.0-OpenUpgrade openupgrade10
cd openupgrade10/odoo
ak build
cd ..
docky build
```

## Load your dump and migrate it

### If you are coming from a previous OpenUpgrade step to version 9.0

Then move your 9.0 database to this new container

```
mv ../openupgrade9/.db .db
mkdir -p data/filestore
mv ../openupgrade9/data/filestore/openupgrade9 data/filestore/openupgrade10
docky run
```

Now, inside the container, create a copy of the 9.0 database on which we will run the migration:
`
```
createdb openupgrade10 -T openupgrade9
time odoo -d openupgrade10 -u all --stop-after-init
```

### If you are starting the process from a 9.0 production database instead

Copy your dump in ```odoo/backup/prod.dump```

Create the filestore directory ```mkdir -p data/filestore```

Copy your filestore in ```./data/filestore/openupgrade10```

Start docky with ```docky run```

Now, inside the container, load your dump as a new database that we will keep for reference
and create a copy of it on which we will run the migration:
```
createdb prod-9.0
time psql prod-9.0 < /odoo/backup/prod.dump
createdb openupgrade10 -T 9.0-prod
time odoo -d openupgrade10 -u all --stop-after-init
```
