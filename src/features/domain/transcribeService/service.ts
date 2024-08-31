import { TranscribeRepository } from './repositories/interface'

export default class TranscribeService {
  private repository: TranscribeRepository

  constructor ({ repository }: {
    repository: TranscribeRepository,
  }) {
    this.repository = repository
  }

  public transcribe (source: Blob) {
    return this.repository.transcribe(source)
  }
}
