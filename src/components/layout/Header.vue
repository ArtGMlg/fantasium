<template>
  <a-layout-header :style="headerStyle">
    <div>
      <story-name-field value="Test"/>
    </div>
    <div class="actions-block">
      <div class="mr-10 cursor-pointer">
        <img :src="saveSrc" alt="save">
      </div>
      <div class="cursor-pointer">
        <download-outlined style="font-size: 38px;" />
      </div>
    </div>
  </a-layout-header>
</template>

<script setup lang="ts">
import type { CSSProperties } from 'vue'
import { DownloadOutlined } from '@ant-design/icons-vue'
import saveSrc from '@/assets/icons/save.svg'
import StoryNameField from './StoryNameField.vue'

const headerStyle: CSSProperties = {
  color: '#000',
  height: 85,
  paddingInline: 0,
  paddingLeft: '60px',
  paddingRight: '35px',
  lineHeight: '85px',
  backgroundColor: '#fff',
  marginLeft: '112px',
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'space-between',
}
</script>

<style scoped lang="scss">
.actions-block {
  display: flex;
  align-items: center;
}
</style>
