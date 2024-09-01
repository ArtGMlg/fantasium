/* eslint-disable max-len */
import AjaxService from '@/features/core/ajax/service'
import { GenerateRepository } from './interface'
import { GenerationRequest, GenerationResponse, IllustratorResponse } from '../models/generationModel'
import { exportGeneration } from './converters'

export default class GenerateApiRepository implements GenerateRepository {
  private ajaxService: AjaxService

  private baseUrl = '/generate_complete'

  constructor ({ ajaxService }: {
    ajaxService: AjaxService
  }) {
    this.ajaxService = ajaxService
  }

  public generate: (source: GenerationRequest) => Promise<GenerationResponse> = (source: GenerationRequest) => this.ajaxService.post({
    url: this.baseUrl,
    data: exportGeneration(source),
  })
    .then((res) => res)

  public getIllustration: (source: GenerationRequest) => Promise<IllustratorResponse> = (source) => this.ajaxService.post({
    url: '/illustrator',
    data: exportGeneration(source),
  })
    .then((res) => res)
}
