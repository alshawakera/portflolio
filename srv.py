from random import randint
import re

from flask import Flask, render_template, redirect, request
import csv

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'somthing went wrong'


@app.route('/guessing-game', methods=['POST', 'GET'])
def guessing_game():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            username = data["email"]
            password = data["password"]
            if checker(username, password):
                return redirect('/game.html')

            return redirect('/Guessing_game.html')
        except:
            return 'did not save to database   '
    else:
        return 'somthing went wrong'


@app.route('/game', methods=['POST'])
def game():
    data = request.form.to_dict()
    guess = int(data['guess'])
    return guess_game(guess)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f"\n{email},{subject},{message}")


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


def checker(email, password):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    pass_regex = r"^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"
    return re.fullmatch(email_regex, email) and re.fullmatch(pass_regex, password)


def guess_game(guess):
    answer = randint(1, 15)

    if 0 < guess < 16:
        if guess == answer:
            return 'صح عليك'
        return 'غلط خمن صح مره ثانية'

    return 'قلت لك خمن 1 الى 10 مدخل حروف ليه؟؟؟؟'


if __name__ == '__main__':
    app.debug = True
    app.run()

# @app.route('/index.html')
# def hello():
#     return render_template('index.html')
#
# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
# @app.route('/about')
# def about2():
#     return render_template('about.html')
#
# @app.route('/components.html')
# def components():
#     return render_template('components.html')
#
#
# @app.route('/components')
# def components2():
#     return render_template('components.html')
#
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
#
#
# @app.route('/contact')
# def contact2():
#     return render_template('contact.html')
#
#
# @app.route('/thankyou.html')
# def thankyou():
#     return render_template('thankyou.html')
#
#
# @app.route('/work.html')
# def work():
#     return render_template('work.html')
#
#
# @app.route('/work')
# def work2():
#     return render_template('work.html')
#
#
# @app.route('/works.html')
# def works():
#     return render_template('works.html')
#
#
# @app.route('/works')
# def works2():
#     return render_template('works.html')
