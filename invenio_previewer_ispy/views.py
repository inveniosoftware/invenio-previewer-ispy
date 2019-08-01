# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2019 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Define Invenio-Previewer-ISPY Blueprint."""

from flask import Blueprint

blueprint = Blueprint('invenio_previewer_ispy', __name__,
                      template_folder='templates',
                      static_folder='static')
