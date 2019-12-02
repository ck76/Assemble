import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

///但如果我们只想简单的调整一个子元素在父元素中的位置的话，使用Align组件会更简单一些。
///Align 组件可以调整子组件的位置，并且可以根据子组件的宽高来确定自身的的宽高，
///
/**
 * alignment : 需要一个AlignmentGeometry类型的值，表示子组件在父组件中的起始位置。
    // ignore: slash_for_doc_comments
 * AlignmentGeometry 是一个抽象类，它有两个常用的子类：Alignment和 FractionalOffset
 * ，我们将在下面的示例中详细介绍。
    // ignore: slash_for_doc_comments
    widthFactor和heightFactor是用于确定Align 组件本身宽高的属性；它们是两个缩放因子，
    会分别乘以子元素的宽、高，最终的结果就是Align 组件的宽高。如果值为null，则组件的宽高将会占用尽可能多的空间。
 */
class AlignWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return Scaffold(
        appBar: AppBar(),
        body: Column(
          children: <Widget>[
            Text(" Widget会以矩形的中心点作为坐标原点，即Alignment(0.0, 0.0) 。"
                "x、y的值从-1到1分别代表矩形左边到右边的距离和顶部到底边的距离，"),
            Container(
              height: 120.0,
              width: 120.0,
              color: Colors.blue[50],
              child: Align(
                alignment: Alignment.topRight,
                child: FlutterLogo(
                  size: 60,
                ),
              ),
            ),
            Text("因为FlutterLogo的宽高为60，则Align的最终宽高都为2*60=120。"),
            Container(
              color: Colors.green,
              child:  Align(
                widthFactor: 2,
                heightFactor: 2,
                alignment: Alignment(2, 0.0),

                ///因为FlutterLogo的宽高为60，则Align的最终宽高都为2*60=120。
                child: FlutterLogo(
                  size: 60,
                ),
              ),
            ),

            Text('''FractionalOffset
FractionalOffset 继承自 Alignment，它和 Alignment唯一的区别就是坐标原点不同！
FractionalOffset 的坐标原点为矩形的左侧顶点，这和布局系统的一致，所以理解起来会比较容易。'''),
            Container(
              height: 120.0,
              width: 120.0,
              color: Colors.blue[50],
              child: Align(
                alignment: FractionalOffset(0.2, 0.6),
                child: FlutterLogo(
                  size: 60,
                ),
              ),
            ),
            DecoratedBox(
              decoration: BoxDecoration(color: Colors.red),
              child: Center(
                child: Text("xxx"),
              ),
            ),
            DecoratedBox(
              decoration: BoxDecoration(color: Colors.red),
              child: Center(
                widthFactor: 1,
                heightFactor: 1,
                child: Text("xxx"),
              ),
            ),
          ],
        ));
  }
}
