# Gradient_Colorizing_Fix
A short python code to fix a issue that could cause brightness loss in gradient colorizing.

![image](https://raw.githubusercontent.com/zznewclear13/Gradient_Colorizing_Fix/master/example.jpg)

## How to acheive same effect in Photoshop

Sadly I do not think there is a simple way to achieve that in Photoshop. But the following steps could achieve a similar result:

1. In Hue/Saturation, set the Saturation and Lightness of Reds, Greens, and Blues to 60 or even higher.
2. Set the Saturation and Lightness of Yellows, Cyans, and Magentas to half the values as Reds, Greens, and Blues.
3. Adjust the Saturation and Lightness of Master until you feel comfortable.

## 那么在PS里该怎么做呢（本代码的理论指导意义）

很遗憾我并不认为在PS中能够很轻松的做到同样的效果。不过下面的这些步骤可以取得差不多的结果：

1. 在色相饱和度里把红绿蓝的饱和度和明度调高至60甚至更高；
2. 同样在色相饱和度里，把黄色青色和洋红的饱和度和明度调高到大概是红绿蓝的一半；
3. 调整全图的饱和度和明度，直到满意为止。

可以事先用普通的方式画出一幅画，然后用灰阶上色的方法画出对应的偏暗的画，用上述方法调整出满意的色相饱和度蒙版图层后，保存这个图层用作以后灰阶上色的修正颜色的图层。
