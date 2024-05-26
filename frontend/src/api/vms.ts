import axios from 'axios'

async function getVMs() {
    return (await axios.get('http://localhost:8000/vms/')).data
}


export default function useVMs() {
    return {
        getVMs
    }
}