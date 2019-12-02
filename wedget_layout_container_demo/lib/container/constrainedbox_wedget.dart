import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class ConstrainedboxWidget extends StatefulWidget{
  @override
  State<StatefulWidget> createState() {
    // TODO: implement createState
    return _ConstrainedboxState();
  }

}

class _ConstrainedboxState extends State<ConstrainedboxWidget>{
  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return Scaffold(
      appBar: AppBar(),
      body: Column(
        children: <Widget>[
          ConstrainedBox(
            constraints: BoxConstraints(
              ///  this.minWidth = 0.0, //最小宽度
              ///  this.maxWidth = double.infinity, //最大宽度
              ///  this.minHeight = 0.0, //最小高度
              ///  this.maxHeight = double.infinity //最大高度
                minWidth: double.infinity, //宽度尽可能大
                minHeight: 50.0 //最小高度为50像素
            ),
            child: Container(
              color: Colors.red,
//                height: 5.0,///不起做
                height: 100.0,//起作用
                width: 50,///不起作用
                child: SizedBox(
                  width: 20,
                  height: 10,
                )
            ),
          ),
          SizedBox(
              width: 80.0,
              height: 80.0,
              child: Container(
                color: Colors.green,
              )
          ),
          Text("多重限制"),
          ConstrainedBox(
              constraints: BoxConstraints(minWidth: 60.0, minHeight: 60.0), //父
              child: ConstrainedBox(
                constraints: BoxConstraints(minWidth: 90.0, minHeight: 20.0),//子
                child: Container(
                  color: Colors.amber,
                ),
              )
          ),
          ConstrainedBox(
              constraints: BoxConstraints(minWidth: 60.0, minHeight: 100.0),  //父
              child: UnconstrainedBox( //“去除”父级限制
                child: ConstrainedBox(
                  constraints: BoxConstraints(minWidth: 90.0, minHeight: 20.0),//子
                  child: Container(
                    color: Colors.cyanAccent,
                  ),
                ),
              )
          )
        ],
      ),
    );
  }

}