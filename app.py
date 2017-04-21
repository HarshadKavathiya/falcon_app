import os
import mimetypes
from wsgiref import simple_server
from controller import *
WEBSITE_BASE_URL = '127.0.0.1'
WEBSITE_BASE_PORT = 80
# from project.component import *
import falcon

if __name__ == "__main__":
    def static(req, res, static_dir='static', index_file='index.html'):
        path = static_dir + req.path
        if req.path == '/':
            path += index_file
        if os.path.isfile(path):
            res.content_type = mimetypes.guess_type(path)[0]
            res.status = falcon.HTTP_200
            res.stream = open(path)
        else:
            res.status = falcon.HTTP_404


    apps = falcon.API()

    app.add_route("/get-distance/", GetData())
    app.add_route("/post-distance/", PostData())
    app.add_sink(static)

    host = WEBSITE_BASE_URL
    port = WEBSITE_BASE_PORT
    httpd = simple_server.make_server(host, port, app)
    print("Serving on %s:%s" % (host, port))
    httpd.serve_forever()