import sys
import inspect

def main(fn):
    """Call fn with command line arguments.  Used as a decorator.
    """
    if inspect.stack()[1][0].f_locals['__name__'] == '__main__':
        args = sys.argv[1:] # Discard the script name from command line
        fn(*args) # Call the main function
    return fn

def trace(fn):
    """A decorator that prints a function's name, its arguments, and its return
    values each time the function is called. For example,

    @trace
    def compute_something(x, y):
        # function body
    """
    def wrapped(*args, **kwds):
        global indent
        reprs = [repr(e) for e in args]
        reprs += [repr(k) + '=' + repr(v) for k, v in kwds.items()]
        indent = '  ' * trace.level
        trace.level += 1
        try:
            print('{0}-> {1}({2})'.format(indent, fn.__name__, ', '.join(reprs)))
            result = fn(*args, **kwds)
            print('{0}<- {1}({2}) returns {3}'.format(indent,
                                                     fn.__name__,
                                                     ', '.join(reprs),
                                                     repr(result)))
        finally:
            trace.level -= 1
        return result
    trace.level = 0
    return wrapped 