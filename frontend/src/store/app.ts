import {ref} from "vue";

const currentHost = ref<{id: number, name: string, ip_address: string, scripts: {id:number, name: string, description: string}[]} | null>(null)

export default function useApp() {
    return {
        currentHost,
        // setCurrentHost: (value) => currentHost.value = value
    }
}