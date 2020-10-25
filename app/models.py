# @@ -11,7 +11,8 @@ class User(db.Model,UserMixin):
#     secure_password = db.Column(db.String(255),nullable = False)
#     bio = db.Column(db.String(255))
#     profile_pic_path = db.Column(db.String())
#     pitches = db.relationship('Pitch', backref='user', lazy='dynamic')
#     comment = db.relationship('Comment', backref='user', lazy='dynamic')


#     @property
# @@ -41,6 +42,7 @@ class Pitch(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     title = db.Column(db.String(255))
#     post = db.Column(db.Text())
#     comment = db.relationship('Comment',backref='pitch',lazy='dynamic')
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     time = db.Column(db.DateTime, default = datetime.utcnow)
#     category = db.Column(db.String(255), index = True)
# @@ -49,6 +51,25 @@ def save_p(self):
#         db.session.add(self)
#         db.session.commit()


#     def __repr__(self):
#         return f'Pitch {self.post}'

# class Comment(db.Model):
#     __tablename__ = 'comments'
#     id = db.Column(db.Integer, primary_key=True)
#     comment = db.Column(db.Text())
#     user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
#     pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))

#     def save_p(self):
#         db.session.add(self)
#         db.session.commit()

#     def __repr__(self):
#         return f'comment:{self.comment}'



# @login_manager.user_loader
# def load_user(user_id):