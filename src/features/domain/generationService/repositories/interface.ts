import { GenerationRequest, GenerationResponse, IllustratorResponse } from '../models/generationModel'

export interface GenerateRepository {
  generate: (source: GenerationRequest) => Promise<GenerationResponse>
  getIllustration: (source: GenerationRequest) => Promise<IllustratorResponse>
}
