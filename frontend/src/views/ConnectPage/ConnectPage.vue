<script setup lang="ts">
import {ref} from "vue";
import OverlayLoader from "../../components/OverlayLoader.vue";

const isConnectionEstablished = ref<boolean>(false)
const connecting = ref<boolean>(false)
const handleSetConnection = (): void => {
  connecting.value = true
  setTimeout((): void => {
    isConnectionEstablished.value = true
    connecting.value = false
  }, 2000)
}

const availableHosts = [
  {
    title: 'Host1',
    value: '192.168.0.1',
  },
  {
    title: 'Host2',
    value: '192.168.0.2',
  }
]

const selectedHost = ref<string | null>(null)
</script>

<template>
  <v-card class="w-100 h-100 bg-color3 d-flex justify-center flex-column rounded-0 overflow-auto custom-scrollbar" flat>
    <v-card-text class="d-flex flex-column align-center text-color2">
      <span class="card__header">
       Установка соединения с linux
      </span>
      <div class="d-flex mx-auto card__selector">
        <v-select :items="availableHosts" v-model="selectedHost" @update:model-value="isConnectionEstablished = false"></v-select>
      </div>
      <v-btn :active="!!selectedHost" color="color2" width="300" flat variant="tonal" @click="handleSetConnection">
        Установить соединение
      </v-btn>
      <span class="card__text text-success" v-if="isConnectionEstablished">
        Соединение установлено
      </span>
    </v-card-text>
  </v-card>
  <overlay-loader :loading="connecting" />
</template>

<style scoped lang="scss">
.card {
  &__header {
    font-size: 25px;
    margin-bottom: 60px;
    margin-top: 60px;
  }
  &__selector {
    width: 200px;
  }
}
</style>