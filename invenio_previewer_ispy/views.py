# SPDX-FileCopyrightText: 2014 CERN
# SPDX-License-Identifier: MIT

"""Define Invenio-Previewer-ISPY Blueprint."""

from flask import Blueprint

blueprint = Blueprint('invenio_previewer_ispy', __name__,
                      template_folder='templates',
                      static_folder='static')
