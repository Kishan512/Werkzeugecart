const { Component, mount, Store, qweb } = owl;
const { xml } = owl.tags;
const { whenReady } = owl.utils;
const { useRef, useDispatch, useState, useStore } = owl.hooks;

import { Signup } from "./signUpComponent.js";
import { Navbar } from "./navComponent.js";



class home extends Component {
  static components = { Navbar };

  static template = xml`<div>
                            <Navbar/>
                        </div>`;

}


const ROUTES = [
    { name: "signup", path: "/signup", component: Signup },
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
    app.mount(document.body);
}

whenReady(setup);