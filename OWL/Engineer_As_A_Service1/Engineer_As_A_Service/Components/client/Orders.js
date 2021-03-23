const { Component, mount,useState } = owl;
const { xml } = owl.tags;


export class Orders extends Component {
	constructor() {
        super(...arguments);debugger
        // this.env.bus.on('session_val', this, this.session_val);
        this.state = useState({
            'data': orders.final_order_list,
        });

    }
	static template = xml`<div class="container">  
                    <div class="mt-5 mb-5">
					   <h1>Orders list </h1> 
                    </div>
                    <div>
    					<table class="table">
    						<thead>
    							<tr>
    								<th>id</th>
    								<th>Email</th>
    								<th>Specialist</th>
    								<th>Mobile No</th>
    								<th>Experience</th>
                                    <th>Action</th>
    							</tr>
    						</thead>
    						<tbody>
    								<t t-foreach="state.data" t-as="task" t-key="task.id">
	        							<tr>
	        								<td><t t-esc="task.engineer_id" /></td>
	        								<td><t t-esc="task.email" /></td>
	        								<td><t t-esc="task.specialist" /></td>
	        								<td><t t-esc="task.mobile_no" /></td>
	        								<td><t t-esc="task.experience" /></td>
	                                        <td><button type="submit" class="btn btn-success">View</button></td>
	        							</tr>
        							</t>
    						</tbody>
    					
    					</table>
                    </div>
					
		</div>`;
	}

    
