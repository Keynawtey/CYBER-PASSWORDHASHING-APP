from flask import *
import pymysql
app = Flask(__name__)

# Routes Here
@app.route('/')
def home():
     return render_template('home.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
        #Check if form was posted by user
        #create a function
    if request.method == 'POST':
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            title = request.form['title']

            # Connect to the database

            connection=pymysql.connect (host='localhost', user='root', password='', database='cyberDB')

            cursor = connection.cursor()

            sql = '''
                insert into users (username, email, password, title)values(%s, %s, %s, %s)
                '''
            
            cursor.execute(sql, (username, email, password, title))

            connection.commit()

        

            return render_template('signup.html', msg='Application Made Successfully')
    else:
        # Form not posted, display the form to allow user Post something
        return render_template('signup.html')

app.run(debug=True)