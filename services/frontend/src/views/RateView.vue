<template>
  <div>
    <h2 class="rate-table-header">exchange rate to czk</h2>
    <table class="my-table">
        <thead>
            <tr>
                <th>Currency</th>
                <td>Rate</td>
            </tr>
        </thead>
        <tbody>
            <tr v-for="item in currency" :key="item">
                <th>{{ item }}</th>
                <td>{{ rates[item] }}</td>
            </tr>
        </tbody>
    </table>
  </div>
</template>

<script>
export default {
    data() {
        return {
            currency: null,
            rates: null
        }
    },
    methods: {
        async getRates() {
            const res = await fetch('http://127.0.0.1:5000/get_rates')
            const data = await res.json()
            this.currency = Object.keys(data)
            this.rates = data
        }
    },
    mounted() {
        this.getRates()
    }
}
</script>

<style>
    .my-table {
        margin: 0 auto;
        background-color: rgb(131, 185, 232);
        color: rgb(33, 37, 41);
        border-radius: 10px;
        box-shadow: 4px 4px 10px rgb(87, 87, 87);
    }

    .my-table thead {
        text-transform: uppercase;
        font-size: 1.2rem;
    }

    .my-table tbody th, .my-table tbody td {
        width: 120px
    }

    .my-table th, .my-table td {
        padding: 3px 20px 3px 20px;
    }

    .my-table tr {
        border-bottom: 1px solid rgb(255, 255, 255);
    }

    .rate-table-header {
        font-weight: bold;
        text-transform: uppercase;
    }
</style>