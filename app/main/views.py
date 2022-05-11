from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required,current_user
from ..models import User,Pitch,Comment,Role, Like, Dislike
from .. import db,photos
from .forms import UpdateProfile,PitchForm,CommentForm
# from sqlalchemy.sql import func
# from sqlalchemy.orm import session
# from sqlalchemy import text



@main.route('/', methods=['GET','POST'])
def index():
   
    promotionpitches = Pitch.query.filter_by(category='promotion').order_by(Pitch.posted.desc()).all()
    interviewpitches = Pitch.query.filter_by(category="interview").order_by(Pitch.posted.desc()).all()
    businesspitches = Pitch.query.filter_by(category="business").order_by(Pitch.posted.desc()).all()
    productpitches = Pitch.query.filter_by(category="product").order_by(Pitch.posted.desc()).all()

    pitches = Pitch.query.filter_by().first()
    likes = Like.get_all_likes(pitch_id=Pitch.id)
    dislikes = Dislike.get_all_dislikes(pitch_id=Pitch.id)

    title = 'Home'
    return render_template('index.html', title = title, pitches = pitches, promotionpitches = promotionpitches, interviewpitches = interviewpitches, businesspitches = businesspitches, productpitches = productpitches, likes = likes, dislikes = dislikes)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

# profile picture
@main.route('/user/<uname>/update/pic',methods= ['POST'] )
@login_required
def update_pic(uname):
    # query db to pick up user with same uname we passed
    user = User.query.filter_by(username = uname).first()
    # request function to check if any parameter with the name photo has been passed into the request.
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
# end of profile picture
# 
# 
# 
##############add new pitch route #############################
@main.route('/pitch/new',methods = ['GET','POST'])
@login_required
def pitch():
    '''
    View pitch function that returns the pitch page and data
    '''
    pitch_form = PitchForm()
    my_likes = Like.query.filter_by(pitch_id=Pitch.id)

    if pitch_form.validate_on_submit():
        content = pitch_form.content.data
        category = pitch_form.category.data
        pitch_title = pitch_form.pitch_title.data

        new_pitch = Pitch(pitch_title=pitch_title, content=content, category = category, user = current_user)
        new_pitch.save_pitch()

        return redirect(url_for('main.index'))


    title = 'New Pitch | One Minute Pitch'
    return render_template('newpitch.html', title = title, pitch_form = pitch_form, likes = my_likes)
