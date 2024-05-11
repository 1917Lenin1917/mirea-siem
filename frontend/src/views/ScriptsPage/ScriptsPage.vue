<script setup lang="ts">
import {ref, watch} from "vue";

const scripts = ref([
    {
        title: 'Test title',
        description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque fringilla, nibh id elementum lobortis, metus sapien scelerisque dolor, vitae lacinia ante metus nec ipsum. Morbi interdum sollicitudin purus sed aliquet. Ut mollis lobortis dui eget scelerisque. Donec vel massa et dui lacinia gravida. Cras at quam dolor. Maecenas sit amet sapien ut justo ultricies semper at quis diam. Pellentesque euismod sodales lorem, in facilisis lorem varius eget. Aenean vehicula egestas ligula id sagittis. Sed pharetra, turpis ac dapibus facilisis, nisi justo consequat orci, at faucibus sapien turpis non dui. Praesent ultrices faucibus justo et posuere.\n' +
        '\n' +
        'Fusce in sapien velit. Integer efficitur tempor massa et varius. Aliquam posuere ante nec quam porttitor rhoncus. Quisque eget nunc nec erat ullamcorper condimentum at non arcu. Suspendisse ac metus vitae massa facilisis auctor. Donec venenatis tempus nisl sit amet elementum. Vivamus mollis porta arcu euismod laoreet. In in dapibus quam. Nam suscipit nisi quis dolor semper, sit amet sollicitudin turpis pellentesque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin ullamcorper maximus sapien, eget malesuada turpis egestas vitae. Vivamus dignissim in sem eu pharetra. Vivamus at sagittis nunc. Quisque blandit est id erat pharetra, ut elementum arcu tempor. Duis iaculis vehicula augue eget mollis. Pellentesque accumsan vulputate est et viverra.'
    },{
        title: 'Test title',
        description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque fringilla, nibh id elementum lobortis, metus sapien scelerisque dolor, vitae lacinia ante metus nec ipsum. Morbi interdum sollicitudin purus sed aliquet. Ut mollis lobortis dui eget scelerisque. Donec vel massa et dui lacinia gravida. Cras at quam dolor. Maecenas sit amet sapien ut justo ultricies semper at quis diam. Pellentesque euismod sodales lorem, in facilisis lorem varius eget. Aenean vehicula egestas ligula id sagittis. Sed pharetra, turpis ac dapibus facilisis, nisi justo consequat orci, at faucibus sapien turpis non dui. Praesent ultrices faucibus justo et posuere.\n' +
        '\n' +
        'Fusce in sapien velit. Integer efficitur tempor massa et varius. Aliquam posuere ante nec quam porttitor rhoncus. Quisque eget nunc nec erat ullamcorper condimentum at non arcu. Suspendisse ac metus vitae massa facilisis auctor. Donec venenatis tempus nisl sit amet elementum. Vivamus mollis porta arcu euismod laoreet. In in dapibus quam. Nam suscipit nisi quis dolor semper, sit amet sollicitudin turpis pellentesque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin ullamcorper maximus sapien, eget malesuada turpis egestas vitae. Vivamus dignissim in sem eu pharetra. Vivamus at sagittis nunc. Quisque blandit est id erat pharetra, ut elementum arcu tempor. Duis iaculis vehicula augue eget mollis. Pellentesque accumsan vulputate est et viverra.'
    },{
        title: 'Test title',
        description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque fringilla, nibh id elementum lobortis, metus sapien scelerisque dolor, vitae lacinia ante metus nec ipsum. Morbi interdum sollicitudin purus sed aliquet. Ut mollis lobortis dui eget scelerisque. Donec vel massa et dui lacinia gravida. Cras at quam dolor. Maecenas sit amet sapien ut justo ultricies semper at quis diam. Pellentesque euismod sodales lorem, in facilisis lorem varius eget. Aenean vehicula egestas ligula id sagittis. Sed pharetra, turpis ac dapibus facilisis, nisi justo consequat orci, at faucibus sapien turpis non dui. Praesent ultrices faucibus justo et posuere.\n' +
        '\n' +
        'Fusce in sapien velit. Integer efficitur tempor massa et varius. Aliquam posuere ante nec quam porttitor rhoncus. Quisque eget nunc nec erat ullamcorper condimentum at non arcu. Suspendisse ac metus vitae massa facilisis auctor. Donec venenatis tempus nisl sit amet elementum. Vivamus mollis porta arcu euismod laoreet. In in dapibus quam. Nam suscipit nisi quis dolor semper, sit amet sollicitudin turpis pellentesque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin ullamcorper maximus sapien, eget malesuada turpis egestas vitae. Vivamus dignissim in sem eu pharetra. Vivamus at sagittis nunc. Quisque blandit est id erat pharetra, ut elementum arcu tempor. Duis iaculis vehicula augue eget mollis. Pellentesque accumsan vulputate est et viverra.'
    },{
        title: 'Test title',
        description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque fringilla, nibh id elementum lobortis, metus sapien scelerisque dolor, vitae lacinia ante metus nec ipsum. Morbi interdum sollicitudin purus sed aliquet. Ut mollis lobortis dui eget scelerisque. Donec vel massa et dui lacinia gravida. Cras at quam dolor. Maecenas sit amet sapien ut justo ultricies semper at quis diam. Pellentesque euismod sodales lorem, in facilisis lorem varius eget. Aenean vehicula egestas ligula id sagittis. Sed pharetra, turpis ac dapibus facilisis, nisi justo consequat orci, at faucibus sapien turpis non dui. Praesent ultrices faucibus justo et posuere.\n' +
        '\n' +
        'Fusce in sapien velit. Integer efficitur tempor massa et varius. Aliquam posuere ante nec quam porttitor rhoncus. Quisque eget nunc nec erat ullamcorper condimentum at non arcu. Suspendisse ac metus vitae massa facilisis auctor. Donec venenatis tempus nisl sit amet elementum. Vivamus mollis porta arcu euismod laoreet. In in dapibus quam. Nam suscipit nisi quis dolor semper, sit amet sollicitudin turpis pellentesque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin ullamcorper maximus sapien, eget malesuada turpis egestas vitae. Vivamus dignissim in sem eu pharetra. Vivamus at sagittis nunc. Quisque blandit est id erat pharetra, ut elementum arcu tempor. Duis iaculis vehicula augue eget mollis. Pellentesque accumsan vulputate est et viverra.'
    },
]
)
const loadMore = ref<HTMLElement | null>(null)
const observer = ref<IntersectionObserver | null>(null)
const isFulfilled = ref<boolean>(false)

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
    scripts.value = [...scripts.value, ...scripts.value.splice(0, 5)]
  }, 1000)
}
</script>

<template>
  <v-card class="w-100 h-100 bg-color3 d-flex flex-column rounded-0 overflow-auto custom-scrollbar pa-4 pb-0" flat>
    <div class="d-flex flex-column text-color1 border-b" v-for="(script, key) in scripts" :key="key">
      <v-card-title>
        {{script.title}}
      </v-card-title>
      <v-card-text>
        {{script.description}}
      </v-card-text>
      <v-card-actions>
        <v-spacer/>
        <v-btn>
          Активировать
        </v-btn>
      </v-card-actions>
    </div>
    <div class="d-flex w-100 text-color1" ref="loadMore">
      <v-progress-circular size="30" class="ma-auto my-3" indeterminate />
    </div>
  </v-card>
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