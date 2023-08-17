<template>
  <div v-if="!error" id="nameday">Today is {{ name }}'s day</div >
</template>

<script>
import getAppData from '@/composables/appData'

export default {
    name: 'Nameday',
    data() {
        return {
            name: null,
            error: null
        }
    },
    mounted() {
        this.getNameday()
    },
    methods: {
        getNameday() {
            const { ip, port } = getAppData()
            const url = 'http://' + ip + ':' + port + '/' + 'name_day'

            fetch(url)
                .then(res => res.json() )
                .then(res => this.name = res["nameday"])
                .catch(res => this.error = res.message)
        }
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