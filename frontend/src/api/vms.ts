import axios from 'axios'

async function getVMs() {
    return (await axios.get('http://0.0.0.0:8000/vms/')).data
}


export default function useVMs() {
    return {
        getVMs
    }
}