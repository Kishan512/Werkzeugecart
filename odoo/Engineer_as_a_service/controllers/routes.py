from odoo import http
from odoo.http import request


class Main(http.Controller):

    @http.route('/home', type="http")
    def mypath(self, **kwargs):
        # students = request.env['user.list'].search([])
        return request.render('Engineer_as_a_service.home')

    @http.route('/login', type="http")
    def login(self, **kwargs):
        return request.render('Engineer_as_a_service.login')    
    
    @http.route('/login_submit', type="http")
    def login_submit(self, **kwargs):
        # print(kwargs['email'])
        res = request.env['user.list'].search([('email', '=', kwargs.get('email')),('password', '=', kwargs.get('password'))])
        print(res)
        # import pdb; pdb.set_trace()
        if len(res):
            return request.render('Engineer_as_a_service.home_client')
        else:
            return http.local_redirect('/login')

    @http.route('/home_client', type="http")
    def home_client(self, **kwargs):
        return request.render('Engineer_as_a_service.home_client')


    @http.route('/signup', type="http")
    def signup(self, **kwargs):
        return request.render('Engineer_as_a_service.signup')

    @http.route('/signup_engineer', type="http")
    def signup_engineer(self, **kwargs):
        return request.render('Engineer_as_a_service.signup_engineer')


    @http.route('/signup_submit', type="http", method="POST", csrf=False)
    def signup_submit(self, **kwargs):
        print(kwargs)
        # import pdb; pdb.set_trace()
        request.env['user.list'].create({
            'role': "client",
            'email': kwargs.get("email"),
            'name': kwargs.get("fname"),
            'password': kwargs.get("password"),
            'address': kwargs.get("address"),
            'mobile_no': kwargs.get("mobno"),
            'specialist': kwargs.get("specialist"),
            'experience': kwargs.get("experience"),
            })
        return http.local_redirect('/login')

    @http.route('/delete/<model("user.list"):std>', type="http")
    def delete(self, std=None, **kwargs):
        # print(std)    
        # import pdb; pdb.set_trace()
        std.unlink()
        return http.local_redirect('/mypath')

    @http.route('/client_Engineer_list', type="http")
    def client_Engineer_list(self, **kwargs):
        engineer_list = request.env['user.list'].search([('role', '=', 'client')])
        return request.render('Engineer_as_a_service.client_Engineer_list',{'engineer_list' : engineer_list})
        
    @http.route('/view_engineer_deatail/<int:engineer_id>', type="http")
    def view_engineer_deatail(self,engineer_id, **kwargs):
        print(engineer_id)
        engineer_list = request.env['user.list'].browse(engineer_id)
        return request.render('Engineer_as_a_service.view_engineer_detail',{'engineer_list' : engineer_list})
        
    
    @http.route('/orders', type="http")
    def orders(self, **kwargs):
        return request.render('Engineer_as_a_service.orders')
        
    @http.route('/client_profile', type="http")
    def client_profile(self, **kwargs):
        return request.render('Engineer_as_a_service.client_profile')