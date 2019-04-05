FROM camptocamp/odoo-project:12.0-3.1.2-batteries

RUN apt-get update \
    && apt-get install -y --no-install-recommends vim wget git

COPY . /odoo
COPY templates /templates
RUN pip3 install -r /odoo/requirements.txt
RUN pip3 install -e /odoo
RUN pip3 install -e /odoo/src

ENV ADDONS_PATH=/odoo/src/addons,/odoo/src/odoo/addons,/odoo/links,/odoo/local-src