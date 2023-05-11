FROM ghcr.io/akretion/odoo-docker:16.0-latest

RUN DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y libcairo2-dev libpq-dev && \
    apt-get clean

COPY odoo-spec.yaml /odoo/odoo-spec.yaml
ENV BUILD_RESTRICT_LANG=fr.po
RUN --mount=type=cache,target=/root/.cache /install/build-odoo
RUN --mount=type=cache,target=/root/.cache pip install -e /odoo/src

# generate oca requirement with
# find odoo/external-src/ -name 'requirements.txt' -exec cat {} \; > odoo/oca_requirements.txt
# then remove duplicate

COPY ./spec.yaml /odoo/spec.yaml
RUN --mount=type=cache,target=/root/.cache /install/build-odoo-external

COPY ./oca_requirements.txt /odoo/oca_requirements.txt
RUN --mount=type=cache,target=/root/.cache pip install -r /odoo/oca_requirements.txt

COPY ./requirements.txt /odoo/requirements.txt
RUN --mount=type=cache,target=/root/.cache pip install -r /odoo/requirements.txt

COPY ./local-src /odoo/local-src

ENV SERVER_WIDE_MODULES=base,web,openupgrade_framework

ENV ADDONS_PATH=/odoo/external-src/openupgrade,/odoo/links,/odoo/local-src,/odoo/src/odoo/addons,/odoo/src/addons,/odoo/external-src/account-financial-reporting,/odoo/external-src/account-financial-tools,/odoo/external-src/account-fiscal-rule,/odoo/external-src/account-invoice-reporting,/odoo/external-src/account-invoicing,/odoo/external-src/account-payment,/odoo/external-src/account-reconcile,/odoo/external-src/bank-payment,/odoo/external-src/bank-statement-import,/odoo/external-src/community-data-files,/odoo/external-src/connector,/odoo/external-src/connector-ecommerce,/odoo/external-src/connector-telephony,/odoo/external-src/contract,/odoo/external-src/crm,/odoo/external-src/delivery-carrier,/odoo/external-src/e-commerce,/odoo/external-src/edi,/odoo/external-src/hr,/odoo/external-src/timesheet,/odoo/external-src/intrastat,/odoo/external-src/l10n-france,/odoo/external-src/l10n-brazil,/odoo/external-src/manufacture,/odoo/external-src/partner-contact,/odoo/external-src/pos,/odoo/external-src/product-attribute,/odoo/external-src/product-variant,/odoo/external-src/project,/odoo/external-src/project-reporting,/odoo/external-src/purchase-reporting,/odoo/external-src/purchase-workflow,/odoo/external-src/reporting-engine,/odoo/external-src/sale-financial,/odoo/external-src/sale-reporting,/odoo/external-src/sale-workflow,/odoo/external-src/server-auth,/odoo/external-src/server-tools,/odoo/external-src/social,/odoo/external-src/stock-logistics-barcode,/odoo/external-src/stock-logistics-reporting,/odoo/external-src/stock-logistics-warehouse,/odoo/external-src/stock-logistics-workflow,/odoo/external-src/web,/odoo/external-src/account-closing,/odoo/external-src/server-env,/odoo/external-src/server-backend,/odoo/external-src/multi-company,/odoo/external-src/queue,/odoo/external-src/account-analytic,/odoo/external-src/currency,/odoo/external-src/server-ux,/odoo/external-src/rest-framework,/odoo/external-src/server-brand
