#!/usr/bin/env python3.7
from flask import Flask, render_template, request
from ue_schedule import Schedule
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/schedule')
def schedule():
    schedule_id = request.args.get('schedule-id')
    
    start = datetime.strptime(request.args.get('start-date'), '%Y-%m-%d')
    end = datetime.strptime(request.args.get('end-date'), '%Y-%m-%d')

    schedule = Schedule(schedule_id, start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d'))
    return render_template('schedule.html', schedule = schedule.nested_events)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
