<!-- eslint-disable vuejs-accessibility/mouse-events-have-key-events -->
<template>
  <a-layout-sider>
    <sider-button text="Мои сказки" :icon-path="bookSrc" to="/archive" />
    <sider-button text="Написать сказку" :icon-path="createSrc" to="/app" />
    <sider-button text="Настройки" :icon-path="coggSrc" to="/settings" />
  </a-layout-sider>
</template>

<script setup lang="ts">
import bookSrc from '@/assets/icons/book.svg'
import createSrc from '@/assets/icons/create.svg'
import coggSrc from '@/assets/icons/cogg.svg'
import SiderButton from './SiderButton.vue'
</script>

<style scoped lang="scss">
</style>
