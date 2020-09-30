# -*- coding: utf-8 -*-

import logging

from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)

class FacebookCatalogController(http.Controller):

    @http.route('/facebook_catalog_feed', auth='public', method=["GET"], sitemap=False)
    def feed(self):
        pass
