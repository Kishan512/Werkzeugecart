const { Component, mount } = owl;
const { xml } = owl.tags;
const { whenReady } = owl.utils;
const { useRef, useDispatch, useState, useStore } = owl.hooks;


// -------------------------------------------------------------------------
// Task Component
// -------------------------------------------------------------------------



// -------------------------------------------------------------------------
// App Component
// -------------------------------------------------------------------------
const APP_TEMPLATE = xml /* xml */`
        <div>
          <nav id="nav">
                <h1 id="h1">Shop.com</h1>
          </nav>
          <div class="task-list">

                <center><input type="text" name="search" id="search" t-on-keyup="searchFunction()" placeholder="Search"/></center><br></br><br></br>
                <t t-foreach="products" t-as="product" t-key="product.id">
                    <div class="task">
                           <span><t t-esc="product.Product_name"/></span>
                           <span class="pricetag"><t t-esc="product.price"/></span>
                           <button type="button" t-att-id="product.id" class="addtocart" t-on-click="addtocart" >Add to cart</button>
                    </div>
                </t> 
          </div>
          <div class="split2"> 
          <h2>---Cart---</h2>
                   <t t-foreach="tasks" t-as="task" t-key="task.id">

                      <span><t t-esc="products[task.product_id-1].Product_name"/></span>
                      <span class="delete" t-att-id="task.product_id" t-on-click="deleteTask">🗑</span><br></br>
                   </t>
          </div>
        </div>`;






class App extends Component {
   static template = APP_TEMPLATE;     
    addtocart(ev) {

        // 13 is keycode for ENTER
        const product_id = ev.target.id; 
            if (product_id && (!this.tasks.find(t => parseInt(t.product_id) == parseInt(product_id)))) {
                const newTask = {
                    product_id: product_id,
                };
                console.log(product_id);
                this.tasks.push(newTask);
            }
    }
    deleteTask(ev) {
       
        const index = this.tasks.findIndex(t => t.product_id == ev.target.id);
        this.tasks.splice(index, 1);
    }

    searchFunction(ev){
      const search = ev.target.value; 
      console.log(search);
      
    }

    tasks = useState([]);
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


// Setup code
function setup() {
  owl.config.mode = "dev";
  const app = new App();
  app.mount(document.body);
}

whenReady(setup);