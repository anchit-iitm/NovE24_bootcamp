<template>
    <h2>login page</h2>
    <form @submit.prevent="this.post_login()">
        <label for="email">email id: </label>
        <input type="text" v-model="this.email" name="email" placeholder="email here ...">
        <label for="password">password: </label>
        <input type="password" v-model="this.password" name="password" placeholder="password....">
        <button type="submit">login</button>
    </form> 
</template>
<script>
import axios from 'axios'
export default{
    name: 'login',
    data(){
        return{
            email: '',
            password: ''
        }
    },
    methods:{
        post_login(){
            axios.post('http://localhost:5000/api/login',{
                emailFromJson: this.email,
                passwordFromJson: this.password
            })
            .then(response => {
                console.log(response)
                if(response.status == 200){
                    localStorage.setItem('authToken', response.data.authToken)
                    this.$router.push({name: 'home'})
                }
            })
            .catch(error => {
                console.log(error)
            })
        }
    }
}
</script>