<template>
  <nav>
    <router-link :to="{name: 'dashRoute'}">Dashboard</router-link> |
    <router-link to="/">Home</router-link> |
    <router-link :to="{name: 'testRoute'}">Test</router-link> |
    <router-link :to="{name: 'registerRoute'}">Register</router-link> |
    <router-link :to="{name: 'loginRoute'}">Logins</router-link> |
    <router-link :to="{name: 'createCategoryRoute'}">Create Category</router-link> |
    <router-link :to="{name: 'createProductRoute'}">Create Product</router-link> |    
    <router-link to="/about">About</router-link>
  </nav>
  <router-view/>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
