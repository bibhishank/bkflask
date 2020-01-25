from flask import Flask, render_template, request, redirect
import sys
import inspect
import csv

app = Flask(__name__)

def whoami():
    pass

#frame = inspect.currentframe()
    #return inspect.getframeinfo(frame).function

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/')
def hello_world_template():
    ##print(sys.modules(__name__))
    frame = inspect.currentframe()
    print('Function', inspect.getframeinfo(frame).function)
    return render_template('indexmain.html')

'''
#Generic lister
@app.route('/<stinr:page_name>')
def my_home_index_html():
    return render_template(page_name)
'''

@app.route('/index.html')
def my_home_index_html():
    frame = inspect.currentframe()
    print('Function', inspect.getframeinfo(frame).function)
    return render_template('index.html')

@app.route('/works.html')
def works_html():
    frame = inspect.currentframe()
    print('Function', inspect.getframeinfo(frame).function)
    return render_template('works.html')

@app.route('/contact.html')
def contact_html():
    frame = inspect.currentframe()
    print('Function', inspect.getframeinfo(frame).function)
    return render_template('contact.html')

@app.route('/about.html')
def about_html():
    frame = inspect.currentframe()
    print('Function', inspect.getframeinfo(frame).function)
    return render_template('about.html')

@app.route('/components.html')
def components_html():
    frame = inspect.currentframe()
    print('Function', inspect.getframeinfo(frame).function)
    return render_template('components.html')


@app.route('/indexmain.html')
def html_template():
    frame = inspect.currentframe()
    print('Function', inspect.getframeinfo(frame).function)
    return render_template('indexmain.html')

@app.route('/index1.html')
def hindex1_template():
    frame = inspect.currentframe()
    print('Function', inspect.getframeinfo(frame).function)
    return render_template('index1.html')

@app.route('/<username>')
def accept_user_name(username=None):
    frame = inspect.currentframe()
    print('Function', inspect.getframeinfo(frame).function)
    return render_template('indexmain.html', user_name=username)

#Accept multiple inputs
@app.route('/<username>/<int:emp_number>')
def accept_multi_param(username=None, emp_number=None):
    frame = inspect.currentframe()
    print('Function', inspect.getframeinfo(frame).function)
    return render_template('indexmain.html', user_name=username, employee_number=emp_number)


# belwo route will not execute as we have already defined app.route('/') above
@app.route('/')
def hello_world():
    frame = inspect.currentframe()
    print('Function', inspect.getframeinfo(frame).function)
    return 'Hello, Bibhishan!!!!!'


@app.route('/blog')
def blog():
    frame = inspect.currentframe()
    print('Function', inspect.getframeinfo(frame).function)
    return 'This is my first blog'

@app.route('/blog')
def blog2():
    frame = inspect.currentframe()
    print('Function', inspect.getframeinfo(frame).function)
    return 'This is my second blog but it will not reach here'


#http://127.0.0.1:5000/blog/2020/blog

@app.route('/blog/2020/blog')
def blog3():
    print(whoami())
    frame = inspect.currentframe()
    print('Function', inspect.getframeinfo(frame).function)
    return 'With additonal path'

@app.route('/login')
def login():
    print(whoami())
    frame = inspect.currentframe()
    print('Function', inspect.getframeinfo(frame).function)
    return render_template('login.html')

@app.route('/form_submit', methods=["POST"])
def form_submit():
    if request.method == 'POST':
        #Get all the data from submited request
        #data = request.form.to_dict()
        #return data
        # Get indivisual attribute data from submited request
        userid = request.form['uname']
        password = request.form['psw']
        if userid == 'Bibhishan':
            return 'user =' + userid + ' Pass =' + password
        else:
            return redirect('/login')
    else:
        render_template('login.html')

@app.route('/submit_contact_form', methods=["POST", "GET"])
def submit_contact_form():
    if request.method == 'POST':
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        #or collect these attributes in dictionary
        data = request.form.to_dict()
        saveData(data)
        saveDataToCSV(data)
        return render_template("thankyou.html", email=email)

def saveData(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

def saveDataToCSV(data):
    with open('database.csv', mode='a') as database_csv:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database_csv, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
