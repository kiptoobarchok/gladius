from flask import render_template, url_for, flash, redirect
from flask_login import login_user, logout_user, login_required, current_user
from application import db, bcrypt
from application.models import User
from application.main.forms import RegistrationForm, LoginForm
from flask import Blueprint

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("home.html")

@main.route("/register", methods=["GET", "POST"])
def register():
    if  current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm() 
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(firstname=form.firstname.data, lastname=form.lastname.data, email=form.email.data, username=form.username.data, profession=form.profession.data,  date_of_birth=form.date_of_birth.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.login'))
    return render_template('register.html', title='Sign Up', form=form)

@main.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("Login successful!", "success")
            return redirect(url_for("main.dashboard"))
        else:
            flash("Login failed. Check your email and password.", "danger")
    return render_template("login.html", form=form)

@main.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("main.login"))

@main.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")
