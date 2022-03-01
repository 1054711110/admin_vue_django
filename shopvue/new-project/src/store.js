import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export default new Vuex.Store({
    //所有的数据都放在state中
    state:{
        arr:'123'
    },

    //操作数据，唯一的通道是mutations
    mutations:{},

    //actions,可以来做异步操作，然后提交给mutations，而后再对state(数据)进行操作
    actions:{}
})