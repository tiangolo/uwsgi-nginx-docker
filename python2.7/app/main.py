# test.py
def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    #return [b"Hello World"] # python3
    return ["Hello World from default uWSGI app (default)"] # python2
