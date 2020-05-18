
# call,可用作装饰器
class Singteton(object):
    _instance = None

    def __init__(self, cls):
        self._cls = cls

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = self._cls(*args, **kwargs)
        return self._instance
