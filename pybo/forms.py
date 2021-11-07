from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired


class ListForm(FlaskForm):
    gubun = StringField('구분', validators=[DataRequired('필수 입력항목입니다.')])
    service = StringField('서비스', validators=[DataRequired('필수 입력항목입니다.')])
    role = StringField('롤', validators=[DataRequired('필수 입력항목입니다.')])
    name = StringField('호스트네임', validators=[DataRequired('필수 입력항목입니다.')])
    roc = StringField('위치', validators=[DataRequired('필수 입력항목입니다.')])


class CommentsForm(FlaskForm):
    comment = TextAreaField('코맨트', validators=[DataRequired('필수입력 항목입니다.')])
