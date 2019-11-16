#!/usr/bin/env python3
from flask import Flask, render_template, request, Response
from ue_schedule import Schedule
from datetime import datetime, timedelta, date

app = Flask(__name__)


@app.route("/")
def main():
    now = datetime.now()
    start = now - timedelta(days=now.weekday())
    end = start + timedelta(days=13)

    return render_template(
        "main.jinja2", start=start.strftime("%Y-%m-%d"), end=end.strftime("%Y-%m-%d")
    )


@app.route("/schedule")
def schedule():
    schedule_id = request.args.get("schedule-id")
    schedule = Schedule(schedule_id)

    if "start-date" in request.args and "end-date" in request.args:
        start = datetime.strptime(request.args.get("start-date"), "%Y-%m-%d").date()
        end = datetime.strptime(request.args.get("end-date"), "%Y-%m-%d").date()
        events = schedule.get_events(start, end)
    else:
        events = schedule.get_events()

    return render_template(
        "schedule.jinja2",
        schedule=events,
        schedule_id=schedule_id,
        today=datetime.now().date(),
    )


@app.route("/schedule.ics")
def schedule_ics():
    schedule_id = request.args.get("schedule-id")
    schedule = Schedule(schedule_id)

    events = schedule.get_ical()

    return Response(events, mimetype="text/calendar")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
