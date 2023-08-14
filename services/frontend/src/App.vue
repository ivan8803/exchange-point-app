<template>
  <div>
    <Navbar />
    <Nameday class="text-end px-3" />
    <div class="view">
      <router-view />
    </div>
  </div>
</template>

<script>
  import Navbar from './components/Navbar.vue'
  import Clock from './components/Clock.vue'
  import Nameday from './components/Nameday.vue'

  export default {
    name: 'App',
    components: {
      Navbar, Clock, Nameday
    }
  }
</script>

<style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

  body {
    background-color: rgb(235, 235, 235);
  }

  .view {
    text-align: center;
    margin-top: 30px;
  }
</style>
