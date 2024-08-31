import ajaxService from '@/init'

import TranscribeApiRepository from '@/features/domain/transcribeService/repositories/api'
import TranscribeService from '@/features/domain/transcribeService/service'

import GenerateApiRepository from '@/features/domain/generationService/repositories/api'
import GenerateService from '@/features/domain/generationService/service'

const transcribeService = new TranscribeService({
  repository: new TranscribeApiRepository({
    ajaxService,
  }),
})

const generateService = new GenerateService({
  repository: new GenerateApiRepository({
    ajaxService,
  }),
})

export {
  transcribeService,
  generateService,
}
