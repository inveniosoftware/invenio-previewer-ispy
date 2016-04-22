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
    "vendors/ispy-webgl/js/lib/three.min.js",
    "vendors/ispy-webgl/js/lib/helvetiker_regular.typeface.js",
    "vendors/ispy-webgl/js/lib/jquery.scrollintoview.min.js",
    "vendors/ispy-webgl/js/lib/stats.min.js",
    "vendors/ispy-webgl/js/lib/stupidtable.min.js",
    "vendors/ispy-webgl/js/lib/tween.min.js",
    "vendors/ispy-webgl/js/lib/CanvasRenderer.js",
    "vendors/ispy-webgl/js/lib/CombinedCamera.js",
    "vendors/ispy-webgl/js/lib/DeviceOrientationControls.js",
    "vendors/ispy-webgl/js/lib/MTLLoader.js",
    "vendors/ispy-webgl/js/lib/OBJExporter.js",
    "vendors/ispy-webgl/js/lib/OBJLoader.js",
    "vendors/ispy-webgl/js/lib/OBJMTLLoader.js",
    "vendors/ispy-webgl/js/lib/Projector.js",
    "vendors/ispy-webgl/js/lib/SVGRenderer.js",
    "vendors/ispy-webgl/js/lib/TrackballControls.js",

    "vendors/ispy-webgl/js/StereoEffect.js",

    "vendors/ispy-webgl/js/config.js",
    "vendors/ispy-webgl/js/setup.js",
    "vendors/ispy-webgl/js/animate.js",
    "vendors/ispy-webgl/js/files-load.js",
    "vendors/ispy-webgl/js/objects-draw.js",
    "vendors/ispy-webgl/js/objects-add.js",
    "vendors/ispy-webgl/js/objects-config.js",

    "vendors/ispy-webgl/js/controls.js",
    "vendors/ispy-webgl/js/tree-view.js",
    "vendors/ispy-webgl/js/display.js",
    "vendors/ispy-webgl/js/ispy.js",

    "vendors/ispy-webgl/geometry/models.min.js",
    "vendors/ispy-webgl/geometry/dt.min.js",
    "vendors/ispy-webgl/geometry/csc.min.js",
    "vendors/ispy-webgl/geometry/rpc.min.js",
    "vendors/ispy-webgl/geometry/ho.min.js",
    "vendors/ispy-webgl/geometry/hehf.min.js",
    "vendors/ispy-webgl/geometry/hb.min.js",
    "vendors/ispy-webgl/geometry/eb-reduced.min.js",
    "vendors/ispy-webgl/geometry/ee-reduced.min.js",
    "vendors/ispy-webgl/geometry/tob.min.js",
    "vendors/ispy-webgl/geometry/tec.min.js",
    "vendors/ispy-webgl/geometry/tib.min.js",
    "vendors/ispy-webgl/geometry/tid.min.js",
    "vendors/ispy-webgl/geometry/pixel.min.js",

    output="previewer_ispy.js",
    filters="requirejs",
    weight=51,
    bower={
    "ispy-webgl": "0.9.4-invenio.22"
    }
)

styles = Bundle(
    "vendors/ispy-webgl/css/ispy.css",
    output="previewer_ispy.css",
    filters="cleancss",
    weight=51
)
