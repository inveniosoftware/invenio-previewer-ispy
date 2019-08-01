# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2019 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

from flask import render_template, request

def can_preview(f):
    """Return ``True`` if filetype can be previewed."""
    return f.superformat == '.ig'


def preview(f):
    """Return appropiate template and passes the file and an embed flag."""
    return render_template("previewer/ispy.html", f=f,
                           embed=request.args.get('embed', type=bool))
