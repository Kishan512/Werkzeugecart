const { Component, mount, Store, qweb } = owl;
const { xml } = owl.tags;
const { EventBus } = owl.core;
const { RouteComponent } = owl.router
const { whenReady } = owl.utils;
const { useRef, useDispatch, useState, useStore } = owl.hooks;

import { HeaderComponent } from "./include/HeaderComponent.js";
import { FooterComponent } from "./include/FooterComponent.js";

import { Home } from "./HomeComponent.js";
import { Signup } from "./signUpComponent.js";
// engineer
import { signup_engineer } from "./signup_engineer.js";
import { Login } from "./LoginComponent.js";
import { HomeEngineer } from "./engineer/HomeEngineer.js";
import { Engineers } from "./engineer/Engineers.js";
import { Jobs } from "./engineer/Job_list.js";
import { Profile } from "./engineer/Profile_engineer.js";
import { New_Jobs_engineer } from "./engineer/New_Jobs_engineer.js";
// Client
import { HomeClient } from "./client/HomeClient.js";



class home extends Component {
   static components = {RouteComponent,HeaderComponent,FooterComponent };

   static template = xml`<div>
        <div>
          <HeaderComponent/>
          <RouteComponent/>
          <FooterComponent/> 
        </div>
    </div>`;

}       


const ROUTES = [
    // Before Login
    { name: "home", path: "/", component: Home },
    { name: "signup", path: "/signup", component: Signup },
    { name: "signup_engineer", path: "/signupEngineer", component: signup_engineer },
    { name: "login", path: "/login", component: Login },
    // engineer
    { name: "engineers", path: "/engineers", component: Engineers },
    { name: "HomeEngineer", path: "/homee", component: HomeEngineer },
    { name: "jobs", path: "/jobs", component: Jobs },
    { name: "profile", path: "/profile", component: Profile },
    { name: "new_jobs_engineer", path: "/new_jobs", component: New_Jobs_engineer },
    // client
    { name: "HomeClient", path: "/home", component: HomeClient },
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