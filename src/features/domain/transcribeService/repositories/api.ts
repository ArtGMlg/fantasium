import AjaxService from '@/features/core/ajax/service'
import { TranscribeRepository } from './interface'

export default class TranscribeApiRepository implements TranscribeRepository {
  private ajaxService: AjaxService

  private baseUrl = '/transcribe'

  constructor ({ ajaxService }: {
    ajaxService: AjaxService
  }) {
    this.ajaxService = ajaxService
  }

  public transcribe: (source: Blob) => Promise<string> = (source: Blob) => {
    const formData = new FormData()
    formData.append('file', source, 'recording.wav')

    return this.ajaxService.post({
      url: this.baseUrl,
      data: formData,
      config: {
        headers: {
          'content-type': 'multipart/form-data',
        },
      },
    })
      .then((res) => res.transcription)
  }
}
