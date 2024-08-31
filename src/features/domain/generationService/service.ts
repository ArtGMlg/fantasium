import { GenerationRequest } from './models/generationModel'
import { GenerateRepository } from './repositories/interface'

export default class GenerateService {
  private repository: GenerateRepository

  constructor ({ repository }: {
    repository: GenerateRepository,
  }) {
    this.repository = repository
  }

  public generate (source: GenerationRequest) {
    return this.repository.generate(source)
  }
}
