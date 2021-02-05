const { Component, mount } = owl;
const { xml } = owl.tags;

import { Navbar } from "./navComponent.js";

export class Signup extends Component {
  static components = { Navbar };
  static template = xml`<div>
                                <Navbar/>
                                    <h1>SignUp Here</h1>
                                    <form action="#">
                                        <div class="form-group">
                                            <label for="email">Email address:</label>
                                            <input type="email" class="form-control" placeholder="Enter email" id="email"/>
                                        </div>
                                        <div class="form-group">
                                            <label for="pwd">Password:</label>
                                            <input type="password" class="form-control" placeholder="Enter password" id="pwd"/>
                                        </div>
                                         <div class="form-group">
                                            <label for="Address">Address:</label>
                                            <input type="text" class="form-control" placeholder="Enter Address" id="add"/>
                                        </div>
                                        <div class="form-group">
                                            <label for="mobile-no">Mobile No:</label>
                                            <input type="number" class="form-control" placeholder="Enter Mobile number" id="mobile-no"/>
                                        </div>
                                         <div class="form-group">
                                            <label for="Specialist">Specialist:</label>
                                            <input type="text" class="form-control" placeholder="Enter Specialist" id="specialist"/>
                                        </div>
                                        <div class="form-group form-check">
                                            <label class="form-check-label">
                                                <input class="form-check-input" type="checkbox"/> Remember me
                                            </label>
                                        </div>
                                        <button type="submit" class="btn btn-primary">Submit</button>
                                    </form></div>`;
}

    