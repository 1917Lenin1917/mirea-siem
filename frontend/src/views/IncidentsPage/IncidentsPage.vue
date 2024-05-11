<script setup lang="ts">
import DataTable from "../../components/data-table/DataTable.vue";
import {ref} from "vue";
import {Table} from "../../namespaces/table";
import {Incidents} from "../../namespaces/incidents";
import {COLUMNS} from "../../table-configs/incidents";
import AppModal from "../../components/base/AppModal.vue";

const apiItems = ref([//emulating objects from backend
  {
    time: '18:33',
    date: '07.04.2024',
    label: 'test',
    priority: "info" as Incidents.Priority,
  },
  {
    time: '18:33',
    date: '07.04.2024',
    label: 'test',
    priority: "info" as Incidents.Priority,
  },
])

const itemToPreview = ref()
const isPreviewModalOpen = ref<boolean>(false)

const items = ref<Incidents.IncidentItem[]>(apiItems.value.map((item, index) => {
  return {
    ...item,
    actions: [
      {
        title: 'Показать подробности',
        value: () => openInfoModal(item)
      }
    ],
  }
}))

const openInfoModal = (item) => {
  itemToPreview.value = item
  isPreviewModalOpen.value = true
}

</script>

<template>
  <v-card class="w-100 h-100 bg-color3 px-6 d-flex flex-column rounded-0 overflow-auto custom-scrollbar" flat>
    <v-card-title class="pl-0 text-color1 font-weight-bold page__title pt-4">
      Инциденты
    </v-card-title>
    <v-card-subtitle class="pa-0">
      Хост: 111.111.11.1
    </v-card-subtitle>
    <data-table :columns="COLUMNS" :items="items" />
  </v-card>
  <app-modal v-model="isPreviewModalOpen" @confirm="isPreviewModalOpen = false" @close="isPreviewModalOpen = false" title="Подробности" no-cancel-button>
    <v-card-text class="text-surface-variant">
      Описание: тест
    </v-card-text>
  </app-modal>
</template>

<style scoped lang="scss">
.page {
  &__title {
    font-size: 28px;
  }
}
.card {
  &__header {
    font-size: 20px;
    margin-bottom: 60px;
  }
  &__text {
    &--success {
      color: #33374d;
    }
  }
}
</style>