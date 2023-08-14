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
    <p class="note">After the transaction is confirmed, json with transaction data is written to the console</p>
  </div>
</template>

<script>
export default {
    data() {
        return {
            currency_types: null,
            rates: null,
            amount: 0, 
            account: '',
            currency: '',
            converted_amount: 0,
            rounded_converted_amount: 0,
            amount_error: '',
            
            get_rates_error: null,
            convert_error: null,
        }
    },
    methods: {
        getCurrency() {
            fetch("http://127.0.0.1:5000/currency_type")
                .then(res => res.json() )
                .then(data => this.currency_types = data)
                .catch(err => this.get_currency_error = err.message)
        },
        getRates() {
            fetch('http://127.0.0.1:5000/get_rates')
                .then(res => res.json() )
                .then(res => this.rates = res)
                .catch(err => this.get_rates_error = err.message)
        },
        convertAmount() {
            let rate = this.rates[this.currency]
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
    mounted() {
        this.getCurrency()
        this.getRates()
    },
    updated() {
        if (this.currency && this.amount !== null) {
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