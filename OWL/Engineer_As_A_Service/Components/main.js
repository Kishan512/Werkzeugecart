const { Component, mount, Store, qweb } = owl;
const { xml } = owl.tags;
const { EventBus } = owl.core;
const { RouteComponent } = owl.router
const { whenReady } = owl.utils;
const { useRef, useDispatch, useState, useStore } = owl.hooks;

import { HeaderComponent } from "./HeaderComponent.js";
import { FooterComponent } from "./FooterComponent.js";
import { Home } from "./HomeComponent.js";
import { Signup } from "./signUpComponent.js";
import { Login } from "./LoginComponent.js";
import { HomeAfterLogin } from "./HomeAfterLogin.js";
import { Engineers } from "./Engineers.js";



class home extends Component {
   static components = {RouteComponent,HeaderComponent,FooterComponent };

   static template = xml`<div>
        <div>
          <HeaderComponent/>
          <RouteComponent/>
          <FooterComponent/> 
        </div>
    </div>`;

        async willStart() {debugger
            const session_id = document.cookie;
            if(session_id){
                const xhr = new window.XMLHttpRequest();
                xhr.open('POST', '/session_validate');
                xhr.send(JSON.stringify({'session_id': session_id}));
                xhr.onload = async () => {
                    const response = JSON.parse(xhr.response);
                    if (response.valid === true) {
                        this.env.bus.trigger('login_changed', {valid: true});
                        this.env.router.navigate({to:'homeafterlogin'});
                    }
                };
            }
        }
    }       


const ROUTES = [
    { name: "home", path: "/", component: Home },
    { name: "signup", path: "/signup", component: Signup },
    { name: "login", path: "/login", component: Login },
    { name: "engineers", path: "/engineers", component: Engineers },
    { name: "homeafterlogin", path: "/home", component: HomeAfterLogin },
];


function makeEnvironment() {
    const env = { qweb };   
    const router = new owl.router.Router(env, ROUTES);
    env.router.start();
    env.bus = new EventBus();
    return env;
}


home.env = makeEnvironment()

function setup() {
    const app = new home();
/*    app.env.router.navigate({to: 'signup'});
*/    app.mount(document.body);
}

whenReady(setup);