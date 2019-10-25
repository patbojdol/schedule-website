#!/usr/bin/env python3.7
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
        "main.html.j2", start=start.strftime("%Y-%m-%d"), end=end.strftime("%Y-%m-%d")
    )


@app.route("/schedule")
def schedule():
    schedule_id = request.args.get("schedule-id")

    start = datetime.strptime(request.args.get("start-date"), "%Y-%m-%d")
    end = datetime.strptime(request.args.get("end-date"), "%Y-%m-%d")

    schedule = Schedule(
        schedule_id, start.strftime("%Y-%m-%d"), end.strftime("%Y-%m-%d")
    )

    now = datetime.now()
    today = date(now.year, now.month, now.day)

    return render_template(
        "schedule.html.j2", schedule=schedule.nested_events, today=today
    )


@app.route("/schedule.ics")
def schedule_ics():
    schedule_id = request.args.get("schedule-id")

    if "start-date" in request.args and "end-date" in request.args:
        start = datetime.strptime(request.args.get("start-date"), "%Y-%m-%d")
        end = datetime.strptime(request.args.get("end-date"), "%Y-%m-%d")

        schedule = Schedule(
            schedule_id, start.strftime("%Y-%m-%d"), end.strftime("%Y-%m-%d")
        )
    else:
        schedule = Schedule(schedule_id)

    return Response(schedule.to_ical(), mimetype="text/calendar")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
