import { transcribeService } from '@/init/services'
import { store } from '@/store'

// Проверяем, поддерживает ли браузер необходимые API
if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
  console.error('getUserMedia не поддерживается в этом браузере')
}

let mediaRecorder: MediaRecorder
let audioChunks: Blob[] = []
let audioBlob: Blob

const startRecording = async () => {
  try {
    // Запрашиваем доступ к микрофону
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true })

    // Инициализируем MediaRecorder
    mediaRecorder = new MediaRecorder(stream)

    // Обрабатываем данные, поступающие с микрофона
    mediaRecorder.ondataavailable = (event: BlobEvent) => {
      audioChunks.push(event.data)
    }

    // Обработка завершения записи
    mediaRecorder.onstop = () => {
      audioBlob = new Blob(audioChunks, { type: 'audio/wav' })

      // Очищаем данные после завершения записи
      transcribeService.transcribe(audioBlob)
        .then((res) => {
          store.dispatch('replace', res)
          audioChunks = []
        })
        .catch((error) => {
          store.dispatch('transcriptionError', error)
        })
    }

    // Начинаем запись
    mediaRecorder.start()
    console.log('Запись началась...')
  } catch (error) {
    console.error('Ошибка при доступе к микрофону:', error)
  }
}

// eslint-disable-next-line consistent-return
const stopRecording = () => {
  if (mediaRecorder && mediaRecorder.state !== 'inactive') {
    console.log('Запись остановлена.')
    mediaRecorder.stop()
  }
}

export { startRecording, stopRecording }

// // Пример использования:
// // Запуск записи
// startRecording()

// // Остановка записи через 5 секунд
// setTimeout(() => {
//   stopRecording()
// }, 5000)
