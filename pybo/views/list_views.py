from datetime import datetime
from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect
from .. import db
from pybo.models import List, Comments
from ..forms import ListForm , CommentsForm

bp = Blueprint('list', __name__, url_prefix='/list')

@bp.route('/list/')
def _list():

    page = request.args.get('page', type=int, default=1)
    list_list = List.query.order_by(List.create_date.desc())
    list_list = list_list.paginate(page, per_page=10)
    return render_template('list/list_list.html',list_list=list_list)

'''

    #입력 파라미터
    page = request.args.get('page', type=int, default=1)
    kw = request.args.get('kw', type=str, default='')

    #조회
    list_list = List.query.order_by(List.create_date.desc())
    if kw:
        search = '%%{}%%'.format(kw)
        list_list = list_list.filter(List.gubun.ilike(search) |
                                     List.service.ilike(search) |
                                     List.name.ilike(search) |
                                     List.role.ilike(search) |
                                     List.roc.ilike(search) ).distinct()

    # 페이징
    list_list = liost_list.paginate(page, per_page=10)
    return render_template('list/list_list.html', list_list=list_list, page=page, kw=kw)

'''
@bp.route('/detail/<int:list_id>/')
def detail(list_id):
    form = CommentsForm()
    list = List.query.get_or_404 (list_id)
    return render_template('list/list_detail.html',list=list, form=form)


@bp.route('/create/', methods=('GET','POST'))
def create():
    form = ListForm()
    if request.method == 'POST' and form.validate_on_submit():
        list = List(gubun = form.gubun.data, service = form.service.data, role = form.role.data, name = form.name.data, roc = form.roc.data, create_date=datetime.now())
        db.session.add(list)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('list/list_form.html', form=form)

@bp.route('/modify/<int:list_id>', methods=('GET','POST'))
def modify(list_id):
    list = List.query.get_or_404(list_id)
    if request.method =='POST':
        form = ListForm()
        if form.validate_on_submit():
            form.populate_obj(list)
            list.modify_date = datetime.now()
            db.session.commit()
            return redirect(url_for('list.detail', list_id=list_id))
    else:
        form = ListForm(obj=list)
    return render_template('list/list_form.html', form=form)

@bp.route('/delete/<int:list_id>')
def delete(list_id):
    list = List.query.get_or_404(list_id)
    db.session.delete(list)
    db.session.commit()
    return redirect(url_for('list._list'))
