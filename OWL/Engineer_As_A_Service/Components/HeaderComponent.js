const { Component, mount, useState } = owl;
const { xml } = owl.tags;


export class HeaderComponent extends Component {

    constructor() {
        super(...arguments);
        // from willstar
        this.env.bus.on('login_changed', this, this._loginChanged);
        // this.env.bus.on('session_val', this, this.session_val);
        // this.state = useState({
        //     valid: this.valid,
        // });
    }  
   
    Home(ev){
         this.env.router.navigate({ to: 'home' });
    }
    homeAfterLogin(ev){
         this.env.router.navigate({ to: 'homeafterlogin' });
    }
    signup(ev){
         this.env.router.navigate({ to: 'signup' });
    }
    login(ev){
         this.env.router.navigate({ to: 'login' });
    }

    engineers(ev){
         this.env.router.navigate({ to: 'engineers' });
    }
    
    async logout(ev){debugger
            this.valid = ev.valid;
            const session_id = document.cookie;
            const xhr = new window.XMLHttpRequest();
            xhr.open('POST', '/do_logout');
            xhr.send(JSON.stringify({'session_id': session_id}));
            xhr.onload = async () => {
                console.log(xhr);
                document.cookie = "";
            }
            this.env.router.navigate({ to: 'home' });
        }
    
    _loginChanged (ev) {
        this.valid=ev.valid
    }
   


    static template = xml`<div>
        <nav class="navbar navbar-expand-lg navbar-light bg-info">
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav mr-auto">
                <t t-if="valid">
                <a class="navbar-brand" t-on-click="homeAfterLogin">LOGO</a>
                    <li class="nav-item active">
                       <button class="nav-link btn-warning mr-2" t-on-click="homeAfterLogin">Home</button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-link btn-warning mr-2" href="#" t-on-click="Service">Service</button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-link btn-warning mr-2" href="#" t-on-click="engineers">Engineers</button>
                    </li>
                    <li class="nav-item">
                        <button class="nav-link btn-warning mr-2" href="#" t-on-click="logout">Logout</button>
                    </li>
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
                <form class="form-inline my-2 my-lg-0">
                    <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search"/>
                    <button class="btn btn-outline-warning my-2 my-sm-0" type="submit">Search</button>
                </form>
            </div>
        </nav>
        </div>`;
}