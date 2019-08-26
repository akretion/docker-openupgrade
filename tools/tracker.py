# -*- coding: utf-8 -*-
# Copyright 2019 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

# Copy me in the directory /openerp/modules/migration
# or /odoo/modules/migration
# and add from . import tracker in __init__.py

try:
    from openerp.modules.migration import MigrationManager
except:
    from odoo.modules.migration import MigrationManager

from datetime import datetime
import logging
_logger = logging.getLogger(__name__)

ori_migrate_module = MigrationManager.migrate_module

MIGRATION_TIME = {}
MIGRATION_TIME_OUTPUT = '/odoo/migration_time_ouput.txt'

def migrate_module(self, pkg, stage):
    global MIGRATION_TIME
    if (hasattr(pkg, 'update') or pkg.state == 'to upgrade'):
        if stage == 'pre':
            MIGRATION_TIME[pkg.name] = {'start': datetime.now()}
        if stage == 'post':
            res = MIGRATION_TIME[pkg.name]
            res['stop'] = datetime.now()
            res['duration'] = (res['stop'] - res['start']).seconds / 60
            _logger.info(
                'Migrate Module %s, duration %s min', pkg.name, res['duration'])
            with open(MIGRATION_TIME_OUTPUT, 'a') as out:
                out.write(u"%s %s %s %s\n" % (
                    pkg.name,
                    res['start'],
                    res['stop'],
                    res['duration']
                    ))
    return ori_migrate_module(self, pkg, stage)

MigrationManager.migrate_module = migrate_module
