export interface GenerationRequest {
  chatId: string
  message: string
}

export interface GenerationResponse {
  story: string
  audio: string
  image: string
}
