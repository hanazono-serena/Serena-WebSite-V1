import smtplib
import os
from email.mime.text import MIMEText
from email.header import Header

import tornado.escape
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application, HTTPError
from tornado.web import RequestHandler

EMAIL_SENDER = ''
EMAIL_RECEIVER = ''
SMTP_HOST = ''
SMTP_USER = ''
SMTP_PASS = ''


class BaseHandler(RequestHandler):

    def data_received(self, chunk: bytes):
        pass

    def set_default_headers(self) -> None:
        try:
            origin = self.request.headers['Origin']
        except KeyError:
            origin = '*'
        self.set_header("Access-Control-Allow-Origin", origin)
        self.set_header("Access-Control-Allow-Headers", "Content-Type,Access-Token,X-XSRFToken,Set-Cookie")
        self.set_header("Access-Control-Allow-Credentials", "true")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def options(self):
        self.set_status(204)
        self.finish()


class IndexHandler(BaseHandler):
    def get(self):
        self.finish('Hello')


class ContactHandler(BaseHandler):
    def get(self):
        # self.render('index.html')
        self.finish(dict(token=self.xsrf_token.decode()))

    def post(self):
        self.check_xsrf_cookie()
        data = tornado.escape.json_decode(self.request.body)
        print(data)
        email_subject = 'Message from website: ' + data.get('name') + ' ' + data.get('email')
        email_body = 'name:' + data.get('name') + '\n' + \
                     'email:' + data.get('email') + '\n' + \
                     'title:' + data.get('title') + '\n' + \
                     'message:' + data.get('message') + '\n'
        email_message = MIMEText(email_body, 'plain', 'utf-8')
        email_message['From'] = Header('hanazono serena site <' + EMAIL_SENDER + '>', 'utf-8')
        email_message['To'] = Header('serena', 'utf-8')
        email_message['Subject'] = Header(email_subject, 'utf-8')
        try:
            smtp = smtplib.SMTP()
            smtp.connect(SMTP_HOST, 25)
            smtp.login(SMTP_USER, SMTP_PASS)
            smtp.sendmail(EMAIL_SENDER, [EMAIL_RECEIVER], email_message.as_string())
            self.finish('succeed')
            return
        except smtplib.SMTPException:
            self.set_status(500)
            self.finish('failed')
        self.set_status(500)
        self.finish('failed')


class APP(Application):
    def __init__(self):
        settings = {
            'xsrf_cookies': True,
            "cookie_secret": "HpJZdo5ah9GIl9A*9s1nN2qadLtWt#IJ",
            'template_path': os.path.join(os.path.dirname(__file__), 'template')
        }
        handlers = [
            (r"/", IndexHandler),
            (r"/contact", ContactHandler)
        ]
        Application.__init__(self, handlers, **settings)


def main():
    app = APP()
    server = HTTPServer(app)
    server.bind(6001)
    server.start()
    IOLoop.current().start()


if __name__ == '__main__':
    main()
