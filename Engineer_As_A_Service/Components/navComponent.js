const { Component, mount } = owl;
const { xml } = owl.tags;


export class Navbar extends Component {
  static template = xml`<div>
                                <nav class="navbar navbar-expand-lg navbar-light bg-info">
                                      <a class="navbar-brand" href="#" t-on-click="Home">LOGO</a>
                                      <div class="collapse navbar-collapse" id="navbarSupportedContent">
                                        <ul class="navbar-nav mr-auto">
                                          <li class="nav-item active">
                                            <a class="nav-link" href="#" t-on-click="Home">Home</a>
                                          </li>
                                          <li class="nav-item">
                                            <a class="nav-link" href="#" t-on-click="Login">Login</a>
                                          </li>
                                          <li class="nav-item">
                                            <a class="nav-link" href="#" t-on-click="signup">SignIn</a>
                                          </li>
                                        </ul>
                                      
                                        <form class="form-inline my-2 my-lg-0">
                                          <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search"/>
                                          <button class="btn btn-outline-warning my-2 my-sm-0" type="submit">Search</button>
                                        </form>
                                      </div>
                                    </nav>
                                </div>`;
    
     
     Home(ev){
         this.env.router.navigate({ to: 'Home' });
    }
    signup(ev){
         this.env.router.navigate({ to: 'Signup' });
    }
    Login(ev){
         this.env.router.navigate({ to: 'Login' });
    }
}



