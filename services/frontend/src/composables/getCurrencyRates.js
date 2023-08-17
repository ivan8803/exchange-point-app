import { ref } from 'vue'
import getAppData from './appData'

const getCurrencyRates = (path) => {
    //<summary>the function returns reference object for data, error message and load function for updating the currency:rate dictionary </summary>
    //>returns type="data: ref(null), error: ref(null) and load: function" />

    const { ip, port } = getAppData()
    const url = 'http://' + ip + ':' + port + '/' + 'get_currency_rates'
    const currency_rates = ref(null)
    const get_rates_error = ref(null)

    const loadCurrencyRates = async () => {
        try {
            let res = await fetch(url)
            if (!res.ok) {
                throw Error('currency_rates not found')
            }
            let temp = await res.json()
            currency_rates.value = temp["currency_rates"]
        }
        catch (err) {
            get_rates_error.value = err.message
            console.log(get_rates_error.value)
        }
    }
    return { currency_rates, get_rates_error, loadCurrencyRates }
}

export default getCurrencyRates
