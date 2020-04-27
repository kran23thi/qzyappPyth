from datetime import datetime
import psycopg2
from flask import Flask, render_template, url_for,flash , redirect,json,jsonify,request,make_response
#from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm, QuizSubmitForm, QuestionForm, CategoryForm
import configitems as ci
from collections import defaultdict

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f06a98ac6c1ea22df69f4f4f031c1060'


'''app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db= SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer , primary_key=True)
    username = db.Column(db.String(20),unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file =  db.Column(db.String(20), nullable=False,default='default.jpg')
    password = db.Column(db.String(60),nullable=False)
    posts = db.relationship('Post',backref= 'author' , lazy= True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}','{self.password}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    date_posted = db.Column(db.DateTime,nullable=False, default = datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer,db.Foreignkey('User.id'), nullable=False)


def __repr__(self):
    return f"Post('{self.title}','{self.date_posted}')"


posts = [
    {
        'author': 'corey schafer',
        'title': 'blog post1',
        'content': 'first post content',
        'date_posted': 'April 20,2018'
    },

    {
        'author': 'jane doe',
        'title': 'blog post2',
        'content': 'second post content',
        'date_posted': 'April 21,2018'
    }
]
'''

     
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='home')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    username = form.username.data
    email = form.email.data
    password = form.password.data
    confirm_password =form.confirm_password.data
    if form.validate_on_submit():
        print(username)
        print(email)
        #d = {}
        '''
        d=[]
        d["username"] = username
        d["email"] = email
        d["password"] = password
        with open('data.json', 'a')as fp:
            jsonobj=json.dumps(d)
        '''
        
        conn = psycopg2.connect(database=ci.dbname, user=ci.dbuser, password=ci.dbpassword, host=ci.dbhost, port=ci.dbport)
        cur = conn.cursor()
        Userinsertqry="INSERT INTO register_user (username, email, password, confirm_password) VALUES (%s,%s,%s,%s)"
        UservaluestoInsert=(username,email,password,confirm_password)
        cur.execute(Userinsertqry, UservaluestoInsert)
        print("registered")
        conn.commit()
        print("registered again")
        count = cur.rowcount
        if count>0:
            flash('Account created for {form.username.data}!', 'success')

        return redirect(url_for('home'))
    return render_template('register.html', form=form)


'''@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
         with open('data.json','r')as fp:
            data = json.load(fp)
            print(data)
         for d in data:
            if form.email.data == d['email'] and form.password.data == d['password']:
                flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
    else:
            flash('Login Unsuccessful. please check username and password','danger')
    return render_template('login.html', title='Login', form=form)'''
    
@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
         with open('data.json','r')as fp:
            data = json.load(fp)
            print(data)
         for d in data:
            if form.email.data == d['email'] and form.password.data == d['password']:
                flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
    else:
            flash('Login Unsuccessful. please check username and password','danger')
    return render_template('login.html', title='Login', form=form)




@app.route("/submitform", methods=['GET', 'POST'])
def submitform():
    form = QuizSubmitForm()
    if request.method=='POST':
        question=form.question.data
        #print(form.question.data)
        AOption=form.AOption.data
        BOption=form.BOption.data
        COption=form.COption.data
        DOption=form.DOption.data
        answer=form.Answer.data
        category=form.category.data
        quizId=form.quizId.data
        
        #category=form.category.data
        conn = psycopg2.connect(database=ci.dbname, user=ci.dbuser, password=ci.dbpassword, host=ci.dbhost, port=ci.dbport)
        cur = conn.cursor()
        #cur1 = conn.cursor()
        cur2 = conn.cursor()
        '''qid="1"
        hint="test"
        #Question_insertqry = """ INSERT INTO question (question,choice4) VALUES (%s, %s)"""
        #Question_valuestoInsert=(question,DOption)
        Question_insertqry=""" INSERT INTO question (quest_id, question_description, choice1, choice2, choice3, choice4, correct_answer, category_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
        Question_valuestoInsert=(qid,question,AOption,BOption,COption,DOption,answer,category)
        print(question)
        print(form.errors) 
        Question_count_query="select COUNT(*) from questiondummy"
        cur1.execute(Question_count_query)
        Question_count=cur1.fetchall()
        print(Question_count)'''
        
        Max_qid = "select MAX(qnid) from questiondummy group by qnid"
        cur2.execute(Max_qid)
        print(cur2.rowcount)
        Max_qid_value=cur2.fetchall()
        if cur2.rowcount<=0:
            new_qid=1
        else:
            print(Max_qid_value)
            new_qid=Max_qid_value[0][0]+1
        print(new_qid)
        Question_insertqry= "INSERT INTO questiondummy ( question, choicea, choiceb, choicec, choiced, correctanswer, category, quizId, qid, qnid) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        Question_valuestoInsert=(question,AOption,BOption,COption,DOption,answer,category,quizId,0,new_qid)
        cur.execute(Question_insertqry, Question_valuestoInsert)
        print("Inserted")
        conn.commit()
        print("Inserted again")
        count = cur.rowcount
        if count>0:
            flash('Question added', 'success')
        return redirect(url_for('submitform'))

    return render_template('submitform.html', title='submitQuiz', form=form)

        
@app.route('/loadQuestion', methods=['GET','POST'])
def Question():
      form=QuestionForm()
      
      conn = psycopg2.connect(database=ci.dbname, user=ci.dbuser, password=ci.dbpassword, host=ci.dbhost, port=ci.dbport)
      print("connected")
      cur = conn.cursor()
      cur1 = conn.cursor()
      #cur2 = conn.cursor()
      
      print("connected again")
      cur.execute("select qnid, question, choicea, choiceb, choicec, choiced from questiondummy")
      print("fetch")
      #question=form.question.data
      question = cur.fetchall()#data from database
      form.question=question
      print("try to insert value")
      
      cur1.execute("select qnid,correctanswer from questiondummy")
      correct_answers=cur1.fetchall()
      print(correct_answers)
      new_answer=dict(correct_answers)
      print(new_answer)
      
      '''cur2.execute("select quizId from questiondummy")
      QuizId=cur2.fetchall()
      print(QuizId)'''
            
      '''form.question=[["Q1","Q1opt1","Q1opt2"],["Q2","Q2opt1","Q2opt2"]]
      print(form.question[0][0])
      print(form.question[1][0])
      #for qname in question:
      print(request.form.get(form.question[0][0]))
      res2 = request.form.get(form.question[1][0])
      print(res2)
      res=request.form
      print(res)
      #print=request.form.get()
      #print(questionSet[0][0])
      print("fetched")'''
      
      if request.method=='POST':
        username=form.username.data
        print(form.username.data)
        #quizId=form.quizId.data
        quizId=1
        score=0
        print(question)
        print(form)
        for item in form.question:
            print(item)
            print(item[0])
            user_answer=request.form.get(str(item[0]))
            print(user_answer)
            print(new_answer.get(item[0]))
            correctAnswer = new_answer.get(item[0])
            Question_insertqry= "INSERT INTO quiz_response ( username, quizId, question, user_answer) VALUES (%s,%s,%s,%s)"
            Question_valuestoInsert=(username, quizId, item[0], user_answer)
            cur.execute(Question_insertqry, Question_valuestoInsert)
            #print("Inserted")
            conn.commit()
            if correctAnswer == user_answer:
                print("initial score")
                score=score+1
            print("total score %s" % (score))
            
            count = cur.rowcount
            if count>0:
                flash('Quiz result submitted', 'success')    
            
            
            
        Score_insertqry= "INSERT INTO leaderboard (username, quizId, score) VALUES (%s,%s,%s)"
        Score_valuestoInsert=(username, quizId, score)
        cur.execute(Score_insertqry,Score_valuestoInsert)
        conn.commit()
            
        print("scores added")
        
        return redirect(url_for('LeaderBoard'))  
        
      return render_template('loadQuestion.html', questionDisplay=form)
  
@app.route("/category")
def Category():
    form=CategoryForm()
    '''temp = defaultdict(lambda: len(temp)) 
    new_quizid = [temp[item] for item in form] 
    quizId=new_quizid'''
      
    '''conn = psycopg2.connect(database=ci.dbname, user=ci.dbuser, password=ci.dbpassword, host=ci.dbhost, port=ci.dbport)
    cur = conn.cursor()
    select=request.form.get(list)
    print(str(select))
    if select == 'Technical':
        quizId=1
    elif select == 'About Daimler':
        quizId=2
    else:
        quizId=3
    Quizid_Insertqry= "INSERT INTO questiondummy (quizId) VALUES (%s)"
    Quizid_valuestoInsert=(quizId)
    cur.execute(Quizid_Insertqry,(Quizid_valuestoInsert,))
    conn.commit()'''
    
    
    return render_template('category.html', form=form)

@app.route("/leaderboard", methods=['GET','POST'])
def LeaderBoard():
    conn = psycopg2.connect(database=ci.dbname, user=ci.dbuser, password=ci.dbpassword, host=ci.dbhost, port=ci.dbport)
    cur = conn.cursor()
    cur.execute("select username,score from leaderboard")
    result=cur.fetchall()
    print(result)
    return render_template('leaderboard.html', result=result)





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
