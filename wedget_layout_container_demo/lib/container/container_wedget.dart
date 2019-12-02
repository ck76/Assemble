import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class ContainerWidget2 extends StatefulWidget{
  @override
  State<StatefulWidget> createState() {
    // TODO: implement createState
    return _ContainerWidgetState();
  }

}

class _ContainerWidgetState extends State<ContainerWidget2>{
  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return Scaffold(
      appBar: AppBar(),
      body: Column(
        children: <Widget>[
          Text("Container是一个组合类容器，它本身不对应具体的RenderObject，"
              "它是DecoratedBox、ConstrainedBox、Transform、Padding、Align等组件组合的一个多功能容器"),
          Container(
            margin: EdgeInsets.only(top: 50.0, left: 120.0), //容器外填充
            constraints: BoxConstraints.tightFor(width: 200.0, height: 150.0), //卡片大小
            decoration: BoxDecoration(//背景装饰
                gradient: RadialGradient( //背景径向渐变
                    colors: [Colors.red, Colors.orange],
                    center: Alignment.topLeft,
                    radius: .98
                ),
                boxShadow: [ //卡片阴影
                  BoxShadow(
                      color: Colors.black54,
                      offset: Offset(2.0, 2.0),
                      blurRadius: 4.0
                  )
                ]
            ),
            transform: Matrix4.rotationZ(.2), //卡片倾斜变换
            alignment: Alignment.center, //卡片内文字居中
            child: Text( //卡片文字
              "5.20", style: TextStyle(color: Colors.white, fontSize: 40.0),
            ),
          ),
          Container(
            margin: EdgeInsets.all(20.0), //容器外补白
            color: Colors.orange,
            child: Text("Hello world!"),
          ),
          Container(
            padding: EdgeInsets.all(20.0), //容器内补白
            color: Colors.orange,
            child: Text("Hello world!"),
          ),
          Text("上下代码等价。因为padding和margin都是Padding来实现的"),
          Padding(
            padding: EdgeInsets.all(20.0),
            child: DecoratedBox(
              decoration: BoxDecoration(color: Colors.orange),
              child: Text("Hello world!"),
            ),
          ),
          DecoratedBox(
            decoration: BoxDecoration(color: Colors.orange),
            child: Padding(
              padding: const EdgeInsets.all(20.0),
              child: Text("Hello world!"),
            ),
          ),
        ],
      ),
    );
  }

}