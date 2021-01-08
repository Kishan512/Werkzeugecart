const { Component, mount } = owl;
const { xml } = owl.tags;
const { whenReady } = owl.utils;
const { useRef, useDispatch, useState, useStore } = owl.hooks;
class App extends Component {
  static template = xml/* xml */ `
    <div class="task-list" t-on-delete-task="deleteTask">
          <h1><center>Shop.com</center></h1>
          <t t-foreach="products" t-as="product" t-key="product.id">
              <div class="task">
                     <span><t t-esc="product.Product_name"/></span>
                     <span class="pricetag"><t t-esc="product.price"/></span>
                     <button type="button" t-att-id="product.Product_name" class="addtocart" t-on-click="addtocart" >Add to cart</button>
              </div>
          </t>
          <h2>---Cart---</h2>
           <t t-foreach="tasks" t-as="task" t-key="tasks.id">
            <span><t t-esc="task.title"/></span>
            <span class="delete" t-on-click="deleteTask">🗑</span>
           </t>       
    </div>`;
    
     
    addtocart(ev) {

        // 13 is keycode for ENTER
        const title = ev.target.id; 
            if (title) {
                const newTask = {
                    title: title,
                };
                this.tasks.push(newTask);
            }
    }
deleteTask(ev) {
    const index = this.tasks.findIndex(t => t.id === ev.detail.id);
    this.tasks.splice(index, 1);
}

tasks = useState([]);
products = [
               {
      "id": "1",
        "Product_name": "Shirt",
        "price": "100"
    },
    {
      "id": "2",
        "Product_name": "cap",
        "price": "700"
    },
    {
      "id": "3",
        "Product_name": "jacket",
        "price": "5000"
    },
    {
      "id": "4",
        "Product_name": "hoddie",
        "price": "2000"
    },
    {
      "id": "5",
        "Product_name": "T-shirt",
        "price": "300"
    },
    {
      "id": "6",
        "Product_name": "jarcy",
        "price": "4000"
    }
  ];
}


// Setup code
function setup() {
  const app = new App();
  app.mount(document.body);
}

whenReady(setup);