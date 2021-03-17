const { Component, mount, useState } = owl;
const { xml } = owl.tags;


export class HeaderComponent extends Component {

    constructor() {
        super(...arguments);
        this.env.bus.on('login_changed', this, this._loginChanged);
        // this.env.bus.on('session_val', this, this.session_val);
        this._updateState();
    }
    _updateState() {debugger
        this.state = useState({
            user_id: owl.session_info.user_id,
            is_valid: owl.session_info.is_valid,
            session_id: owl.session_info.session_id,
            role: owl.session_info.role
        });
        console.log(this.state.role)
    }
    // before loging
    Home(ev){
         this.env.router.navigate({ to: 'home' });
    }
    signup(ev){
         this.env.router.navigate({ to: 'signup' });
    }
    login(ev){
         this.env.router.navigate({ to: 'login' });
    }
    // engineer
    HomeEngineer(ev){
         this.env.router.navigate({ to: 'HomeEngineer' });
    }
    engineers(ev){
         this.env.router.navigate({ to: 'engineers' });
    }
    jobs(ev){
         this.env.router.navigate({ to: 'jobs' });
    }
    profile(ev){
         this.env.router.navigate({ to: 'profile' });
    }
    new_jobs_engineer(ev){
         this.env.router.navigate({ to: 'new_jobs_engineer' });
    }
    // client
    homeclient(ev){
         this.env.router.navigate({ to: 'HomeClient' });
    }
    
    async logout(ev){
        const xhr = new window.XMLHttpRequest();
            xhr.open('POST', '/do_logout');
            xhr.send(JSON.stringify({'session_id': this.state.session_id}));
            xhr.onload = async () => {
                const response = JSON.parse(xhr.response);
                if (response.logout === 'success') {
                    document.cookie = 'session_id=null';
                    owl.session_info = {
                        user_id: null,
                        is_valid: false,
                        session_id: null,
                        role: null,
                    };
                    this._updateState();
                    this.env.router.navigate({ to: 'home' });
                }
            }
        }
    
    _loginChanged (ev) {debugger
        this._updateState();
    }
   


    static template = xml`<div>
        <nav class="navbar navbar-expand-md  navbar-light bg-info">
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav mr-auto">
                <t t-if="state.user_id and state.is_valid">
                    <t t-if="state.role === 'engineer'">
                        <a class="navbar-brand" t-on-click="HomeEngineer">LOGO</a>
                            <li class="nav-item active">
                               <button class="nav-link btn-warning mr-2" t-on-click="HomeEngineer">Home</button>
                            </li>
                             <li class="nav-item">
                                <button class="nav-link btn-warning mr-2" href="#" t-on-click="engineers">Engineers</button>
                            </li>
                            <li class="nav-item">
                                <button class="nav-link btn-warning mr-2" href="#" t-on-click="jobs">Jobs</button>
                            </li>
                            <li class="nav-item">
                                <button class="nav-link btn-warning mr-2" href="#" t-on-click="profile">Profile</button>
                            </li>
                            <li class="nav-item">
                                <button class="nav-link btn-warning mr-2" href="#" t-on-click="new_jobs_engineer">New Jobs</button>
                            </li>
                            <li class="nav-item">
                                <button class="nav-link btn-warning ml-3" href="#" t-on-click="logout">Logout</button>
                            </li>
                    </t>
                    <t t-else="">
                    <a class="navbar-brand" t-on-click="homeclient">LOGO</a>
                        <li class="nav-item active">
                           <button class="nav-link btn-warning mr-2" t-on-click="homeclient">Home</button>
                        </li>
                        <li class="nav-item">
                            <button class="nav-link btn-warning ml-3" href="#" t-on-click="logout">Logout</button>
                        </li>
                    </t>
                </t>     
                <t t-else="">
                    <a class="navbar-brand" t-on-click="Home">LOGO</a>
                    <li class="nav-item active">
                       <button class="nav-link btn-warning mr-2" t-on-click="Home">Home</button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-link btn-warning mr-2" href="#" t-on-click="login">Login</button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-link btn-warning mr-2" href="#" t-on-click="signup">Signup</button>
                    </li>
                </t>
                </ul>
                
            </div>
        </nav>
        </div>`;
}