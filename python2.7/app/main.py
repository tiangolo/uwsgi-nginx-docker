def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ["Hello World from a default Nginx uWSGI Python 2.7 app in a\
            Docker container (default)"]
