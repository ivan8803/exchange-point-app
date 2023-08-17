import { ref } from 'vue'
import getAppData from './appData'

const getCurrencyTypes = (path) => {
    //<summary>the function returns reference object for data, error message and load function for updating currency type list </summary>
    //>returns type="data: ref(null), error: ref(null) and load: function" />

    const { ip, port } = getAppData()
    const url = 'http://' + ip + ':' + port + '/' + 'currency_types'
    const currency_types = ref(null)
    const get_currency_error = ref(null)

    const loadCurrencyTypes = async () => {
        try {
            let res = await fetch(url)
            if (!res.ok) {
                throw Error('currency_types not found')
            }
            // currency_types.value = await res.json()
            let temp = await res.json()
            currency_types.value = temp["currency_types"]
        }
        catch (err) {
            get_currency_error.value = err.message
            console.log(error.value)
        }
    }
    return { currency_types, get_currency_error, loadCurrencyTypes }
}

export default getCurrencyTypes
