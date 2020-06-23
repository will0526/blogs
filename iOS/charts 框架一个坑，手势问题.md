iOS开发图表时使用第三方charts 框架遇到的一个坑。
由于把图表的view当做一个子view放在一个controller里面
图表里面会有tap，pinch，pan和touch等各种手势交互。因此会影响其父view的手势交互，比如本项目，手势落在图表内上下滑动，页面并不会滚动。左右滑动图表内容会做出相应改变。因此分析上下滑动手势是好的，只是被图表的view接受处理了。

于是，处理方向就变成了。让图表对上下滑动手势不处理，直接让其上传到父view。
一个思路，利用
-( UIView *)hitTest:(CGPoint)point withEvent:(UIEvent *)event 
这个方法重写去过滤。
结果是作用起了，其他手势图表也不处理了。
想要达到隔绝父视图或者子视图的手势处理，可以参见。
http://blog.csdn.net/itianyi/article/details/50550099

于是，就快要放弃的时候，决定看下charts的源码，看看框架对于这个手势是怎么处理的。
于是就在源码里找到了一句话
![image.png](http://upload-images.jianshu.io/upload_images/2728934-9976cebd8348b1d4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

注释掉就可以了。
父视图也能处理手势。
所以，没事多看源码。

