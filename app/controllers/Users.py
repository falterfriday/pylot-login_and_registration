"""
    This is the CONTROLLER
"""
from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)

        self.load_model('User')
        self.db = self._app.db

    def index(self):
        return self.load_view('index.html')

    def create(self):
        user_info = {
        'first_name':request.form['first_name'], 
        'last_name':request.form['last_name'],
        'email':request.form['email'],
        'password':request.form['password'],
        'pw_confirmation':request.form['pw_confirmation'],
        }
        create_status = self.models['User'].create_user(user_info)

        if create_status['status'] == True:
            session['id'] = create_status['user']['id']
            session['name'] = create_status['user']['first_name']
            name = session['name']
            return self.load_view('success.html', name=name)
        else:
            for message in create_status['errors']:
                flash( message, 'regis_errors')

            return redirect('/')
    
    def login(self):
        user_info = {
        'email':request.form['email'],
        'password':request.form['password']
        }
        login_status = self.models['User'].login_user(user_info)
        
        if login_status['status'] == True:
            session['id'] = login_status['user']['first_name']
            name = session['name']
            return self.load_view('success.html', name=name)
        else:
            for message in login_status['errors']:
                flash( message, 'login_errors')
            return redirect('/')
