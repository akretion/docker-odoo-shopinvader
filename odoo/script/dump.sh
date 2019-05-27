#!/bin/bash

pg_dump db > /backup/db.sql
cp -r /data/odoo/filestore /backup
