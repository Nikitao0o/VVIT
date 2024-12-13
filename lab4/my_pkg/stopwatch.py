from datetime import datetime as dt

def func_time(func):
    def wrapped(*args, **kwargs):
        start_time = (dt.now().time().second * (10**6)) + dt.now().time().microsecond
        f = func(*args, **kwargs)
        end_time = (dt.now().time().second * (10**6)) + dt.now().time().microsecond
        time = end_time - start_time
        print(str(time//(10**6)) + '.' + str(time%(10**6)) + ' Sec')
        return f
    return wrapped
