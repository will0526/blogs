# axios 中设置拦截器

## 实现功能
在请求中设置请求发送时间，在返回中检查响应时间

```markdown

import axios from 'axios'
import {NativeModules} from 'react-native'

class FrontAs{
    isInit = false;
    appName = "";
    //给请求加拦截，用于计算接口耗时
    init(appName){
        if(this.isInit === true){
            return;
        }
        this.appName = appName;

        this.isInit = true;
        axios.interceptors.request.use(
            config => {
                return this._interceptRequest(config)
            },
            error => {
                return Promise.reject(error)
            }
        );

        axios.interceptors.response.use(
            response => {
                return this._interceptResponse(response);
            },
            error => {
                return Promise.reject(error)
            }
        );
    }

    _interceptRequest(config){
        try{
            config.FrontAs = Date.now();
            console.log("axios.config==>",JSON.stringify(config));
        }catch (e) {
            console.log("axios.interceptRequest==>"+e.toString());
        }
        return config
    }

    _interceptResponse(response){
        try{
            let consumeTime = Date.now() - response.config.FrontAs;
            console.log(`${response.config.url}` + '=====axios=======接口耗时>>>>>>>' + consumeTime);
            console.log("axios.response==>"+response.status);
            
        }catch (e) {
            console.log("axios.interceptResponse==>"+e.toString());
        }
        return response
    }

}
const instance = new FrontAs();
export default instance

```






