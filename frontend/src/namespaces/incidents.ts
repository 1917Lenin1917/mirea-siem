import {Table} from "./table";

export declare namespace Incidents {
    type Priority = 'info' | 'low' | 'medium' | 'high'

    type IncidentItem = {
        date: string,
        time: string,
        label: string,
        priority: Priority,
        actions: Table.TValue<(args?: unknown) => unknown>[]
    }
}