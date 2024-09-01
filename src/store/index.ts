import { InjectionKey } from 'vue'
import { createStore, GetterTree, Store } from 'vuex'

export interface ChatMessage {
  type: 'incoming' | 'outcoming'
  content: string
  voiceover?: string
  illustration?: string
}
export interface State {
  transcription: string,
  transcriptionError: any,
  chat: ChatMessage[],
  chatId: string
}

export const key: InjectionKey<Store<State>> = Symbol('')

export interface Getters extends GetterTree<State, State> {
  transcription(state: State): string
  chat(state: State): ChatMessage[]
  chatId(state: State): string
  transcriptionError(state: State): any
}

const getters: Getters = {
  transcription (state) {
    return state.transcription
  },
  chat (state) {
    return state.chat
  },
  chatId (state) {
    return state.chatId
  },
  transcriptionError (state) {
    return state.transcriptionError
  },
}

export const store = createStore<State>({
  state: {
    transcription: '',
    transcriptionError: '',
    chat: [],
    chatId: '',
  },
  getters,
  mutations: {
    set (state: State, payload: string) {
      state.transcription = payload
    },
    ADD_MESSAGE (state: State, payload: ChatMessage) {
      state.chat.push(payload)
    },
    SET_CHAT_ID (state: State, payload: string) {
      state.chatId = payload
    },
    SET_T_ERROR (state: State, payload: any) {
      state.transcriptionError = payload
    },
  },
  actions: {
    replace ({ commit }, payload: string) {
      commit('set', payload)
    },
    addMessage ({ commit }, msg: ChatMessage) {
      commit('ADD_MESSAGE', msg)
    },
    setChatId ({ commit }, chatId: string) {
      commit('SET_CHAT_ID', chatId)
    },
    transcriptionError ({ commit }, error: any) {
      commit('SET_T_ERROR', error)
    },
  },
})
