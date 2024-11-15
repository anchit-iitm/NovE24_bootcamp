<template>
    <div class="dashboard">
        <h1>Dashboard</h1>
        <!-- {{ categories }} -->
        <h2>Categories</h2>
        <table>
            <thead>
                <tr>
                    <td>id</td>
                    <td>name</td>
                    <td>description</td>
                    <td>status</td>
                    <td>created_at</td>
                    <td>created_by</td>
                    <td>updated_at</td>
                    <td>updated_by</td>
                    <td>action</td>
                </tr>
            </thead>
            <tbody>
                <tr v-for="category in this.categories" :key="category.id">
                    <td>{{ category.id }}</td>
                    <td>{{ category.name }}</td>
                    <td>{{ category.description }}</td>
                    <td>{{ category.status }}</td>
                    <td>{{ category.created_at }}</td>
                    <td>{{ category.created_by }}</td>
                    <td><div v-if="category.updated_at == null"> ! </div>{{ category.updated_at }}</td>
                    <td><div v-if="category.updated_by == null"> ! </div>{{ category.updated_by }}</td>
                    <td><button v-if="category.delete == false" @click="this.deletecategory(category.id)">Delete{{ category.delete }}</button> | <button>Update</button></td>
                </tr>
            </tbody>
        </table>
        <h2>Product</h2>
        <table>
            <thead>
                <tr>
                    <td>id</td>
                    <td>name</td>
                    <td>description</td>
                    <td>status</td>
                    <td>created_at</td>
                    <td>created_by</td>
                    <td>updated_at</td>
                    <td>updated_by</td>
                    <td>delete</td>
                </tr>
            </thead>
            <tbody>
                <tr v-for="category in this.products" :key="category.id">
                    <td>{{ category.id }}</td>
                    <td>{{ category.name }}</td>
                    <td>{{ category.description }}</td>
                    <td>{{ category.status }}</td>
                    <td>{{ category.created_at }}</td>
                    <td>{{ category.created_by }}</td>
                    <td><div v-if="category.updated_at == null"> ! </div>{{ category.updated_at }}</td>
                    <td><div v-if="category.updated_by == null"> ! </div>{{ category.updated_by }}</td>
                    <td><button v-if="category.delete == false" @click="this.deleteProducts(category.id)">Delete</button> | <button>Update</button></td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Dashboard',
    data() {
        return {
            token: null,
            categories: null,
            products: null
        }
    },
    created() {
        this.token = localStorage.getItem("authToken")
        if (!this.token) {
            this.$router.push({ name: "loginRoute" });
            return
        }
        this.getCategories()
        this.getProducts()
    },
    methods:{
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
    },
    async getProducts(){
        axios
        .get('http://localhost:5000/api/product',
          {
            headers: {
              'Authorization': `${this.token}`,
            },
          }
        )
        .then(response => {
            if(response.status == 200){
                console.log(response);
                this.products = response.data.data
                console.log(this.categories);                
            }
        })
        .catch(error => {
          alert(error.response.data.response.errors[0])
        })
    },
    async deleteProducts(id){
        axios
        .delete(`http://localhost:5000/api/product/${id}`,
          {
            headers: {
              'Authorization': `${this.token}`,
            },
          }
        )
        .then(response => {
            if(response.status == 201){
                this.getProducts()              
            }
        })
        .catch(error => {
          alert(error.response.data.response.errors[0])
        })
    },
    async deletecategory(id){
        axios
        .delete(`http://localhost:5000/api/category/${id}`,
          {
            headers: {
              'Authorization': `${this.token}`,
            },
          }
        )
        .then(response => {
            if(response.status == 201){
                this.getCategories()              
            }
        })
        .catch(error => {
          alert(error.response.data.response.errors[0])
        })
    }
    }
}
</script>

<style>
table {
    width: 100%;
    border-collapse: collapse;
}
thead {
    background-color: #f2f2f2;
}
th, td {
    border: 1px solid #f2f2f2;
    padding: 8px;
    text-align: left;
}
</style>