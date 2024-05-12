<script setup lang="ts">
import {computed, ref, watch} from "vue";
import useApp from "../../store/app.ts";
import axios from "axios";
import OverlayLoader from "../../components/OverlayLoader.vue";
const { currentHost } = useApp()
const scripts = computed(() => currentHost.value?.scripts)

const loadMore = ref<HTMLElement | null>(null)
const observer = ref<IntersectionObserver | null>(null)
const isFulfilled = ref<boolean>(true)
const scriptIsLoading = ref<boolean>(false)
watch(
    () => loadMore.value,
    () => {
      onObserverUpdate()
    },
)

const onObserverUpdate = (): void => {
  if (!isFulfilled.value && loadMore.value) {
    observer.value = new IntersectionObserver(([entry]) => {
      if (entry && entry.isIntersecting) {
        loadMoreScripts()
      }
    }, {})
    observer.value.observe(loadMore.value)
  }
}

const loadMoreScripts = (): void => {
  setTimeout(() => {
    // scripts.value = [...scripts.value, ...scripts.value.splice(0, 5)]
  }, 1000)
}

const executeScript = async (script, key) => {
  scriptIsLoading.value = true
  const resp = await axios.post(`http://localhost:8000/vms/${currentHost.value?.id}/execute_script/`, {
    script: script.id
  })
  scriptIsLoading.value = false
  alert(`script #${key}, message: ${resp.data.output}`)
}

const executeAllScripts = async () => {
  // await Promise.all(currentHost.value?.scripts.map(async (v, k) => executeScript(v, k)))
  currentHost.value?.scripts.forEach((v, k) => {
    executeScript(v, k)
  })
}

</script>

<template>
  <v-card class="w-100 h-100 bg-color3 d-flex flex-column rounded-0 overflow-auto custom-scrollbar pa-4 pb-0" flat>
    <v-btn class="ml-auto" height="50" color="color2" flat variant="tonal" @click="executeAllScripts">Активировать все</v-btn>
    <div class="d-flex flex-column text-color1 border-b" v-for="(script, key) in scripts" :key="key">
      <v-card-title>
        {{script.name}}
      </v-card-title>
      <v-card-text>
        {{script.description}}
      </v-card-text>
      <v-card-actions>
        <v-spacer/>
        <v-btn @click="executeScript(script, key)">
          Активировать
        </v-btn>
      </v-card-actions>
    </div>
    <div v-if="!isFulfilled" class="d-flex w-100 text-color1" ref="loadMore">
      <v-progress-circular size="30" class="ma-auto my-3" indeterminate />
    </div>
  </v-card>
  <overlay-loader :loading="scriptIsLoading"></overlay-loader>
</template>

<style scoped lang="scss">
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