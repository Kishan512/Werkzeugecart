from odoo import http
from odoo.http import request


class Main(http.Controller):
    @http.route('/home', type="http")
    def home(self, **kwargs):
        request.session.get('user_id') and request.session.pop('user_id')
        request.session.get('user_name') and request.session.pop('user_name')
        # students = request.env['user.list'].search([])
        return request.render('Engineer_as_a_service.home')

    @http.route('/login', type="http")
    def login(self, **kwargs):
        return request.render('Engineer_as_a_service.login')    
    
    @http.route('/login_submit', type="http")
    def login_submit(self, **kwargs):
        res_eng = request.env['engineer'].search([('email', '=', kwargs.get('email')),('password', '=', kwargs.get('password'))])
        res_cli = request.env['client'].search([('email', '=', kwargs.get('email')),('password', '=', kwargs.get('password'))])
        

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



    @http.route('/signup', type="http")
    def signup(self, **kwargs):
        return request.render('Engineer_as_a_service.signup')

    @http.route('/signup_engineer', type="http")
    def signup_engineer(self, **kwargs):
        service = request.env['service'].search([])
        return request.render('Engineer_as_a_service.signup_engineer',{'service':service})


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
            'rating': 0,
            })

        return http.local_redirect('/login')


# -------------------------------client side--------------------------------------

    @http.route('/home_client', type="http")
    def home_client(self, **kwargs):
        return request.render('Engineer_as_a_service.home_client')

    @http.route('/service', type="http")
    def service(self, **kwargs):
        service = request.env['service'].search([])
        engineers = request.env['engineer'].search([])
        return request.render('Engineer_as_a_service.service',{'service':service,'engineers':engineers})

        filter_by_service_engineer_list

    @http.route('/service/filter_by_service_engineer_list/<string:service_name>', type="http")
    def filter_by_service_engineer_list(self,service_name, **kwargs):
        filter_engineer_list = request.env['engineer'].search([('specialist','=',service_name)])
        return request.render('Engineer_as_a_service.filter_engineer_list',{'filter_engineer_lists' : filter_engineer_list,'service_name' : service_name})

    @http.route('/client_Engineer_list', type="http")
    def client_Engineer_list(self, **kwargs):
        engineer_list = request.env['engineer'].search([('role', '=', 'engineer')])
        return request.render('Engineer_as_a_service.client_Engineer_list',{'engineer_list' : engineer_list})
    
    @http.route('/client_Engineer_list/book/<int:engineer_id>/<int:client_id>', type="http")
    def book(self,engineer_id,client_id, **kwargs):
        return request.render('Engineer_as_a_service.book',{'engineer_id' : engineer_id, 'client_id' : client_id })


    @http.route('/book_engineer/<int:engineer_id>/<int:client_id>', type="http")
    def book_engineer(self,engineer_id,client_id, **kwargs):
        order_id = request.env['orders'].create({
            'engineer_id' : engineer_id,
            'client_id' : client_id,
            'order_status' : "1"
        })  
        request.env['job_work_detail'].create({
            'order_id' : order_id.id,
            'product_name': kwargs.get("pname"),
            'product_problem': kwargs.get("pproblem"),
            'job_address': kwargs.get("address"),
        })  
        return request.render('Engineer_as_a_service.home_client')


       

    @http.route('/client_Engineer_list/view_engineer_deatail/<int:engineer_id>', type="http")
    def view_engineer_deatail(self,engineer_id, **kwargs):
        engineer_list = request.env['engineer'].browse(engineer_id)
        return request.render('Engineer_as_a_service.view_engineer_detail',{'engineer_list' : engineer_list})

            
    @http.route('/orders', type="http")
    def orders(self, **kwargs):
        order_list = request.env['orders'].search([('client_id', '=', request.session.get('user_id'))],order="create_date desc")
        return request.render('Engineer_as_a_service.orders',{'order_list':order_list})

    @http.route('/orders/view_order_deatail/<int:order_id>', type="http")
    def view_order_deatail(self,order_id, **kwargs):
        order_list = request.env['orders'].browse(order_id)
        product_detail = request.env['job_work_detail'].search([('order_id', '=', order_id)])

        rating_id = request.env['ratings'].search([('order_id', '=', int(order_id))])
        return request.render('Engineer_as_a_service.view_order_deatail',{'order_list' : order_list,'product_detail' : product_detail,'rating_id' : rating_id})
        

    @http.route('/rating', type="http", method="POST",csrf=False)
    def rating(self, **kwargs):

        eng = request.env['ratings'].create({
            'engineer_id': kwargs.get("engineer_id"),
            'client_id': kwargs.get("client_id"),
            'order_id': kwargs.get("order_id"),
            'rating': kwargs.get("rating"),
            'feedback': kwargs.get("feedback"),
            })
        rating_id = request.env['ratings'].search([('engineer_id', '=', int(kwargs.get("engineer_id")))])
        ratings = round(rating_id.cal_rating())
        engineer_id = request.env['engineer'].browse(int(kwargs.get("engineer_id")))
        if engineer_id:
            engineer_id.write({
                'rating' : ratings
            })
        return request.render('Engineer_as_a_service.home_client')


    @http.route('/client_profile', type="http")
    def client_profile(self, **kwargs):
        profile = request.env['client'].search([('id', '=', request.session.get('user_id'))])
        return request.render('Engineer_as_a_service.client_profile',{'profile' : profile})



# --------------------------------Engineer side----------------------------------


    @http.route('/jobs', type="http")
    def jobs(self, **kwargs):
        client_detail = request.env['orders'].search([('engineer_id', '=', request.session.get('user_id'))],order="create_date desc")
        return request.render('Engineer_as_a_service.jobs',{'jobs' : client_detail})

    @http.route('/view_jobs_detail/<int:order_id>', type="http")
    def view_jobs_detail(self,order_id, **kwargs):
        order_detail = request.env['orders'].browse(order_id)
        product_detail = request.env['job_work_detail'].search([('order_id', '=', order_id)])
        rating = request.env['ratings'].search([('order_id', '=', order_id)])
        return request.render('Engineer_as_a_service.view_jobs_detail',{'order_detail' : order_detail,'product_detail' : product_detail,'rating':rating})

    
    @http.route('/job_status_change/<int:order_id>/<string:status>', type="http")
    def job_status_change(self,order_id,status, **kwargs):
        print(status)
        if status == "accept":    
            order = request.env['orders'].browse(order_id)
            if order:
                order.write({
                    'order_status' : "2"
                })
        elif status == "decline":
            order = request.env['orders'].browse(order_id)
            if order:
                order.write({
                    'order_status' : "0"
                })
        elif status == "delivered":
            order = request.env['orders'].browse(order_id)
            if order:
                order.write({
                    'order_status' : "3"
                })

                
        return request.render('Engineer_as_a_service.home_client')

    @http.route('/Engineer_profile', type="http")
    def Engineer_profile(self, **kwargs):
        profile = request.env['engineer'].search([('id', '=', request.session.get('user_id'))])
        return request.render('Engineer_as_a_service.Engineer_profile',{'profile' : profile})
