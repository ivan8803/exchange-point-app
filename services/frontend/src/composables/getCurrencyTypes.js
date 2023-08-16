import { ref } from 'vue'
import getAppData from './appData'

const getCurrencyTypes = (path) => {
    //<summary>the function returns reference object for data, error message and load function for updating currency type list </summary>
    //>returns type="data: ref(null), error: ref(null) and load: function" />

    const { ip, port } = getAppData()
    const url = 'http://' + ip + ':' + port + '/' + 'currency_type'
    const currency_types = ref(null)
    const error = ref(null)

    const loadCurrencyTypes = async () => {
        try {
            let res = await fetch(url)
            if (!res.ok) {
                throw Error('currency_types not found')
            }
            currency_types.value = await res.json()
        }
        catch (err) {
            error.value = err.message
            console.log(error.value)
        }
    }
    return { currency_types, error, loadCurrencyTypes }
}

export default getCurrencyTypes
