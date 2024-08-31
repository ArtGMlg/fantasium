<!-- eslint-disable vuejs-accessibility/mouse-events-have-key-events -->
<template>
  <a-layout-sider
    @mouseenter="setHovered(true)"
    @mouseleave="setHovered(false)"
  >
    <sider-button text="Мои сказки" :icon-path="bookSrc" :sider-hovered="hovered" />
    <sider-button text="Написать сказку" :icon-path="createSrc" :sider-hovered="hovered" />
    <sider-button text="Настройки" :icon-path="coggSrc" :sider-hovered="hovered" />
  </a-layout-sider>
</template>

<script setup lang="ts">
import { ref, CSSProperties } from 'vue'
import bookSrc from '@/assets/icons/book.svg'
import createSrc from '@/assets/icons/create.svg'
import coggSrc from '@/assets/icons/cogg.svg'
import SiderButton from './SiderButton.vue'

const hovered = ref<boolean>(false)

const setHovered = (state: boolean) => {
  if (state) {
    setTimeout(() => {
      hovered.value = true
    }, 200)
  } else {
    hovered.value = false
  }
}
</script>

<style scoped lang="scss">
</style>
