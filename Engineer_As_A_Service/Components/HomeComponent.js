const { Component, mount } = owl;
const { xml } = owl.tags;

import { Navbar } from "./navComponent.js";


export class Home extends Component {
  static components = { Navbar };
  static template = xml`<div>   <Navbar/>
                                <div class="mb-0 ml-5 mt-5">
                                <div class="row">
                                    <div class="col-sm-6"><br></br>
                                        <h3><font color="orange"> Best Solution of your Product</font> </h3><br></br>
                                        <h1><font color="orange">We have the amzing staff of engineer</font></h1><br></br>
                                       
                                        <button onclick="window.location.href='#';" class="btn btn-dark">Get started</button>
                                        <button onclick="window.location.href='#';" class="btn btn-danger ml-3">Login</button>
                                    </div>
                                    <div class="col-sm-6">
                                        <img src="static/images/engineer.jpg" class="img-fluid mt-5 rounded zoom" alt="Responsive image"/>
                                    </div>
                                </div>
                            </div></div>`;
        
}

    