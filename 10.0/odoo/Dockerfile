FROM camptocamp/odoo-project:10.0-latest-batteries

RUN DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y git vim && \
    apt-get clean

COPY ./src /odoo/src
RUN pip install -e /odoo/src

COPY ./requirements.txt /odoo/requirements.txt
RUN pip install -r /odoo/requirements.txt

COPY ./external-src /odoo/external-src
COPY ./local-src /odoo/local-src
COPY ./VERSION /odoo/VERSION
COPY ./setup.py /odoo/setup.py
COPY ./songs /odoo/songs
COPY ./migration.yml /odoo/migration.yml
COPY ./links /odoo/links
RUN pip install -e /odoo

ENV ADDONS_PATH=/odoo/local-src,/odoo/links,/odoo/src/addons,/odoo/external-src/bank-payment,/odoo/external-src/intrastat,/odoo/external-src/web,/odoo/external-src/server-tools,/odoo/external-src/account-invoicing,/odoo/external-src/product-attribute,/odoo/external-src/l10n-france,/odoo/external-src/l10n-brazil,/odoo/external-src/partner-contact
