<template>
  <div class="ProductCreate">
    <h2>Create a new product to a present category</h2>
    <form @submit.prevent="this.postProduct()">
      <label for="name">Name: </label>
      <input type="text" id="name" v-model="this.name" required />
      <label for="desc">Description: </label>
      <input type="text" id="desc" v-model="this.desc" required />
      <label for="stock">stock: </label>
      <input type="number" id="desc" v-model="this.stock" required />
      <label for="price">price: </label>
      <input type="number" id="desc" v-model="this.price" required />
      <label for="cateID">Category: </label>
      <select name="cateID" v-model="this.category_id">
            <option v-for="category in this.categories" :key="category.id" :value="category.id">{{ category.name }}</option>
        </select>
      <button type="submit">Create</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "ProductCreate",
  data() {
    return {
      name: "",
      desc: "",
      token: null,
      stock: 0,
      price: 0,
      category_id: 0,
      categories: null
    };
  },
  beforeCreate() {
    if (!localStorage.getItem("authToken")) {
      this.$router.push({ name: "loginRoute" });
    }
  },
  created(){
    this.token = localStorage.getItem("authToken")
    if(this.token){
        this.getCategories()
    }
  },
  methods: {
    async postProduct() {
        if(this.name === "" || this.desc === "" || this.stock === null || this.price === null || this.category_id === null){
            alert("Please fill in all fields")
            return
        }
        console.log(this.category_id);
        
      axios
        .post(
          "http://localhost:5000/api/product",
          {
            name: this.name,
            description: this.desc,
            stock: this.stock,
            price: this.price,
            category_id: this.category_id,  
          },
          {
            headers: {
              'Authorization': `${localStorage.getItem("authToken")}`,
            },
          }
        )
        .then((Response) => {
          if (Response.status === 201) {
            this.$router.push({ name: "home" });
          }
        })
        .catch((error) => {
          console.log(error);

          alert(error.response.data.response.errors[0]);
        });
    },
    async getCategories(){
        axios
        .get('http://localhost:5000/api/category',
          {
            headers: {
              'Authorization': `${this.token}`,
            },
          }
        )
        .then(response => {
            if(response.status == 200){
                console.log(response);
                
                this.categories = response.data.data
                console.log(this.categories);                
            }
        })
        .catch(error => {
          alert(error.response.data.response.errors[0])
        })
    }
  },
};
</script>
