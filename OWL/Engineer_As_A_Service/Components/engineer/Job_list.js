const { Component, mount } = owl;
const { xml } = owl.tags;



export class Jobs extends Component {
  static template = xml`<div>   
            <div class="mb-5 ml-5 mt-5">
                <div class="row">
                    <h1>Recent Jobs list </h1> 
                </div>
            </div>
        </div>`;
}

    