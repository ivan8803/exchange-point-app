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
            <tr v-for="(rate, currency) in currency_rates" :key="currency">
                <th>{{ currency }}</th>
                <td>{{ rate }}</td>
            </tr>
        </tbody>
    </table>
  </div>
</template>

<script>
import getCurrencyRates from '../composables/getCurrencyRates'

export default {
    setup() {
        const { currency_rates, get_rates_error, loadCurrencyRates } = getCurrencyRates()
        loadCurrencyRates()

        return { currency_rates }
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