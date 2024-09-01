<!-- eslint-disable vuejs-accessibility/mouse-events-have-key-events -->
<template>
  <a-layout>
    <sidebar />
    <a-layout>
      <Header />
      <a-layout-content :style="contentStyle">
        <Chat />
      </a-layout-content>
    </a-layout>
  </a-layout>
</template>

<script setup lang="ts">
import type { CSSProperties } from 'vue'
import Sidebar from '@/components/layout/Sidebar.vue'
import Header from '@/components/layout/Header.vue'
import Chat from '@/components/chat/Chat.vue'

const contentStyle: CSSProperties = {
  textAlign: 'center',
  minHeight: 120,
  lineHeight: '120px',
  color: '#000',
  backgroundColor: '#F5F5F5',
  paddingLeft: '100px',
}
</script>

<style scoped lang="scss">
::v-deep .ant-layout-sider {
  position: absolute;
  height: 100%;
  max-width: unset!important;
  min-width: 112px!important;
  width: 112px!important;
  padding: 32px 22px;
  background: linear-gradient(180deg, rgba(255,221,45,1) 0%, rgba(255,241,171,1) 100%);
  z-index: 20;
  overflow: hidden;

  &:hover {
    width: 380px!important;
  }
}
</style>
