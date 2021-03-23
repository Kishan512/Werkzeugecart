const { Component, mount, useState } = owl;
const { xml } = owl.tags;


export class client_Engineer_list extends Component {
     constructor() {
        super(...arguments);
        // this.env.bus.on('session_val', this, this.session_val);
        this.state = useState({
            'data': users.data_list,
        });

    }

    async book_engineer(ev){debugger
        const eng_id = ev.target.id;
        const xhr = new window.XMLHttpRequest();
            xhr.open('POST', '/book_engineer');
            xhr.send(JSON.stringify({'id': eng_id}));
            xhr.onload = async () => {
                const response = JSON.parse(xhr.response);
                if(response.book_engineer === "success"){
                    this.env.router.navigate({to:'Orders'});
                }
                else{
                    this.env.router.navigate({to:'home'});
                }
               
            }
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
                                    <t t-foreach="state.data" t-as="task" t-key="task.id">
                                    <tr>
                                        <td><t t-esc="task.engineer_id" /></td>
                                        <td><t t-esc="task.email" /></td>
                                        <td><t t-esc="task.specialist" /></td>
                                        <td><t t-esc="task.mobile_no" /></td>
                                        <td><t t-esc="task.experience" /></td>
                                        <td><button type="submit" class="btn btn-danger" t-att-id='task.engineer_id' t-on-click="book_engineer">Book</button></td>
                                        <td><button type="submit" class="btn btn-success">View</button></td>
                                    </tr>
                                    </t>
                            </tbody>
                        
                        </table>
                    </div>
                    
        </div>`;

        
}

    