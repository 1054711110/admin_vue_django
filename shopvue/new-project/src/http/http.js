// 导入axios
import axios from 'axios';



const Server = axios.create({
  baseURL: "http://127.0.0.1:8000/",//根域名
  timeout: 3000,//超时时间
});


//3. 定义请求拦截器
Server.interceptors.request.use((config) => {
  let user = localStorage.getItem('user')
  let token = JSON.parse(user)
  // console.log(token.token)
  if (token != null) {
    // console.log(token.token)
    config.headers.Authorization = 'JWT ' + token.token
  }
  return config;
}, (error) => {


  return Promise.reject(error);
});

//4. 定义相应拦截器
Server.interceptors.response.use((response) => {

  if (response.status == 200) {

    return response.data;
  }
}, (error) => {
  return Promise.reject(error);
});

export default Server;