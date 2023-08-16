import { ref } from 'vue'
import getAppData from './appData'

const getRates = (path) => {
    //<summary>the function returns reference object for data, error message and load function for updating the currency:rate dictionary </summary>
    //>returns type="data: ref(null), error: ref(null) and load: function" />

    const { ip, port } = getAppData()
    const url = 'http://' + ip + ':' + port + '/' + 'get_rates'
    const rates = ref(null)
    const error = ref(null)

    const loadRates = async () => {
        try {
            let res = await fetch(url)
            if (!res.ok) {
                throw Error('rates not found')
            }
            rates.value = await res.json()
        }
        catch (err) {
            error.value = err.message
            console.log(error.value)
        }
    }
    return { rates, error, loadRates }
}

export default getRates
