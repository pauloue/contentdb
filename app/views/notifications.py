# Content DB
# Copyright (C) 2018  rubenwardy
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from flask import *
from flask_user import current_user, login_required
from app import app
from app.models import *

@app.route("/notifications/")
@login_required
def notifications_page():
	return render_template("notifications/list.html")

@app.route("/notifications/clear/", methods=["POST"])
@login_required
def clear_notifications_page():
	current_user.notifications.clear()
	db.session.commit()
	return redirect(url_for("notifications_page"))
