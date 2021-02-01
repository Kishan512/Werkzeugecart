import { login } from "./app.js";
const { Component, mount, Store } = owl;
const { xml } = owl.tags;
const { whenReady } = owl.utils;
const { useRef, useDispatch, useState, useStore } = owl.hooks;


class home extends Component {
  static template = xml`<div>
                                <nav class="navbar navbar-expand-sm bg-light">
                                  <ul class="navbar-nav">
                                    <li class="nav-item">
                                      <a class="nav-link" href="#">LOGIN</a>
                                    </li>
                                    <li class="nav-item">
                                      <a class="nav-link" href="app.js">SIGNUP</a>
                                    </li>
                                  </ul>
                                </nav>

                                <div>Please Login First</div>
                        </div>
                               `;
}




// Setup code
function setup() {
    const app = new home();
    app.mount(document.body);
}

whenReady(setup);