const { Component, mount, Store, qweb } = owl;
const { xml } = owl.tags;
const { RouteComponent } = owl.router
const { whenReady } = owl.utils;
const { useRef, useDispatch, useState, useStore } = owl.hooks;

import { Home } from "./HomeComponent.js";
import { Signup } from "./signUpComponent.js";
import { Login } from "./LoginComponent.js";



class home extends Component {
  static components = {RouteComponent };

  static template = xml`<div>
                            <div>
                              <RouteComponent/>
                            </div>
                        </div>`;  
   
}   


const ROUTES = [
    { name: "Home", path: "/", component: Home },
    { name: "Signup", path: "/signup", component: Signup },
    { name: "Login", path: "/Login", component: Login },
];



function makeEnvironment() {
    const env = { qweb };   
    const router = new owl.router.Router(env, ROUTES);
    env.router.start();
    return env;
}


home.env = makeEnvironment()

function setup() {
    const app = new home();
/*    app.env.router.navigate({to: 'signup'});
*/    app.mount(document.body);
}

whenReady(setup);