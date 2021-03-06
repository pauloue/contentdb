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
from flask_user import *
from flask.ext import menu
from app import app
from app.models import *

@app.route("/todo/")
@login_required
def todo_page():
	canApproveNew = Permission.APPROVE_NEW.check(current_user)
	canApproveRel = Permission.APPROVE_RELEASE.check(current_user)
	canApproveScn = Permission.APPROVE_SCREENSHOT.check(current_user)

	packages = None
	if canApproveNew:
		packages = Package.query.filter_by(approved=False, soft_deleted=False).all()

	releases = None
	if canApproveRel:
		releases = PackageRelease.query.filter_by(approved=False).all()

	screenshots = None
	if canApproveScn:
		screenshots = PackageScreenshot.query.filter_by(approved=False).all()


	topics_to_add = ForumTopic.query \
			.filter(~ db.exists().where(Package.forums==ForumTopic.topic_id)) \
			.count()

	return render_template("todo/list.html", title="Reports and Work Queue",
		packages=packages, releases=releases, screenshots=screenshots,
		canApproveNew=canApproveNew, canApproveRel=canApproveRel, canApproveScn=canApproveScn,
		topics_to_add=topics_to_add)


@app.route("/todo/topics/")
@login_required
def todo_topics_page():
	total = ForumTopic.query.count()

	topics = ForumTopic.query \
			.filter(~ db.exists().where(Package.forums==ForumTopic.topic_id)) \
			.order_by(db.asc(ForumTopic.wip), db.asc(ForumTopic.name), db.asc(ForumTopic.title)) \
			.all()

	return render_template("todo/topics.html", topics=topics, total=total)
