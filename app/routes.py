from app import app
from app.forms import LoginForm, SubmitForm
from flask import render_template, jsonify, request, redirect, flash, url_for
from twilio.twiml.messaging_response import MessagingResponse
from config import MY_ACCOUNT, MY_TOKEN, MY_PHONE, API_ID
from message import Send
from weather import Weather
import requests



@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():

    form = SubmitForm()
    if form.validate_on_submit():
        try:
            flash('Submitted for number {} of {}'.format(form.usernum.data, form.usercity.data))
            place = form.usercity.data
            user_num = '+1' + form.usernum.data
            weather = Weather(place, API_ID)
            send_message = Send(MY_ACCOUNT, MY_TOKEN, user_num)
            send_message.send_message(weather.city, weather.current, weather.high, weather.low, weather.condition)

            return redirect(url_for('index'))
        except:
            flash('ERROR: City Name Not Spelled Correctly! e.g. los angeles, not losangeles')
            return redirect(url_for('index'))
    else:
        return render_template('index.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)



@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)
    print(body)
    new_body = body.split(':')
    print(new_body)
    # Start TwiML response
    resp = MessagingResponse()

    # check for valid sms input from user

    if len(new_body) == 2 and new_body[0].lower().strip() == 'weather' and ':' in body:
        try:
            location = new_body[1].lstrip()
            weather = Weather(location, API_ID)
            resp.message("{}: Current Temp: {}F, High: {}F, Low: {}F, Condition: {}".format(weather.city.title(), str(weather.current)+u'\N{DEGREE SIGN}', str(weather.high)+u'\N{DEGREE SIGN}', str(weather.low)+u'\N{DEGREE SIGN}', weather.condition.title()))
        except:
            resp.message("Please follow this format for your message=> weather: CITYNAME e.g. weather: new york")
    else:
        resp.message("Please follow this format for your message=> weather: CITYNAME e.g. weather: new york")


    return str(resp)


# @app.route('/api', methods=['GET'])
# @app.route('/api/<name>/<age>/<language>', methods=['GET', 'POST'])
# def api(name = '', age = '', language = ''):
#     people = [
#         {
#             "name": "Max",
#             "age": 26,
#             "language": "Python"
#         },
#         {
#             "name": "John",
#             "age": 43,
#             "language": "Java"
#         },
#         {
#             "name": "Kelly",
#             "age": 16,
#             "language": "C++"
#         },
#         {
#             "name": "Stuart",
#             "age": 55,
#             "language": "Fortran"
#         }
#     ]
#
#     if name != '' and age != '' and language != '':
#         people.append({
#             "name": name,
#             "age": int(age),
#             "language": language
#         })
#
#     return jsonify(people)
