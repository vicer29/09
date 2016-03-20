def application(environ, start_responcse):
    start_responcse('200 OK', [('Content-Type', 'text/plain')])
    queryString = environ['QUERY_STRING'].split('&')
    responsBody = ''
    for i in queryString:
        responsBody += i + '\n'
    return responsBody    