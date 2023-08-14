<template>
  <div v-if="!error" id="nameday">Today is {{ name }}'s day</div >
</template>

<script>
export default {
    name: 'Nameday',
    data() {
        return {
            name: null,
            error: null
        }
    },
    mounted() {
        fetch("http://127.0.0.1:5000/name_day")
            .then(res => res.json() )
            .then(name => this.name = name)
            .catch(err => this.error = err.message)
    }
}
</script>

<style>
    #nameday {
        font-size: 1.5rem;
        font-weight: bold;
        padding-top: 1rem;
        color: rgb(33, 37, 41);
    }
</style>