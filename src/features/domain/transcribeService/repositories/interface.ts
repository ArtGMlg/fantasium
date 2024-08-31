export interface TranscribeRepository {
  transcribe: (source: Blob) => Promise<string>
}
