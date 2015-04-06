def load(module):
    if not hasattr(module, '__file__'):
        module = __import__(module, fromlist = [True])
    globals().update(module.__dict__)

class latebind(object):
    def __init__(self, f):
        self.f = f
    def __get__(self, obj, owner):
        return self.f(owner)
