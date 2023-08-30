from flask import render_template,request,url_for,redirect,flash,jsonify;
from app import app,db;
from app.schemas.database import Encuesta;
import re;
from sqlalchemy import func,case;

def verify_input(req:request):
    if (re.match(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',req.form.get('Email')) 
        and req.form.get('age') and req.form.get('sex') and req.form.get('favorite')):
        if db.session.query(func.count(Encuesta.email)).filter(Encuesta.email==req.form.get('Email')).first()[0]==0:
            return True;
        flash('Ese Correo ya se encuentra ya registrado','Error');
    elif not req.form.get('sex'):
        flash('No selecciono su sexo','Error');
    elif not req.form.get('age'):
        flash('No inserto su rango de Edad','Error');
    elif not req.form.get('favorite'):
        flash('No inserto su Red Favorita','Error');
    else:
        flash('Correo invalido','Error');
    return False;

def webs_age_category(ok,search,count=False):
    if count:
        nroEncuestas = Encuesta.query.count();
        return [(db.session.query(func.sum(ok)).filter(Encuesta.age_category==i).first()[0])/nroEncuestas for i in search];
    return [(db.session.query(func.count(ok)).filter(Encuesta.favorite_web==i).first()[0]) for i in search];

@app.route('/')
def index():
    nroEncuestas = Encuesta.query.count();
    return render_template('home.html',styles='CSS/styleHome.css', nroEncuestas=nroEncuestas);

@app.route('/Grafs')
def grafs():
    all_encuesta_time = (Encuesta.time_Facebook,Encuesta.time_Whatsapp,Encuesta.time_Twitter,Encuesta.time_Instagram,Encuesta.time_Tiktok);
    times_prom = [float(db.session.query(func.avg(encuest)).first()[0]) for encuest in all_encuesta_time];
    data_to_return = {
        'times_prom': times_prom,
        'favorite': webs_age_category(Encuesta.favorite_web,['Facebook','Whatsapp','Twitter','Instagram','Tiktok']),
        'age_Fb': webs_age_category(Encuesta.time_Facebook,['18-25','26-33','34-40','40+'],True),
        'age_Wp': webs_age_category(Encuesta.time_Whatsapp,['18-25','26-33','34-40','40+'],True),
        'age_Tw': webs_age_category(Encuesta.time_Twitter,['18-25','26-33','34-40','40+'],True),
        'age_In': webs_age_category(Encuesta.time_Instagram,['18-25','26-33','34-40','40+'],True),
        'age_Tk': webs_age_category(Encuesta.time_Tiktok,['18-25','26-33','34-40','40+'],True)
    };
    return jsonify(data_to_return);

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method == 'POST':
        if verify_input(request):
            new_survey = Encuesta(email=request.form.get('Email'),age_category=request.form.get('age'),
                                  sex=request.form.get('sex'),favorite_web=request.form.get('favorite'),
                                  time_Facebook=request.form.get('timeFacebook'),
                                  time_Whatsapp=request.form.get('timeWhatsapp'),
                                  time_Twitter=request.form.get('timeTwitter'),
                                  time_Instagram=request.form.get('timeInstagram'),
                                  time_Tiktok=request.form.get('timeTiktok'));
            db.session.add(new_survey);
            db.session.commit();
            return redirect(url_for('index'));
        return render_template('form.html',styles='CSS/styleForm.css',messages=True);
    return render_template('form.html',styles='CSS/styleForm.css');

app.secret_key = '\xabI\x82TI\xe6\x9a\xe0\xf7hn\xd3';