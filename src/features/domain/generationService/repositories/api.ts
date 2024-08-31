import AjaxService from '@/features/core/ajax/service'
import { GenerateRepository } from './interface'
import { GenerationRequest, GenerationResponse } from '../models/generationModel'

export default class GenerateApiRepository implements GenerateRepository {
  private ajaxService: AjaxService

  private baseUrl = '/generate_story'

  constructor ({ ajaxService }: {
    ajaxService: AjaxService
  }) {
    this.ajaxService = ajaxService
  }

  // eslint-disable-next-line max-len
  public generate: (source: GenerationRequest) => Promise<GenerationResponse> = (source: GenerationRequest) => this.ajaxService.post({
    url: this.baseUrl,
    data: source,
  })
    .then((res) => res)
}
