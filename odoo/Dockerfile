FROM camptocamp/odoo-project:10.0-3.1.1-batteries

RUN echo "deb [check-valid-until=no] http://archive.debian.org/debian jessie-backports main" > /etc/apt/sources.list.d/jessie-backports.list \
    && sed -i '/deb http:\/\/deb.debian.org\/debian jessie-updates main/d' /etc/apt/sources.list \
    && echo 'Acquire::Check-Valid-Until "false";' > /etc/apt/apt.conf;
RUN apt-get update \
    && apt-get install -y --no-install-recommends vim wget git

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

COPY ./templates/odoo.cfg.tmpl /templates/odoo.cfg.tmpl

ENV ADDONS_PATH /odoo/src/addons,/odoo/src/odoo/addons,/odoo/links,/odoo/external-src/odoo-shopinvader,/odoo/external-src/connector-search-engine,/odoo/external-src/bank-payment,/odoo/external-src/product-brand,/odoo/external-src/rest-framework,/odoo/external-src/sale-workflow,/odoo/external-src/queue,/odoo/external-src/product-variant,/odoo/external-src/server-tools,/odoo/external-src/delivery-carrier,/odoo/external-src/payment-gateway,/odoo/external-src/storage,/odoo/external-src/connector,/odoo/external-src/e-commerce,/odoo/external-src/ak-odoo-incubator,/odoo/external-src/crm,/odoo/external-src/account-reconcile
