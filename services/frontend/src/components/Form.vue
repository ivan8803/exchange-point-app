<template>
  <div>
    <h2 class="form-header">Transaction form</h2>
    <form @submit.prevent="handleSubmit" id="send-money-form">
        <div class="f-group">
            <label>Amount in CZK:</label>
            <input v-model="amount" type="number" required>
        </div>
        <div v-if="amount_error" class="error">{{ amount_error }}</div>
        <div class="f-group">
            <label>Account:</label>
            <input type="text" v-model="account" placeholder="Account number" required>
        </div>
        <div class="f-group">
            <label>Currency:</label>
            <select v-model="currency" required>
                <option value="" selected disabled hidden>--Select currency--</option>
                <option v-for="currency in currency_types" :key="currency" :value="currency">{{ currency }}</option>
            </select>
        </div>
        <div class="f-group">
            <label>Converted amount:</label>
            <p>{{ rounded_converted_amount }} {{ currency }}</p>
        </div>
        <div class="f-group">
            <button class="submit-button">Send</button>
        </div>
    </form>
  </div>
</template>

<script>
import { ref } from 'vue'
import getCurrencyTypes from '../composables/getCurrencyTypes'
import getCurrencyRates from '../composables/getCurrencyRates'

    export default {
        setup() {
            // loading list of currency types
            const { currency_types, get_currency_error, loadCurrencyTypes } = getCurrencyTypes()
            loadCurrencyTypes()

            // loading curency:rate dictionary
            const { currency_rates, get_rates_error, loadCurrencyRates } = getCurrencyRates('get_rates')
            loadCurrencyRates()

            const currency = ref('')
            const amount = ref(0)
            const account = ref('')
            const converted_amount = ref(0)
            const rounded_converted_amount = ref(0)
            const amount_error = ref('')
            
            const convert_error = ref(null)

            

            return { currency_types, get_currency_error, currency_rates, get_rates_error, currency, amount, 
                account, converted_amount, rounded_converted_amount, amount_error, convert_error }
        },
        methods: {
            convertAmount() {
                let rate = this.currency_rates[this.currency]
                this.converted_amount = this.amount/rate
            },
            roundAmount(amount) {
                return amount.toFixed(2)
            },
            handleSubmit() {
                this.amount_error = this.amount >= 0 ? '' : 'Enter a non-negative amount'

                console.log(this.amount_error)

                if (!this.amount_error) {
                    const request = { "amount": this.amount, "account": this.account, "currency": this.currency, "converted_amount": this.converted_amount }
                    console.log(request)
                }
            }
        },
        updated() {        
            if (this.currency && this.amount >= 0) {
                this.convertAmount()
                this.rounded_converted_amount = this.roundAmount(this.converted_amount)
            }
        }
}
</script>

<style>
    #send-money-form {
        max-width: 420px;
        padding: 20px 10px 20px 10px;
        border-radius: 10px;
        margin: auto;
        text-align: center;
        background-color: rgb(131, 185, 232);
        box-shadow: 4px 4px 10px rgb(87, 87, 87);
    }

    .f-group {
        display: flex;
        justify-content: space-between;
        padding: 10px 0 10px 0;
        color: rgb(33, 37, 41);
        font-weight: bold;
        font-size: 1.3rem;
    }
    
    .f-group:last-child {
        padding: 0;
        display: block;
    }

    .f-group input, .f-group select, .f-group p {
        width: 50%;
        border: none;
        border-radius: 5px;
        text-align: center;
    }

    .submit-button {
        font-family: Verdana, Geneva, Tahoma, sans-serif;
        padding: 5px 20px;
        border: none;
        border-radius: 10px;
        background-color: rgb(27, 88, 163);
        text-transform: uppercase;
        color:white;
        letter-spacing: 2px;
    }

    .error {
        color:crimson;
        text-align: end;
    }

    .note {
        color: black;
        padding-top: 1rem;
    }

    .form-header {
        text-transform: uppercase;
        font-weight: bold;
    }
</style>