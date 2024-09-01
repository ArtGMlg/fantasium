<!-- eslint-disable vuejs-accessibility/click-events-have-key-events -->
<template>
  <div class="flex items-center justify-center h-full" style="background-color: #F5F5F5;">
    <div class="card">
      <span>Функция находится в разработке</span>
      <div class="ico-holder mt-3">
        <img :src="devSrc" alt="dev">
      </div>
      <div
        class="back hover:cursor-pointer"
        @click="goBack"
      >
        <i class="pi pi-arrow-left"></i>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import devSrc from '@/assets/icons/dev.svg'
import { useRouter } from 'vue-router'

const router = useRouter()

const goBack = () => {
  router.back()
}

</script>

<style scoped>
.card {
  width: 40%;
  display: flex;
  flex-direction: column;
  align-items: center;
  border-radius: 22px;
  padding: 20px;
  box-shadow: 0px 0px 15px 0px rgba(34, 60, 80, 0.2);
  position: relative;
}

.back {
  width: 36px;
  height: 36px;
  border-radius: 18px;
  display: flex;
  align-items: center;
  justify-content: center;
  position: absolute;
  background-color: #fff;
  top: -10px;
  left: -10px;
  box-shadow: 0px 0px 15px 0px rgba(34, 60, 80, 0.2);
}

.ico-holder {
  background-color: #FFDD2D;
  border-radius: 80px;
  width: 160px;
  height: 160px;
  display: flex;
  align-items: center;
  justify-content: center;
}

</style>
