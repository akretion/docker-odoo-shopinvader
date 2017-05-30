# Voodoo (buildout) project for shopinvader

Clone it and launch

```voodoo run```

Or if you don't use voodoo:

```
./bootstrap
./buildout
cp local-template.cfg local.cfg
vi local.cfg  # and edit your stuff
bin/start_openerp
```

Known problems:
===============

After you run buildout, the `bin/start_openerp` file will contain a reference to the local Python modules folder. Remove that line, otherwise an `urllib3` version conflict can occur.

