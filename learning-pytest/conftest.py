import pytest


def pytest_addoption(parser):
    parser.addoption('--host', action='store',
                     help='host of db')
    parser.addoption('--port', action='store', default='8888',
                     help='port of db')


def test_option1(pytestconfig):
    print('host: %s' % pytestconfig.getoption('host'))
    print('port: %s' % pytestconfig.getoption('port'))

# pytestconfig 其实是 request.config 的快捷方式，所以也可以自定义固件实现命令行参数读取。
@pytest.fixture
def config(request):
    return request.config


# test_config.py

def test_option2(config):
    print('host: %s' % config.getoption('host'))
    print('port: %s' % config.getoption('port'))
