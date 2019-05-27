#!/bin/bash

pg_dump db > /odoo/backup/db.sql
cp -r /data/odoo/filestore /odoo/backup
