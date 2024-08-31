import axios, { AxiosInstance, AxiosRequestConfig } from 'axios'

interface Request<T = any> {
  url: string
  data?: T
  config?: AxiosRequestConfig
}

interface GetRequest<T = any> {
  url: string
  config?: AxiosRequestConfig
}

export default class AjaxService {
  private axios: AxiosInstance

  constructor (
    baseUrl: string,
  ) {
    this.axios = axios.create({
      baseURL: baseUrl,
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
      },
    })
  }

  public async post ({ url, data, config }: Request) {
    return (await this.axios.post(url, data, config)).data
  }

  public async get ({ url, config }: GetRequest) {
    return (await this.axios.get(url, config)).data
  }
}
