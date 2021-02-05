const { Component, mount } = owl;
const { xml } = owl.tags;


export class Navbar extends Component {
  static components = { Navbar };
  static template = xml`<div>
                                <nav class="navbar navbar-expand-lg navbar-light bg-light">
                                    <div class="collapse navbar-collapse" id="navbarNav">
                                        <ul class="navbar-nav">
                                                <li class="nav-item">
                                                    <a class="nav-link" href="#" data-mode="Login" >Login</a>
                                                </li>   
                                                <li class="nav-item">
                                                    <a class="nav-link" data-mode="SignIn" t-on-click="SignIn">SignUp</a>
                                                </li>
                                        </ul>
                                    </div>
                                </nav></div>`;
    
     SignIn() {
        return this.env.router.navigate({ to: 'signup'});
    }

}


