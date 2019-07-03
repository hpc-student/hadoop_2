#################
#### imports ####
#################
from bokeh.embed import components
import random
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_login import login_user, current_user, login_required, logout_user

from . import hadoop_blueprint
from .forms import HadoopForm
from .job import HJob
from .bokeh_bar import chart
from .pandas import data
#from project.models import User
from project import db


################
#### routes ####
################

@hadoop_blueprint.route('/hadoop', methods=['GET','POST'])
def hadoop():
    form=HadoopForm()
    job=HJob(form.javaClass.data,form.dataInput.data,form.dataOutput.data)
    if request.method == 'POST' and form.validate_on_submit():
        flash('wait')
        #j=job.clean()
        
        jj=[job.clean(),"wait",job.exec2(), "fin" ]
        d=data()
        plot=d.read()
        script, div = components(plot)
        return render_template('hadoop/hadoopHome.html', form=form,result=jj,the_div=div,the_script=script)
        #return redirect(url_for('hadoop.result'))
    return render_template('hadoop/hadoopHome.html',form=form)




@hadoop_blueprint.route('/hadoop/<int:bars_count>/')
def chartt(bars_count):
    if bars_count <= 0:
        bars_count = 1
    d=data()
    plot = d.read()
    script, div = components(plot)

    return render_template("hadoop/chart.html", bars_count=bars_count,
                           the_div=div, the_script=script)
'''
#@app.route("/<int:bars_count>/")
@hadoop_blueprint.route('/hadoop/<int:bars_count>/')
def chartt(bars_count):
    if bars_count <= 0:
        bars_count = 1

    data = {"days": [], "bugs": [], "costs": []}
    for i in range(1, bars_count + 1):
        data['days'].append(i)
        data['bugs'].append(random.randint(1,100))
        data['costs'].append(random.uniform(1.00, 1000.00))
    c=chart()
    hover = c.create_hover_tool()
    plot = c.create_bar_chart(data, "Bugs found per day", "days",
                            "bugs", hover)
    script, div = components(plot)

    return render_template("hadoop/chart.html", bars_count=bars_count,
                           the_div=div, the_script=script)



'''
'''

@hadoop_blueprint.route('/hadoop', methods=['GET','POST'])
def hadoop():
    form=HadoopForm()
    job=HJob(form.javaClass.data,form.dataInput.data,form.dataOutput.data)
    if request.method == 'POST' and form.validate_on_submit():
        flash('wait')
        resultt=job.exec()
        resultt=resultt.split( maxsplit=10)
        result=[]
        for i in range(0,len(resultt)-1,2):
            x={'key':resultt[i],'vlaue':resultt[i+1]}
            result.append(x)
        data = {"days": [], "bugs": [], "costs": []}
        for i in range(0,len(resultt)-1,2):
            data['days'].append(resultt[i])
            data['bugs'].append(int(resultt[i+1]))
            data['costs'].append(random.uniform(1.00, 1000.00))
        c=chart()
        hover = c.create_hover_tool()
        plot = c.create_bar_chart(data, "Bugs found per day", "days",
                            "bugs", hover)
        script, div = components(plot)
        return render_template('hadoop/hadoopHome.html', form=form,result=result,the_div=div,the_script=script)
        #return redirect(url_for('hadoop.result'))
    return render_template('hadoop/hadoopHome.html',form=form)
'''

'''
@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    # If the User is already logged in, don't allow them to try to register
    if current_user.is_authenticated:
        flash('Already registered!  Redirecting to your User Profile page...')
        return redirect(url_for('users.profile'))

    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        new_user = User(form.email.data, form.password.data)
        new_user.authenticated = True
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        flash('Thanks for registering, {}!'.format(new_user.email))
        return redirect(url_for('users.profile'))
    return render_template('users/register.html', form=form)


@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    # If the User is already logged in, don't allow them to try to log in again
    if current_user.is_authenticated:
        flash('Already logged in!  Redirecting to your User Profile page...')
        return redirect(url_for('users.profile'))

    form = LoginForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and user.is_correct_password(form.password.data):
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=form.remember_me.data)
                flash('Thanks for logging in, {}!'.format(current_user.email))
                return redirect(url_for('users.profile'))

        flash('ERROR! Incorrect login credentials.')
    return render_template('hadoop/hadoopHome.html', form=form)


@users_blueprint.route('/logout')
@login_required
def logout():
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    flash('Goodbye!')
    return redirect(url_for('recipes.index'))
    '''
