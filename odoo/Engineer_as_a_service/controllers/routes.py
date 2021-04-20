from odoo import http
from odoo.http import request


class Main(http.Controller):
    @http.route('/home', type="http")
    def mypath(self, **kwargs):
        request.session.get('user_id') and request.session.pop('user_id')
        request.session.get('user_name') and request.session.pop('user_name')
        # students = request.env['user.list'].search([])
        return request.render('Engineer_as_a_service.home')

    @http.route('/login', type="http")
    def login(self, **kwargs):
        return request.render('Engineer_as_a_service.login')    
    
    @http.route('/login_submit', type="http")
    def login_submit(self, **kwargs):
        # print(kwargs['email'])
        res_eng = request.env['engineer'].search([('email', '=', kwargs.get('email')),('password', '=', kwargs.get('password'))])
        res_cli = request.env['client'].search([('email', '=', kwargs.get('email')),('password', '=', kwargs.get('password'))])
        

        # import pdb; pdb.set_trace()
        if len(res_eng) or len(res_cli):
            if len(res_eng):

                request.session['user_id'] = res_eng.id
                request.session['user_name'] = res_eng.name
                request.session['role'] = res_eng.role
                print("print from ;engineer" + request.session['user_name'])
                return request.render('Engineer_as_a_service.home_client')
            else:
                request.session['user_id'] = res_cli.id
                request.session['user_name'] = res_cli.name
                request.session['role'] = res_cli.role
                print("print from client" + request.session['user_name'])

                return request.render('Engineer_as_a_service.home_client')
        else:
            return http.local_redirect('/login')

    @http.route('/home_client', type="http")
    def home_client(self, **kwargs):
        request.session.get('user_id')
        return request.render('Engineer_as_a_service.home_client')


    @http.route('/signup', type="http")
    def signup(self, **kwargs):
        return request.render('Engineer_as_a_service.signup')

    @http.route('/signup_engineer', type="http")
    def signup_engineer(self, **kwargs):
        return request.render('Engineer_as_a_service.signup_engineer')


    @http.route('/signup_submit', type="http", method="POST", csrf=False)
    def signup_submit(self, **kwargs):
        # import pdb; pdb.set_trace()
        request.env['client'].create({
            'role': "client",
            'email': kwargs.get("email"),
            'name': kwargs.get("fname"),
            'password': kwargs.get("password"),
            'address': kwargs.get("address"),
            'mobile_no': kwargs.get("mobno"),
            })
        return http.local_redirect('/login')

    @http.route('/engineer_signup_submit', type="http", method="POST", csrf=False)
    def engineer_signup_submit(self, **kwargs):
        # print(kwargs)
        # import pdb; pdb.set_trace()
        request.env['engineer'].create({
            'role': "engineer",
            'email': kwargs.get("email"),
            'name': kwargs.get("fname"),
            'password': kwargs.get("password"),
            'address': kwargs.get("address"),
            'mobile_no': kwargs.get("mobno"),
            'specialist': kwargs.get("specialist"),
            'experience': kwargs.get("experience"),
            })
        return http.local_redirect('/login')

    # @http.route('/delete/<model("user.list"):std>', type="http")
    # def delete(self, std=None, **kwargs):
    #     # print(std)    
    #     # import pdb; pdb.set_trace()
    #     std.unlink()
    #     return http.local_redirect('/mypath')

    @http.route('/client_Engineer_list', type="http")
    def client_Engineer_list(self, **kwargs):
        engineer_list = request.env['engineer'].search([('role', '=', 'engineer')])
        return request.render('Engineer_as_a_service.client_Engineer_list',{'engineer_list' : engineer_list})
        
    @http.route('/view_engineer_deatail/<int:engineer_id>', type="http")
    def view_engineer_deatail(self,engineer_id, **kwargs):
        engineer_list = request.env['engineer'].browse(engineer_id)
        return request.render('Engineer_as_a_service.view_engineer_detail',{'engineer_list' : engineer_list})
    
    @http.route('/book_engineer/<int:engineer_id>/<int:client_id>', type="http")
    def book_engineer(self,engineer_id,client_id, **kwargs):
        request.env['orders'].create({
            'engineer_id' : engineer_id,
            'client_id' : client_id
        })  
        return request.render('Engineer_as_a_service.home_client')


    
    @http.route('/orders', type="http")
    def orders(self, **kwargs):
        order_list = request.env['orders'].search([('client_id', '=', request.session.get('user_id'))])
        return request.render('Engineer_as_a_service.orders',{'order_list':order_list})
        
    @http.route('/client_profile', type="http")
    def client_profile(self, **kwargs):
        return request.render('Engineer_as_a_service.client_profile')


        