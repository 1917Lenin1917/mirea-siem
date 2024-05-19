import axios from 'axios'

async function getVMs() {
    return (await axios.get('http://26.41.183.33:8000/vms/')).data
}


export default function useVMs() {
    return {
        getVMs
    }
}