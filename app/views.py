from app import app, db
from flask import render_template, request, redirect, url_for
from app.models import Tambah
from app.forms import addPlatform

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/list', methods=['GET'])
def viewPlatform():
    platforms = Tambah.query.all()
    return render_template('view.html', platforms=platforms)

@app.route('/add', methods = ['GET','POST'])
def AddPlatform():
    # Add Platform
    form = addPlatform()
    if request.method == 'POST':
    # sesuai dengan forms.py
        Platform = request.form['Platform']
        Email = request.form['Email']
        Password = request.form['Password']
        
        new_data = Tambah(Platform=Platform, Email=Email, Password=Password)
        try:
            db.session.add(new_data)
            db.session.commit()
            return redirect(url_for('viewPlatform'))
        except Exception as e:
            print(f'ERROR:{e}')
            return f'ERROR:{e}'
        
    return render_template('add.html', form=form)
    
@app.route('/edit/<int:id>', methods=['GET','POST'])
def edit(id:int):
    data = Tambah.query.get_or_404(id)
    form = addPlatform(obj=data)
    if form.validate_on_submit():
        data.Platform = form.Platform.data
        data.Email  = form.Email.data
        data.Password  = form.Password.data
        try:
            db.session.commit()
            return redirect(url_for('viewPlatform'))
        except Exception as e:
            return f'ERROR:{e}'
    else:
        return render_template('edit.html', form=form)

@app.route('/delete/<int:id>')
def delete(id:int):
    delete_platform = Tambah.query.get_or_404(id)
    try:
        db.session.delete(delete_platform)
        db.session.commit()
        return redirect(url_for('viewPlatform'))
    except Exception as e :
        return f'ERROR:{e}'










