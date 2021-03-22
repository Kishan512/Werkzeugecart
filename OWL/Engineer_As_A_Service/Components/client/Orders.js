const { Component, mount,useState } = owl;
const { xml } = owl.tags;


export class Orders extends Component {
	constructor() {
        super(...arguments);debugger
        // this.env.bus.on('session_val', this, this.session_val);
        this.state = useState({
            'engineer_id': orders.get_order_list.engineer_id,
            'email': orders.get_order_list.email,
            'specialist': orders.get_order_list.specialist,
            'mobile_no': orders.get_order_list.mobile_no,
            'experience': orders.get_order_list.experience,
        });
        console.log(orders.get_order_list.engineer_id)

    }
	static template = xml`<div class="container">  
                    <div class="mt-5 mb-5">
					   <h1>Engineers list </h1> 
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
    								<th>View</th>
    							</tr>
    						</thead>
    						<tbody>
        							<tr>
        								<td><t t-esc="state.engineer_id" /></td>
        								<td><t t-esc="state.email" /></td>
        								<td><t t-esc="state.specialist" /></td>
        								<td><t t-esc="state.mobile_no" /></td>
        								<td><t t-esc="state.experience" /></td>
        								<td><button type="submit" class="btn btn-danger" t-on-click="book_engineer">Book</button></td>
                                        <td><button type="submit" class="btn btn-success">View</button></td>
        							</tr>
    						</tbody>
    					
    					</table>
                    </div>
					
		</div>`;
	}

    
