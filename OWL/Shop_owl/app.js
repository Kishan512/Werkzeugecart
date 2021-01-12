const { Component, mount, Store } = owl;
const { xml } = owl.tags;
const { whenReady } = owl.utils;
const { useRef, useDispatch, useState, useStore } = owl.hooks;

const actions = {
    addtocart({ state }, product_id) {
        if (product_id && (!state.tasks.find(t => parseInt(t.product_id) == parseInt(product_id)))) {
                const newTask = {
                        product_id: product_id,
                };
                console.log(product_id);
                state.tasks.push(newTask);
        }
    },
    deleteTask({ state }, product_id) {
      const index = state.tasks.findIndex((t) => t.product_id == product_id);
      state.tasks.splice(index, 1);
    },
  };

const APP_TEMPLATE = xml /* xml */`
                <div>
                    <nav id="nav">
                                <h1 id="h1">Shop.com</h1>
                    </nav>
                    <div class="task-list" id="task-list">

                                <center><input type="text" name="search" id="search" t-on-keyup="searchFunction()" placeholder="Search"/></center><br></br><br></br>
                                <table id="tbl">                 
                                    <t t-foreach="products" t-as="product" t-key="product.id">
                                            <div class="task" id="task">
                                                    <tr>
                                                                 <td><span id="sp"><t t-esc="product.Product_name"/></span></td>
                                                                 <td><span id="sp1" class="pricetag"><t t-esc="product.price"/></span></td>
                                                                 <td><button type="button" t-att-id="product.id" class="addtocart" t-on-click="addtocart" >Add to cart</button></td>
                                                    </tr>
                                           </div>
                                    </t> 
                                </table>
                    </div>
                    <div class="split2"> 
                    <h2>---Cart---</h2>
                                    <table >
                                            <t t-set="total" t-value="0"/>
                                            <t t-foreach="tasks" t-as="task" t-key="task.id">
                                                <tr>
                                                        <t t-set="total" t-value="total + products[task.product_id-1].price"/>
                                                        <td><span><t t-esc="products[task.product_id-1].Product_name"/></span></td>
                                                        <td><span><t t-esc="products[task.product_id-1].price"/></span></td>
                                                        <td><span class="delete" t-att-id="task.product_id" t-on-click="deleteTask">🗑</span></td><br></br>
                                                </tr>
                                            </t>

                                    </table>
                              ---------------------------------------------------
                                    <br></br>
                                    <span>GrandTotal :<t t-esc="total"/></span>
                    </div>
                </div>`;





const tasks = [];

class App extends Component {
     static template = APP_TEMPLATE;
     tasks = useStore((state) => state.tasks)
     dispatch = useDispatch();
        addtocart(ev) {
            if (ev.target.id) {
                this.dispatch("addtocart", ev.target.id)
            }
        }
        deleteTask(ev) {
            this.dispatch("deleteTask", ev.target.id)
        }

        searchFunction(ev){
                var input, filter, mainDiv, div, childDiv, i, txtValue;
                input = document.getElementById("search").value; 
                filter = input.toUpperCase();
                mainDiv = document.getElementById("task-list");
                div = mainDiv.getElementsByClassName("task");
                for (i = 0; i < div.length; i++) {
                    childDiv = div[i].getElementsByTagName("span")[0];
                    if (childDiv) {
                        txtValue = childDiv.textContent || childDiv.innerText;
                        if (txtValue.toUpperCase().indexOf(filter) > -1) {
                            div[i].style.display = "";
                        }
                        else{
                            div[i].style.display = "none";
                        }
                    }   
                }
        } 

        products = [
                                     {
                    "id": 1,
                        "Product_name": "Shirt",
                        "price": 100
                },
                {
                    "id": 2,
                        "Product_name": "cap",
                        "price": 700
                },
                {
                    "id": 3,
                        "Product_name": "jacket",
                        "price": 5000
                },
                {
                    "id": 4,
                        "Product_name": "hoddie",
                        "price": 2000
                },
                {
                    "id": 5,
                        "Product_name": "T-shirt",
                        "price": 300
                },
                {
                    "id": 6,
                        "Product_name": "jarcy",
                        "price": 4000
                }
            ];
}

function makeStore() {
    const localState = window.localStorage.getItem("todoapp");
    const state = localState ? JSON.parse(localState) : this.tasks;
    const store = new Store({ state, actions });
    store.on("update", null, () => {
        localStorage.setItem("todoapp", JSON.stringify(store.state));
    });
    return store;
}

// Setup code
function setup() {
    owl.config.mode = "dev";
    App.env.store = makeStore();
    const app = new App();
    app.mount(document.body);
}

whenReady(setup);