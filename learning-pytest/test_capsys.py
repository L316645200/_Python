# capsys 用于捕获 stdout 和 stderr 的内容，并临时关闭系统输出
import sys


def ping(output):
    print('Pong...', file=output)


def test_stdout(capsys):
    ping(sys.stdout)
    out, err = capsys.readouterr()
    assert out == 'Pong...\n'
    assert err == ''


def test_stderr(capsys):
    ping(sys.stderr)
    out, err = capsys.readouterr()
    assert out == ''
    assert err == 'Pong...\n'