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
RUN find /odoo/external-src/ -name 'requirements.txt' -exec cat {} \; > /odoo/oca_requirements.txt
RUN pip install -r /odoo/oca_requirements.txt
COPY ./local-src /odoo/local-src
COPY ./VERSION /odoo/VERSION
COPY ./setup.py /odoo/setup.py
COPY ./songs /odoo/songs
COPY ./migration.yml /odoo/migration.yml
COPY ./links /odoo/links
RUN pip install -e /odoo

ENV ADDONS_PATH=/odoo/links,/odoo/local-src,/odoo/src/odoo/addons,/odoo/src/addons,/odoo/external-src/account-financial-reporting,/odoo/external-src/account-financial-tools,/odoo/external-src/account-fiscal-rule,/odoo/external-src/account-invoice-reporting,/odoo/external-src/account-invoicing,/odoo/external-src/account-payment,/odoo/external-src/account-reconcile,/odoo/external-src/bank-payment,/odoo/external-src/bank-statement-import,/odoo/external-src/community-data-files,/odoo/external-src/connector,/odoo/external-src/connector-ecommerce,/odoo/external-src/connector-telephony,/odoo/external-src/contract,/odoo/external-src/crm,/odoo/external-src/delivery-carrier,/odoo/external-src/e-commerce,/odoo/external-src/edi,/odoo/external-src/hr,/odoo/external-src/hr-timesheet,/odoo/external-src/intrastat,/odoo/external-src/l10n-france,/odoo/external-src/l10n-brazil,/odoo/external-src/manufacture,/odoo/external-src/partner-contact,/odoo/external-src/pos,/odoo/external-src/product-attribute,/odoo/external-src/product-variant,/odoo/external-src/project,/odoo/external-src/project-reporting,/odoo/external-src/purchase-reporting,/odoo/external-src/purchase-workflow,/odoo/external-src/reporting-engine,/odoo/external-src/sale-financial,/odoo/external-src/sale-reporting,/odoo/external-src/sale-workflow,/odoo/external-src/server-auth,/odoo/external-src/server-tools,/odoo/external-src/social,/odoo/external-src/stock-logistics-barcode,/odoo/external-src/stock-logistics-reporting,/odoo/external-src/stock-logistics-warehouse,/odoo/external-src/stock-logistics-workflow,/odoo/external-src/web
