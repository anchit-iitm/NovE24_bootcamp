<template>
    <h2>register page</h2>
    <form @submit.prevent="this.post_register()">
        <label for="email">email id: </label>
        <input type="text" v-model="this.email" name="email" placeholder="email here ...">
        <label for="password">password: </label>
        <input type="password" v-model="this.password" name="password" placeholder="password....">
        <label for="role">select role: </label>
        <select name="role" v-model="this.role">
            <option value="manager">Manager</option>
            <option value="customer">Customer</option>
        </select>
        <button type="submit">register</button>
    </form> 
</template>
<script>
import axios from 'axios'
export default{
    name: 'register',
    data(){
        return{
            email: '',
            password: '',
            role: ''
        }
    },
    methods:{
        post_register(){
            axios.post('http://localhost:5000/api/register',{
                emailFromJson: this.email,
                passwordFromJson: this.password,
                roleFromJson: this.role
            })
            .then(response => {
                console.log(response)
                if(response.status == 201){
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