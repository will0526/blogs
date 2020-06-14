#前端页面性能优化

##一、网络加载类


1．首屏数据请求提前，避免JavaScript文件加载后才请求数据

2．首屏加载和按需加载，非首屏内容滚屏加载，保证首屏内容最小化
一般推荐移动端页面首屏数据展示延时最长不超过3秒。目前中国联通3G的网络速度为338KB/s（2.71Mb/s），所以推荐首屏所有资源大小不超过1014KB，即大约不超过1MB。

3．模块化资源并行下载
在移动端资源加载中，尽量保证JavaScript资源并行加载，主要指的是模块化JavaScript资源的异步加载，例如AMD的异步模块，使用并行的加载方式能够缩短多个文件资源的加载时间。

4．inline首屏必备的CSS和JavaScript
通常为了在HTML加载完成时能使浏览器中有基本的样式，需要将页面渲染时必备的CSS和JavaScript通过`<script>`或`<style>`内联到页面中，避免页面HTML载入完成到页面内容展示这段过程中页面出现空白

5．meta dns prefetch设置DNS预解析
设置文件资源的DNS预解析，让浏览器提前解析获取静态资源的主机IP，避免等到请求时才发起DNS解析请求。通常在移动端HTML中可以采用如下方式完成。
```
<!-- cdn域名预解析 -->
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.domain.com">
```
6．资源预加载
对于移动端首屏加载后可能会被使用的资源，需要在首屏完成加载后尽快进行加载，保证在用户需要浏览时已经加载完成，这时候如果再去异步请求就显得很慢。

7．合理利用MTU策略
通常情况下，我们认为TCP网络传输的最大传输单元（Maximum Transmission Unit，MTU）为1500B，即网络一个RTT（Round-Trip Time，网络请求往返时间）时间内可以传输的数据量最大为1500字节。因此，在前后端分离的开发模式中，尽量保证页面的HTML内容在1KB以内，这样整个HTML的内容请求就可以在一个RTT时间内请求完成，最大限度地提高HTML载入速度。


##二、缓存类


1．合理利用浏览器缓存

除了上面说到的使用Cache-Control、Expires、Etag和Last-Modified来设置HTTP缓存外，在移动端还可以使用localStorage等来保存AJAX返回的数据，或者使用localStorage保存CSS或JavaScript静态资源内容，实现移动端的离线应用，尽可能减少网络请求，保证静态资源内容的快速加载。

2．静态资源离线方案
对于移动端或Hybrid应用，可以设置离线文件或离线包机制让静态资源请求从本地读取，加快资源载入速度，并实现离线更新。
3．尝试使用AMP HTML
AMP HTML可以作为优化前端页面性能的一个解决方案，使用AMP Component中的元素来代替原始的页面元素进行直接渲染。

<amp-video width="400" height="300" src="http://www.domain.com/videos/myvideo.mp4" poster= "path/poster.jpg">
<div fallback>

##三、图片类

1．图片压缩处理

2．使用较小的图片，合理使用base64内嵌图片

3．使用更高压缩比格式的图片
使用具有较高压缩比格式的图片，如webp等。

4．图片懒加载

5．使用Media Query或srcset根据不同屏幕加载不同大小图片
在介绍响应式的章节中我们了解到，针对不同的移动端屏幕尺寸和分辨率，输出不同大小的图片或背景图能保证在用户体验不降低的前提下节省网络流量，加快部分机型的图片加载速度，这在移动端非常值得推荐。

6．使用iconfont代替图片图标

7．定义图片大小限制
加载的单张图片一般建议不超过30KB

##四、脚本类

1．尽量使用id选择器
选择页面DOM元素时尽量使用id选择器，因为id选择器速度最快。

2．合理缓存DOM对象
对于需要重复使用的DOM对象，要优先设置缓存变量，避免每次使用时都要从整个DOM树中重新查找。

```
// 不推荐
$('#mod .active').remove('active');
$('#mod .not-active').addClass('active');

// 推荐
let $mod = $('#mod');
$mod.find('.active').remove('active');
$mod.find('.not-active').addClass('active');
```

3．页面元素尽量使用事件代理，避免直接事件绑定
使用事件代理可以避免对每个元素都进行绑定，并且可以避免出现内存泄露及需要动态添加元素的事件绑定问题，所以尽量不要直接使用事件绑定。

```
// 不推荐
$('.btn').on('click', function(e){
    console.log(this)；
});
// 推荐
$('body').on('click', '.btn', function(e){
    console.log(this);
});
```

4．使用touchstart代替click
由于移动端屏幕的设计，touchstart事件和click事件触发时间之间存在300毫秒的延时，所以在页面中没有实现touchmove滚动处理的情况下，可以使用touchstart事件来代替元素的click事件，加快页面点击的响应速度，提高用户体验。但同时我们也要注意页面重叠元素touch动作的点击穿透问题。
// 不推荐
$('body').on('click', '.btn', function(e){
    console.log(this);
});
// 推荐
$('body').on('touchstart', '.btn', function(e){
    console.log(this);
});

5．避免touchmove、scroll连续事件处理
需要对touchmove、scroll这类可能连续触发回调的事件设置事件节流，例如设置每隔16ms（60帧的帧间隔为16.7ms，因此可以合理地设置为16ms）才进行一次事件处理，避免频繁的事件调用导致移动端页面卡顿。

// 不推荐
$('.scroller').on('touchmove', '.btn', function(e){
    console.log(this);
});
// 推荐
$('.scroller').on('touchmove', '.btn', function(e){
    let self = this;
    setTimeout(function(){
        console.log(self);
    }, 16);
});

6．避免使用eval、with，使用join代替连接符+，推荐使用ECMAScript 6的字符串模板。这些都是一些基础的安全脚本编写问题，尽可能使用较高效率的特性来完成这些操作，避免不规范或不安全的写法。

7．尽量使用ECMAScript 6+的特性来编程
ECMAScript 6+一定程度上更加安全高效，而且部分特性执行速度更快，也是未来规范的需要，所以推荐使用ECMAScript 6+的新特性来完成后面的开发。

##五、渲染类

1．使用Viewport固定屏幕渲染，可以加速页面渲染内容

一般认为，在移动端设置Viewport可以加速页面的渲染，同时可以避免缩放导致页面重排重绘。在移动端固定Viewport设置的方法如下。
<!-- 设置viewport不缩放 -->
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">

2．避免各种形式重排重绘

页面的重排重绘很耗性能，所以一定要尽可能减少页面的重排重绘，例如页面图片大小变化、元素位置变化等这些情况都会导致重排重绘。

3．使用CSS3动画，开启GPU加速

使用CSS3动画时可以设置transform: translateZ(0)来开启移动设备浏览器的GPU图形处理加速，让动画过程更加流畅。
-webkit-transform: translateZ(0);
-ms-transform: translateZ(0);
-o-transform: translateZ(0);
transform: translateZ(0);

4．合理使用Canvas和requestAnimationFrame

选择Canvas或requestAnimationFrame等更高效的动画实现方式，尽量避免使用setTimeout、setInterval等方式来直接处理连续动画。

5．SVG代替图片

部分情况下可以考虑使用SVG代替图片实现动画，因为使用SVG格式内容更小，而且SVG DOM结构方便调整。

6．不滥用float

在DOM渲染树生成后的布局渲染阶段，使用float的元素布局计算比较耗性能，所以尽量减少float的使用，推荐使用固定布局或flex-box弹性布局的方式来实现页面元素布局。
7．不滥用web字体或过多font-size声明

过多的font-size声明会增加字体的大小计算，而且也没有必要的。

##六、架构协议类

1．尝试使用SPDY和HTTP 

在条件允许的情况下可以考虑使用SPDY协议来进行文件资源传输，利用连接复用加快传输过程，缩短资源加载时间。HTTP 2在未来也是可以考虑尝试的。

2．使用后端数据渲染

使用后端数据渲染的方式可以加快页面内容的渲染展示，避免空白页面的出现，同时可以解决移动端页面SEO的问题。如果条件允许，后端数据渲染是一个很不错的实践思路。后面的章节会详细介绍后端数据渲染的相关内容。

3．使用Native View代替DOM的性能劣势

可以尝试使用Native View的MNV开发模式来避免HTML DOM性能慢的问题，目前使用MNV的开发模式已经可以将页面内容渲染体验做到接近客户端Native应用的体验了。

本文摘自书籍《现代前端技术解析》。