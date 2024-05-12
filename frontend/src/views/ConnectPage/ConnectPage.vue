<script setup lang="ts">
import {onMounted, ref} from "vue";
import OverlayLoader from "../../components/OverlayLoader.vue";
import useVMs from "../../api/vms.ts";
import useApp from "../../store/app.ts";
const { getVMs } = useVMs()
const { currentHost } = useApp()
const isConnectionEstablished = ref<boolean>(false)
const connecting = ref<boolean>(false)
const handleSetConnection = (): void => {
  connecting.value = true
  setTimeout((): void => {
    isConnectionEstablished.value = true
    connecting.value = false
    console.log(currentHost.value)
  }, 2000)
}

const availableHosts = ref<typeof currentHost.value[]>([])
const selectedHost = ref<string | null>(null)
onMounted(async () => {
  availableHosts.value = await getVMs()
  // console.log(availableHosts.value)
})
</script>

<template>
  <v-card class="w-100 h-100 bg-color3 d-flex justify-center flex-column rounded-0 overflow-auto custom-scrollbar" flat>
    <v-card-text class="d-flex flex-column align-center text-color2">
      <span class="card__header">
       Установка соединения с linux
      </span>
      <div class="d-flex mx-auto card__selector">
        <v-select :items="availableHosts" item-title="name" item-value="ip_address" v-model="currentHost" return-object @update:model-value="isConnectionEstablished = false"></v-select>
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