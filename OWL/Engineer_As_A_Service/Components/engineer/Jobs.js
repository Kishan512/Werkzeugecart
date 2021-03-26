const { Component, mount, useState } = owl;
const { xml } = owl.tags;



export class Jobs extends Component {

	constructor() {
        super(...arguments);
        this.env.bus.on('arrives_jobs', this, this.arrives_jobs);
        this.state = useState({
            data: [],
        });

    }

    arrives_jobs (ev) {
        this.state.data = ev.valid
    }

    view_job_detail(ev){
        const user_id = ev.target.id;
        const xhr = new window.XMLHttpRequest();
            xhr.open('POST', '/view_job_detail');
            xhr.send(JSON.stringify({'user_id': user_id}));
            xhr.onload = async () => {
                const response = JSON.parse(xhr.response);
                this.env.bus.trigger('view_job_list', {valid: response.view_job_list});
            }
        this.env.router.navigate({ to: 'view_jobs_detail' });
    }

  	static template = xml`<div class="container">  
                    <div class="mt-5 mb-5">
                       <h1>Job Arrives List </h1> 
                    </div>
                    <div>
                        <table class="table" style="width:60%">
                            <thead>
                                <tr>
                                    <th>Email</th>
                                    <th>Mobile No</th>
                                    <th>Action</th>
                                </tr>
                            </thead>
                            <tbody>
                                     <t t-foreach="state.data" t-as="i">
                                        <tr>
                                            <td><t t-esc="i.client_name"/></td>
                                            <td><t t-esc="i.mobile_no"/></td>
                                            <td><button type="submit" t-att-id="i.user_id" t-on-click="view_job_detail" class="btn btn-success">View</button></td>
                                        </tr>
                                    </t>
                            </tbody>
                        
                        </table>
                    </div>
                    
        </div>`;
}

    