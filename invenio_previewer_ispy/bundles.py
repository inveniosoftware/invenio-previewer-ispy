# -*- coding: utf-8 -*-
#
# This file is part of Invenio-Previewer-ISPY
# Copyright (C) 2014 CERN
#
# Invenio-Previewer-ISPY is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio-Previewer-ISPY is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio-Previewer-ISPY; if not, write to the Free Software Foundation,
# Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""Invenio-Previewer-ISPY bundles."""

from invenio.ext.assets import Bundle


js = Bundle(
    "js/previewer/ispy/init.js",
    "vendors/ispy-online/js/jszip.min.js",
    "vendors/ispy-online/js/elab.js",
    "vendors/ispy-online/js/utils.js",
    "vendors/ispy-online/js/flexcroll.js",
    "vendors/jquery/dist/jquery.min.js",
    "vendors/ispy-online/js/pre3d.js",
    "vendors/ispy-online/js/pre3d_shape_utils.js",
    "vendors/ispy-online/js/demo_utils.js",
    "vendors/ispy-online/js/object-conversion.js",
    "vendors/ispy-online/js/detector-model-gen.js",
    "vendors/ispy-online/js/detector-model-geometry.js",
    "vendors/ispy-online/js/data-description.js",
    "vendors/ispy-online/js/eventdisplay.js",
    "vendors/ispy-online/js/about.js",
    "vendors/ispy-online/js/event-browser.js",
    "vendors/ispy-online/js/range-selection.js",
    "vendors/ispy-online/js/settings.js",
    "vendors/ispy-online/js/speed-test.js",
    output="previewer_ispy.js",
    filters="requirejs",
    weight=51,
    bower={
      "ispy-online": "latest"
    }
)

styles = Bundle(
    "css/previewer/ispy.css",
    "vendors/ispy-online/css/scrollbar.css",
    "vendors/ispy-online/css/eventdisplay.css",
    "vendors/ispy-online/css/settings.css",
    "vendors/ispy-online/css/range-selection.css",
    "vendors/ispy-online/css/event-browser.css",
    "vendors/ispy-online/css/speed-test.css",
    "vendors/font-awesome/css/font-awesome.min.css",
  output="previewer_ispy.css",
    filters="cleancss",
    weight=51
)
