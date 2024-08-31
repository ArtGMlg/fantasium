import { GenerationRequest, GenerationResponse } from '../models/generationModel'

export interface GenerateRepository {
  generate: (source: GenerationRequest) => Promise<GenerationResponse>
}
