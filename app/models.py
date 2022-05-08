from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin, current_user
from . import login_manager
#...

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    profile_pic_path = db.Column(db.String(255),)
    password_secure = db.Column(db.String(255))
   
    @property
    def password(self):
        # block access to password
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)

    def __repr__(self):
        return f'User {self.username}'



class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'

#################################### Pitches###########







# # COMMENT
# class Comment(db.Model):
#     ___tablename__='users'

#     id = db.Column(db.Integer,primary_key = True)
#     pitch_id = db.Column(db.Integer)
#     user_id = db.Column(db.Integer)
#     comment = db.Column(db.String(255))


#     def save_comment(self,comment):
#         db.session.add(comment)
#         db.session.commit()

#     @classmethod
#     def get_comments(cls,id):
#         comments = Comment.query.filter_by(pitch_id=id).all()
#         return comments


# #like comments
# class like_comment(db.Model):
#     ___tablename__='users'

#     id = db.Column(db.Integer,primary_key = True)
    
#     like = db.Column(db.Integer)


#     def save_likes(self,like):
#         db.session.add(like)
#         db.session.commit()

#     def add_likes(cls,id):
#         likes = like_comment(user = current_user, pitch_id = id)
#         return likes.save_likes()

# # dislikes
# class dislike_comment(db.Model):
#     ___tablename__='users'
    

