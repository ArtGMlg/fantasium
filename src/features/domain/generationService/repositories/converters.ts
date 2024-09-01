import { ChatMessage } from '@/store'
import { GenerationRequest, GenerationResponse, IllustratorResponse } from '../models/generationModel'

export interface OuterGeneration {
  story: string
  transcription: string
}

export interface Req {
  // eslint-disable-next-line camelcase
  chat_id: string
  message: string
}

export const importGeneration = (value: GenerationResponse): ChatMessage => ({
  type: 'incoming',
  content: value.story,
  voiceover: value.transcription,
})

export const exportGeneration = (value: GenerationRequest): Req => ({
  chat_id: value.chatId,
  message: value.message,
})

export const importIllustration = (value: IllustratorResponse): IllustratorResponse => ({
  image: value.image,
})
