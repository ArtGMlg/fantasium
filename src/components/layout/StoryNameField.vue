<!-- eslint-disable vuejs-accessibility/click-events-have-key-events -->
<template>
  <div>
    <div
      v-if="!editing"
      class="hover:underline flex items-center cursor-pointer"
      @click="editing = true"
      style="font-size: 24px;"
    >
      Сказка: {{ value }}
      <EditOutlined class="ml-1" />
    </div>
    <div v-else>
      <a-input @blur="editing = false" :value="value"></a-input>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { EditOutlined } from '@ant-design/icons-vue'

defineProps<{
  value: string
}>()

const editing = ref<boolean>(false)
</script>

<style scoped>

</style>
