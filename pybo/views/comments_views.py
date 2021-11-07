from datetime import datetime
from flask import Blueprint, url_for, request, render_template
from werkzeug.utils import redirect
from pybo import db
from ..forms import CommentsForm
from pybo.models import List, Comments

bp = Blueprint('comments', __name__, url_prefix='/comments')

@bp.route('/create/<int:list_id>', methods=('POST', ))
def create(list_id):
    form = CommentsForm()
    list = List.query.get_or_404(list_id)
    if form.validate_on_submit():
        comment = request.form['comment']
        comment = Comments(comment=comment, create_date=datetime.now())
        list.comments_set.append(comment)
        db.session.commit()
        return redirect('{}#comments_{}'.format(url_for('list.detail',list_id=list_id), comment.id))
    return render_template('list/list_detail.html', list=list, form=form)

@bp.route('/modify/<int:comments_id>', methods=('GET','POST'))
def modify(comments_id):
    comments = Comments.query.get_or_404(comments_id)
    if request.method == "POST":
        form = CommentsForm()
        if form.validate_on_submit():
            form.populate_obj(comments)
            comments.modify_date =datetime.now()
            db.session.commit()
            return redirect('{}#comments_{}'.format(url_for('list.detail',list_id=list_id), comment.id))
    else:
        form = CommentsForm(obj=comments)
    return render_template('comments/comments_form.html', comments=comments, form=form)


@bp.route('/delete/<int:comments_id>')
def delete(comments_id):
    comments = Comments.query.get_or_404(comments_id)
    comments_id = comments.list.id
    db.session.delete(comments)
    db.session.commit()
    return redirect(url_for('list.detail',list_id=comments.list_id))