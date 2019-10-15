#!/usr/bin/env python3.7
from flask import Flask, render_template, request
from UESchedule import ScheduleDownloader
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/schedule')
def schedule():
    schedule_id = request.args.get('schedule-id')
    downloader = ScheduleDownloader(schedule_id)

    now = datetime.now()
    start = now - timedelta(days=now.weekday())
    end = start + timedelta(days=13)

    schedule = downloader.download(start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d'))
    schedule.run_filters()
    return render_template('schedule.html', schedule = schedule.get_schedule(nested=True))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
