# SPDX-FileCopyrightText: 2014 CERN
# SPDX-License-Identifier: MIT

from flask import render_template, request

def can_preview(f):
    """Return ``True`` if filetype can be previewed."""
    return f.superformat == '.ig'


def preview(f):
    """Return appropiate template and passes the file and an embed flag."""
    return render_template("previewer/ispy.html", f=f,
                           embed=request.args.get('embed', type=bool))
