<template>
  <div class="CategoryCreate">
    <h2>Create a new category</h2>
    <form @submit.prevent="this.postCategory()">
      <label for="name">Name: </label>
      <input type="text" id="name" v-model="this.name" required />
      <label for="desc">Description: </label>
      <input type="text" id="desc" v-model="this.desc" required />
      <button type="submit">Create</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "categoryCreate",
  data() {
    return {
      name: "",
      desc: "",
      token: null,
    };
  },
  beforeCreate() {
    if (!localStorage.getItem("authToken")) {
      this.$router.push({ name: "loginRoute" });
    }
  },
  methods: {
    async postCategory() {
        if(this.name === "" || this.desc === ""){
            alert("Please fill in all fields")
            return
        }
      axios
        .post(
          "http://localhost:5000/api/category",
          {
            name: this.name,
            description: this.desc,
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
  },
};
</script>
