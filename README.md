# swift_build_analysis_tool
## 如何开启编译耗时选项
### 主工程

在 **OTHER_SWIFT_FLAGS** 里面添加 **-Xfrontend -debug-time-function-bodies**
<p class="img-tip" data-str="主工程"><img src="https://sf3-ttcdn-tos.pstatp.com/img/tos-cn-v-0000/607e49a33e86438d8936c94da8ed4bc8~noop.png" height="548" width="1013"/></p>


### Pod
在 podfile 里面添加
```
post_install do |installer|
  installer.pods_project.targets.each do |target|
    target.build_configurations.each do |config|
      config.build_settings['OTHER_SWIFT_FLAGS'] ||= '-Xfrontend -debug-time-function-bodies'
    end
  end
end
```

重新 pod install

## 如何获取编译耗时
### 清除缓存
删除 DerivedData & Clean Build Folder (command+shift+k) 
<br/>

### 重新编译
<br/>

### 获取编译日志
```
open ~/Library/Developer/Xcode/DerivedData
```
<p class="img-tip" data-str="DerivedData"><img src="https://sf3-ttcdn-tos.pstatp.com/img/tos-cn-v-0000/f60a944805c7431799abb5e2fa17a1b0~noop.png" height="478" width="1140"/></p>

找到你刚刚编译的项目(你编译的项目/Logs/Build/XXX.xcactivitylog)
<br/>
### 通过脚本分析数据
下载项目中 build_analysis_tool.py
<br/>
### 使用说明
<p class="img-tip" data-str="使用说明"><img src="https://sf3-ttcdn-tos.pstatp.com/img/tos-cn-v-0000/823e1a9838f645e287d0ad2768dd40f2~noop.png" height="440" width="1140"/></p>

```
python build_analysis_tool.py xxx.xcactivitylog > cost_time.log
```
<br/>

打开 cost_time.log 文件即可查看编译耗时

<p class="img-tip" data-str="编译耗时"><img src="https://sf3-ttcdn-tos.pstatp.com/img/tos-cn-v-0000/aaa53e2787f24aa9987a9ec8c2ccbae8~noop.png" height="668" width="1140"/></p>

其中
- 第一个参数代表编译时候出现的次数
- 第二个参数是编译耗时
- 第三个参数是文件路径以及文件名

## 相关阅读
[ https://github.com/RobertGummesson/BuildTimeAnalyzer-for-Xcode]( https://github.com/RobertGummesson/BuildTimeAnalyzer-for-Xcode)



