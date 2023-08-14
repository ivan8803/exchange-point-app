<template>
  <div>
    <h2 class="convert-header">Conversion table</h2>
    <div id="table-container">
        <form @submit.prevent="handleClick" id="convert-table">
            <div class="convert-group">
                <label for="">from</label>
                <select v-model="currency_from" required>
                    <option value="" selected disabled hidden>--currency--</option>
                    <option v-for="currency in currency_types" :key="currency" :value="currency">{{ currency }}</option>
                </select>
            </div>
            <div class="convert-group">
                <label for="">amount</label>
                <input type="number" v-model="amount">
                <p v-if='submit_error' class="error">{{ submit_error }}</p>
            </div>
            <div class="convert-group">
                <label for="">to</label>
                <select v-model="currency_to" required>
                    <option value="" selected disabled hidden>--currency--</option>
                    <option v-for="currency in currency_types" :key="currency" :value="currency">{{ currency }}</option>
                </select>
            </div>
        </form>
        
        <h2 class="convert-result">{{ result }}</h2>
        <input class="convert-submit" type="submit" form="convert-table" value="convert">
    </div>
  </div>
</template>

<script>
export default {
    data() {
        return {
            currency_types: null,
            currency_from: '',
            currency_to: '',
            amount: 0,
            result: 0,
            submit_error: '',

            get_currency_error: '',
            get_rates_error: ''
        }
    },
    methods: {
        getCurrency() {
            fetch("http://127.0.0.1:5000/currency_type")
                .then(res => res.json() )
                .then(data => this.currency_types = data)
                .catch(err => this.get_currency_error = err.message)
        },
        async convert() {
            const res = await fetch('http://127.0.0.1:5000/convert'
             + '?convert_from=' + this.currency_from
             + '&convert_to=' + this.currency_to
             + '&amount=' + this.amount
             )
             
            let r = await res.json()
            this.result = r.toFixed(2)
        },
        handleClick() {
            this.submit_error = this.amount < 0 ? 'Enter a number greater than zero' : ''

            if (this.amount >= 0) {
                this.convert()
            }
        }
    },
    mounted() {
        this.currency_types = this.getCurrency()
    }

}
</script>

<style>
    .convert-header {
        text-transform: uppercase;
        font-weight: bold;
    }

    #table-container {
        max-width: 600px;
        margin:auto;

    }

    #convert-table {
        width: 100%;
        display: flex;
        margin: 0 auto;
        justify-content: space-around;
        background-color: rgb(131, 185, 232);
        padding: 20px;
        border-radius: 10px 10px 0 0;
    }

    .convert-group {
        display: flex;
        flex-direction: column;
    }

    .convert-submit {
        width: 100%;
        background-color: rgb(16, 70, 117);
        border: none;
        padding: 5px;
        border-radius: 0 0 10px 10px;
        text-transform: uppercase;
        font-weight: bold;
        font-size: 1.5rem;
        letter-spacing: 1px;
        color:aliceblue;
    }

    .convert-submit:hover {
        background-color: rgb(12, 51, 85);
    }

    .convert-group input, .convert-group select {
        height: 30px;
        border: none;
        margin: 0;
        border-radius: 5px;
        text-align: center;
    }

    .convert-group select {
        padding: 0 25px 0 25px;
    }

    #convert-table label {
        font-size: 1.4rem;
        font-weight: bold;
        text-transform: uppercase;
        padding-bottom: 10px;
    }

    .convert-result {
        background-color: rgb(131, 185, 232);
        margin: 0;
        font-size: 3rem;
        padding-bottom: 15px;
    }
</style>