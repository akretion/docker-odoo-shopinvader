# Odoo Project with Ak recipe for ShopInvader project 

This repo has two objectives:
-  it's a boostrap project for odoo + shopinvader (+ elastic + postgres + mongo)
-  build the docker image used by https://github.com/akretion/shopinvader-getting-started

If you want to evaluate shopinvader, follow https://github.com/akretion/shopinvader-getting-started.
If you want to develop in odoo or in locomotive, follow this documentation.

## Bootstrap a shopinvader project

#### Requirements

* docky https://github.com/akretion/docky
* ak https://github.com/akretion/ak


### Get the boostrap files

Download this repo, you may not wan to `git clone`.

```
curl -sL https://github.com/akretion/docker-odoo-shopinvader/archive/10.0.tar.gz | tar xz
cd docker-odoo-shopinvader-10.0
```

### Fetch odoo modules

In addition to base Odoo modules, Shopinvader needs odoo community modules. 
Most of the base modules are from github.com/OCA
E-commerce specific modules are from github.com/shopinvader


Ak fetch the necessary modules and add them to path.

```
docker-odoo-shopinvader-10.0 $ cd odoo
docker-odoo-shopinvader-10.0/odoo $ ak build
docker-odoo-shopinvader-10.0 $ cd ..
```
You can manage branches in /odoo/spec.yaml before running ak.

### Install the default locomotive template

```
docker-odoo-shopinvader-10.0 $ curl -sL https://github.com/shopinvader/shopinvader-template/archive/master.tar.gz | tar xz
docker-odoo-shopinvader-10.0 $ docky run wagon bundle exec wagon deploy test -d -v -f
```

### Run the containers

```
docker-odoo-shopinvader-10.0 $ docky up
```

Now you odoo is ready with everything is installed

### Access

Odoo: http://shopinvader10.dy
Shopinvader: http://locomotive.dy
Locomotive admin panel: http://locomotive.dy/locomotive


### Configure the project

