import {ref} from "vue";

type Script = {id:number, name: string, description: string}
type StatusBody = {
    title: string,
    color: string,
}
export const AVAILABLE_STATUSES: Record<string, StatusBody> = {
    '0': {
        title: 'Не выполнен',
        color: `grey`,
    },

    '1': {
        title: 'Выполнен. Найдена ошибка',
        color: `red`,
    },

    '2': {
        title: 'Выполнен. Ошибок не найдено',
        color: `green`,
    }
}

export interface ExtendedScript extends Script {
    isLoading: boolean
    status: StatusBody
    statusText?: string
    recommendationText?: string[]
}

const scriptsList = ref<ExtendedScript[]>([])

const setScriptsList = (newValue: Script[]): void => {
    scriptsList.value = newValue.map((script: Script): ExtendedScript => {
        return {
            ...script,
            isLoading: false,
            status: AVAILABLE_STATUSES['0']
        }
    })
}
const setIsScriptLoading = (script: ExtendedScript, newVal: boolean): void => {
    script.isLoading = newVal
}

export default function useScriptsStore() {
    return {
        scriptsList,
        setScriptsList,
    }
}