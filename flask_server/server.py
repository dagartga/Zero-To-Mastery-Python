from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)




def write_to_file(data):
    '''
        Takes in json data and writes the values to a txt file

        input json example:
        {'email': 'blank@nomail.com', 'subject': 'testing', 'message': 'the message is'}

        txt output:
        'blank@nomail.com','testing','this message is'

    '''
    with open('./database.txt', 'a') as db:
        email = data['email']
        subject = data['subject']
        message = data['message']
        # append the data to the database.txt file
        file = db.write(f'\n{email},{subject},{message}')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return redirect('thankyou.html')

    else:
        return 'something went wrong. Try again!'
