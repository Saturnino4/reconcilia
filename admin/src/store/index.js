import { createStore } from 'vuex'
import axios from 'axios'
import { KEY, BASE_URL } from '@/config'

export default createStore({
  state: {
    loggedUser: {},
    permissoes: []
  },
  getters: {

    getPermissao: (state) => state.permissoes,

    getLoggedUser: (state) => state.loggedUser
    
  },

  mutations: {

    setLoggedUser(){
      try {
        this.state.loggedUser =  JSON.parse(localStorage.getItem('userData'))
      } catch (error) {
          console.log(error)
          this.state.loggedUser =  null
      }
    },

    setPermissoes(state, permissoes){
      state.permissoes = permissoes
      console.log('No setar sermissoes',state.permissoes);
      
    }
    
  
  },
  actions: {
     async fethPermissoes (id=null){
      
        if(!id){
          console.log('Id não informado');
          return
          
        }
        

        try {
          
          const res = await axios.get(`${BASE_URL}/permissao/u/${this.state.loggedUser.id}/?key=${KEY}`)
          this.commit('setPermissoes', res.data.data)
          console.log('PermissoesEEEE: ',this.state.permissoes);
          
        } catch (error) {
          console.log('Erro ao pegar permissoes: ',error);
          
        }

     }

  },
  modules: {
  }
})
 