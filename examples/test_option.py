# -*-coding:utf8-*-
from flask_script import Manager

from manage import app

manager = Manager(app)


@manager.option('-n', '--name', dest='name', help='Your name', default='world')
@manager.option('-u', '--url', dest='url', default='www.csdn.com')
@manager.option('-p', '--port', dest='port')
def hello(name, url, port):
    'hello world or hello <setting name>'
    print('hello', name)
    print(url)
    print(port)


if __name__ == '__main__':
    manager.run()
