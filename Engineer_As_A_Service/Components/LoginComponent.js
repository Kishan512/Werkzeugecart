const { Component, mount } = owl;
const { xml } = owl.tags;

import { Navbar } from "./navComponent.js";

export class Login extends Component {

  static components = { Navbar };
  static template = xml`<div>
                                <Navbar/>
                                    <div class="container mt-5">
                                    <h1 class="mb-4">Login Here</h1>
                                    <form action="#">
                                        <div class="form-group">
                                            <label for="email">Email address:</label>
                                            <input type="email" class="form-control" placeholder="Enter email" id="email"/>
                                        </div>
                                        <div class="form-group">
                                            <label for="pwd">Password:</label>
                                            <input type="password" class="form-control" placeholder="Enter password" id="pwd"/>
                                        </div>
                                        <button type="submit" class="btn btn-primary">Submit</button>
                                    </form>
                                    </div>
                                    </div>`;

}

    