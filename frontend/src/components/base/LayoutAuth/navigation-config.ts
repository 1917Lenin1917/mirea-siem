import useApp from "../../../store/app.ts";
const { currentHost } = useApp()

export type MenuItem = {
    label: string,
    redirect: { name: string },
    isVisible: boolean,
}

export default function useNavigationConfig() {
    const MENU_ITEMS: MenuItem[] = [{
        label: 'Установка соединения',
        redirect: { name: 'connect' },
        isVisible: true,
    },{
        label: 'Инциденты',
        redirect: { name: 'incidents' },
        isVisible: true
    },{
        label: 'Рекомендации',
        redirect: { name: 'recommendations' },
        isVisible: true
    },{
        label: 'Скрипты',
        redirect: { name: 'scripts' },
        isVisible: true
    } ]
    
    return {
        MENU_ITEMS,
    }
}