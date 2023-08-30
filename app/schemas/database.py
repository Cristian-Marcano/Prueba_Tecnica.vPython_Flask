from app import db;

class Encuesta(db.Model):
    id = db.Column(db.Integer,primary_key=True);
    email = db.Column(db.String(120),unique=True,nullable=False);
    age_category = db.Column(db.Enum('18-25','26-33','34-40','40+'),nullable=False);
    sex = db.Column(db.Enum('M','F'),nullable=False);
    favorite_web = db.Column(db.Enum('Facebook','WhatsApp','Twitter','Instagram','Tiktok'));
    time_Facebook = db.Column(db.Integer,nullable=False,default=0);
    time_Whatsapp = db.Column(db.Integer,nullable=False,default=0);
    time_Twitter = db.Column(db.Integer,nullable=False,default=0);
    time_Instagram = db.Column(db.Integer,nullable=False,default=0);
    time_Tiktok = db.Column(db.Integer,nullable=False,default=0);