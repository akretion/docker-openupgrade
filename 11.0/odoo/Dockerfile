FROM ghcr.io/camptocamp/odoo-project:11.0-latest-batteries

RUN rm /etc/apt/sources.list
COPY sources.list /etc/apt/sources.list

RUN DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y git vim libpq5=12.12-0ubuntu0.20.04.1 libpq-dev && \
    apt-get upgrade -y && \
    /install/dev_package.sh && \
    pip install psycopg2 --upgrade && \
    apt-get clean

COPY ./src /odoo/src
RUN pip install -e /odoo/src

# generate oca requirement with
# find odoo/external-src/ -name 'requirements.txt' -exec cat {} \; > odoo/oca_requirements.txt
# then remove duplicate

COPY ./oca_requirements.txt /odoo/oca_requirements.txt
RUN pip install -r /odoo/oca_requirements.txt

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

ENV ADDONS_PATH=/odoo/links,/odoo/local-src,/odoo/src/odoo/addons,/odoo/src/addons,/odoo/external-src/account-financial-reporting,/odoo/external-src/account-financial-tools,/odoo/external-src/account-fiscal-rule,/odoo/external-src/account-invoice-reporting,/odoo/external-src/account-invoicing,/odoo/external-src/account-payment,/odoo/external-src/account-reconcile,/odoo/external-src/bank-payment,/odoo/external-src/bank-statement-import,/odoo/external-src/community-data-files,/odoo/external-src/connector,/odoo/external-src/connector-ecommerce,/odoo/external-src/connector-telephony,/odoo/external-src/contract,/odoo/external-src/crm,/odoo/external-src/delivery-carrier,/odoo/external-src/e-commerce,/odoo/external-src/edi,/odoo/external-src/hr,/odoo/external-src/hr-timesheet,/odoo/external-src/intrastat,/odoo/external-src/l10n-france,/odoo/external-src/l10n-brazil,/odoo/external-src/manufacture,/odoo/external-src/partner-contact,/odoo/external-src/pos,/odoo/external-src/product-attribute,/odoo/external-src/product-variant,/odoo/external-src/project,/odoo/external-src/project-reporting,/odoo/external-src/purchase-reporting,/odoo/external-src/purchase-workflow,/odoo/external-src/reporting-engine,/odoo/external-src/sale-financial,/odoo/external-src/sale-reporting,/odoo/external-src/queue,/odoo/external-src/sale-workflow,/odoo/external-src/server-auth,/odoo/external-src/server-tools,/odoo/external-src/server-ux,/odoo/external-src/social,/odoo/external-src/stock-logistics-barcode,/odoo/external-src/stock-logistics-reporting,/odoo/external-src/stock-logistics-warehouse,/odoo/external-src/stock-logistics-workflow,/odoo/external-src/web
