<template>
    <h1>test page</h1>
    <form action="">
        <label for="text">please add some text: </label>
        <input type="text" name="text" id="" v-model="this.message"><br>
        <!-- <button type="submit" @click.prevent="testMethod()">submit</button> -->
        <button type="button" @click="testMethod()">submit</button>
        <button type="button" @click="testPost()">post</button>
    </form>
    <br>{{ this.text }}
    <button type="button" @click="testGet()">test get</button>
</template>
<script>
import axios from 'axios'
export default {
    name: 'testRoute',
    data() {
        return {
            text: '',
            message: 'Hello Vue!'
        }
    },
    created() {
        console.log('created')
        this.testGet()
    },
    methods: {
        testMethod(){
            console.log("trying to call a method and print a var: ", this.message)
        },
        async testGet(){
            axios
                .get('http://localhost:5000/homeNew1')
                .then(response => {
                    console.log('good response/then block', response)
                    if (response.status >= 200 && response.status < 300) {
                        this.text = response.data.nameFromPythonBackend
                    }   
                })
                .catch(error => {
                    console.log('bad response/catch block', error)
                })
        },
        async testPost(){
            axios
                .post('http://localhost:5000/test_post',
                    {
                        'nameFromHtml': this.message
                    }
                )
                .then(response => {
                    console.log('good response/then block', response)
                    if (response.status >= 200 && response.status < 300) {
                        this.text = response.data
                    }   
                })
                .catch(error => {
                    console.log('bad response/catch block', error)
                })
        }
    }
}
</script>