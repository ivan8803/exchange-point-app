<template>
    <div>
        <div class="navbar navbar-dark bg-dark py-0 flex-nowrap">
            <router-link :to="{ name: 'Home'}" class="mx-3 my-brand text-nowrap">Bank APP</router-link>
            <clock class="container justify-content-end"/>            
        </div>
        <nav class="navbar navbar-dark bg-dark py-1 justify-content-around">
            <ul class="navbar-nav flex-row">
                <li class="nav-item px-3">
                    <router-link :to="{ name: 'Home'}" class="my-link">Home</router-link>
                </li>
                <li class="nav-item px-3">
                    <router-link :to="{ name: 'Form' }" class="my-link">Form</router-link>
                </li>
                <li class="nav-item px-3">
                    <router-link :to="{ name: 'Rate' }" class="my-link">Rates</router-link>
                </li>
                <li class="nav-item px-3">
                    <router-link :to="{ name: 'Convert' }" class="my-link">Convert</router-link>
                </li>
            </ul>
        </nav>
    </div>
</template>

<script>
import Clock from './Clock.vue'

export default {
    name: "Navbar",
    components: { Clock }
}
</script>

<style>
nav ul li {
    font-weight: bold;
    padding-bottom: 5px;
}

.my-link {
    text-decoration: none;
    color: rgb(147, 147, 147);
}

.my-link:hover {
    color: rgb(193, 193, 193);
}

.router-link-active {
    color: rgb(235, 235, 235);
}

.my-brand { 
    text-decoration: none;
    font-size: 1.5rem;
    font-weight: bold;
    color: rgb(235, 235, 235);
}
</style>