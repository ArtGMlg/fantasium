export interface GenerationRequest {
  chatId: string
  message: string
}

export interface GenerationResponse {
  story: string
  transcription: string
}

export interface IllustratorResponse {
  image: string
}
