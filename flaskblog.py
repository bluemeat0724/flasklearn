from flask import Flask, render_template, url_for, redirect, flash
from forms import RegistrationForm, LoginForm
# 运用template
app = Flask(__name__)

app.config['SECRET_KEY'] = 'a4f630629c6baaa138ba8981aa424b1f'
# dummydata
posts = [
    {
        'author': 'ryan',
        'title': 'learn lesson1',
        'content': 'class2',
        'date_posted': '9/11'
    },
    {
        'author': 'g',
        'title': 'learn lesson2',
        'content': 'class3',
        'date_posted': '9/12'
    }
]

# 我们使用 route() 装饰器告诉 Flask 什么样的URL 能触发我们的函数。


@app.route("/")
@app.route("/home")
def home():
    # 运用templates，需要加载render_template函数
    return render_template('home.html', posts=posts)  # 设置加载的数据为posts


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'Post'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account created for {}!'.format(form.username.data), 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'Post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == "password":
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful, please check username and password!', 'danger')
    return render_template('login.html', title='Login', form=form)
# 网页制作好后在密令行，进入py文件所在目录，
# 设置运行环境 set FLASK_APP=flaskblog.py
# 运行 flask run
# 开启debug模式运行网页，刷新可随时提现修改效果 set FLASK_DEBUG=1


# 直接通过python 启动网页服务
#__name__是一个变量，记录python所运行的模板的名称。如果一个文件直接被python运行
#，则变量的赋值为‘__main__’,如果__name__这个变量值为‘__mian__’则我们知道当前文件是被直接运行的而不是被导入后运行的
if __name__ == '__main__':
    app.run(debug=True)  # debugmode
# 设置上述判断后可在命令行直接打开python文件启动网页 python flaskblog.py


@app.route("/about")
def about():
    return render_template('about.html', title='About')
