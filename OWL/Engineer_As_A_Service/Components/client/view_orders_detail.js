const { Component, mount, useState } = owl;
const { xml } = owl.tags;



export class view_orders_detail extends Component {
	constructor() {
        super(...arguments);
        this.env.bus.on('view_orders_detail', this, this.view_orders_detail);
        this.state = useState({
            data: [],
        });

    }

    view_orders_detail (ev) {
        this.valid=ev.valid
        this.state.data = this.valid
    }
	
    static template = xml`<div class="container mt-5">
            <div>
                <h3 class="container mb-5" style="font-size:36px;">Service Order Detail</h3>
            </div>
            <table class="table table-striped">
                <thead class="bg-dark text-white">
                    <tr>
                        <th data-field="key" scope="col" class="key">Key</th>
                        <th data-field="value" scope="col">Value</th>
                    </tr>
                </thead>
                <tbody>
                    <t t-foreach="state.data" t-as="task" t-key="task.id">
                    <tr>
                        <td>Id</td>
                        <td><t t-esc="task.engineer_id" /></td>
                    </tr>
                    <tr>
                        <td>Name</td>
                        <td><t t-esc="task.fname" /></td>
                    </tr>
                    <tr>
                        <td>Mobile No</td>
                        <td><t t-esc="task.mobile_no" /></td>
                    </tr>
                    <tr>
                        <td>Specialist</td>
                        <td><t t-esc="task.specialist" /></td>
                    </tr>
                    <tr>
                        <td>experience</td>
                        <td><t t-esc="task.experience" /></td>
                    </tr>
                    </t>
                </tbody>
            </table>
        </div>`;
    }

    