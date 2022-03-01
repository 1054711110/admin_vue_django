// 导入封装好的网络请求类工具
import Network from '../http/http';

// 封装各种接口请求
// export const 接口名 = () => Network.get('/路由',参数对象);
export const login = (data) => Network.post('/login/',data);

// 用户列表
export const getuserlist = () => Network.get('/getuserlist/');
// 添加用户列表
export const adduserlist = (data) => Network.post('/adduser/',data);
// 添加用户列表
export const deluser = (data) => Network.post('/deluser/',data);
// 设置用户状态
export const userstate = (data) => Network.post('/userstate/',data);
// 修改用户
export const userupdate = (data) => Network.post('/updateuser/',data);