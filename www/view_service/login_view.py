from datetime import timedelta

from flask import Blueprint, session, render_template, request, redirect, url_for

from www.helper.session_help import Session
from www.helper.user_dict import check_user

login_req = Blueprint('login_req',__name__)



@login_req.route('/login/')
def login():
    return render_template('login.html')


@login_req.route("/login_check/",methods=['post','get'])
def login_check():
    if request.method == 'POST':
        user = request.form.get('userid')
        password = request.form.get('passwd')
        print(user)
        print(password)
        if check_user(user,password):
            session.permanent = True
            login_req.permanent_session_lifttime = timedelta(minutes=1)
            Session.set_user(user)
            # return redirect(url_for('widget.widget_func'))
            return redirect('/')

    return render_template('login.html')

@login_req.route("/login_out/")
def login_out():
    session.clear()

    return render_template('login.html')
