# OpenUpgrade from Odoo 11.0 to Odoo 12.0 Docky template

## Install Docker, then docky and ak
```
sudo pip install git+https://github.com/akretion/docky.git@master --upgrade
sudo pip install git+https://github.com/akretion/ak.git@master --upgrade
```

## Clone the project and build it

Clone the repo and then use ak to fetch the required dependencies:
```
git clone https://github.com/akretion/docky-odoo-template.git -b 12.0-OpenUpgrade openupgrade12
cd openupgrade12/odoo
ak build
cd ..
docky build
```

## Load your dump and migrate it

### If you are coming from a previous OpenUpgrade step to version 11.0

Then move your 11.0 database to this new container

```
mv ../openupgrade11/.db .db
mkdir -p data/filestore
mv ../openupgrade11/data/filestore/openupgrade11 data/filestore/openupgrade12
docky run
```

Now, inside the container, create a copy of the 11.0 database on which we will run the migration:
`
```
createdb openupgrade12 -T openupgrade11
time odoo -d openupgrade12 -u all --stop-after-init
```

### If you are starting the process from a 11.0 production database instead

Copy your dump in ```odoo/backup/prod.dump```

Create the filestore directory ```mkdir -p data/filestore```

Copy your filestore in ```./data/filestore/openupgrade12```

Start docky with ```docky run```

Now, inside the container, load your dump as a new database that we will keep for reference
and create a copy of it on which we will run the migration:
```
createdb prod-11.0
time psql prod-11.0 < /odoo/backup/prod.dump
createdb openupgrade12 -T 11.0-prod
time odoo -d openupgrade12 -u all --stop-after-init
```
