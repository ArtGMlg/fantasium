<!-- eslint-disable max-len -->
<template>
  <div class="w-container">
    <div class="image-container">
      <img src="@/assets/img/kandinsky-download-17250087932291.png" alt="Image">
    </div>
    <div class="text-container">
      <h2>Фантазиум — инструмент для развития фантазии ваших детей</h2>
      <p>Ребёнок сможет создавать сказки в формате диалога с искусственным интеллектом</p>
    </div>
  </div>
  <div class="footer">
    Процесс общения с нейросетью безопасен для ребёнка
    <button @click="redirect" class="button">Начать →</button>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()

const redirect = () => {
  router.push('/app')
}
</script>

<style scoped>
.w-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
}

.image-container {
  width: 40%;
}

.image-container img {
  width: 100%;
}

.text-container {
  width: 55%;
  text-align: start;
}

.text-container h2 {
  font-size: 24px;
  margin-bottom: 10px;
}

.text-container p {
  font-size: 16px;
  margin-bottom: 10px;
}

.button {
  background-color: #FFD700;
  color: #000;
  padding: 10px 20px;
  border: none;
  border-radius: 25px;
  font-size: 20px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  box-shadow: 0px 0px 15px 0px rgba(34, 60, 80, 0.2);
}

.button:hover {
  background-color: #FFC107;
}

.footer {
  font-size: 12px;
  margin-top: 20px;
  color: #666;
  position: absolute;
  width: 100%;
  bottom: 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 48px;
}
</style>
