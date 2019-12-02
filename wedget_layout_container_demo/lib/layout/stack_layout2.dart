import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class StackLayout2 extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    // TODO: implement createState
    return _StackLayout2();
  }
}

class _StackLayout2 extends State<StackLayout2> {
  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return Scaffold(
      appBar: AppBar(),
      body: //通过ConstrainedBox来确保Stack占满屏幕
          Stack(
        alignment: Alignment.center,
        fit: StackFit.expand, //未定位widget占满Stack整个空间
        children: <Widget>[
          Positioned(
            left: 18.0,
            child: Text("I am Jack"),
          ),
          Container(
            child: Text("Hello world", style: TextStyle(color: Colors.white)),
            color: Colors.red,
          ),
          Positioned(
            bottom: 10,
            child: Container(
              child: Text("Hello world", style: TextStyle(color: Colors.white)),
              color: Colors.green,
            ),
          ),
          Positioned(
            top: 18.0,
            child: Text("Your friend"),
          )
        ],
      ),
    );
  }
}

//class _StackLayout extends State<StackLayout> {
//  @override
//  Widget build(BuildContext context) {
//    // TODO: implement build
//    return Scaffold(
//        appBar: AppBar(),
//        body: //通过ConstrainedBox来确保Stack占满屏幕
//        Column(
//          children: <Widget>[
//            Flex(
//              direction: Axis.vertical,
//              children: <Widget>[
//                Expanded(
//                  flex: 1,
//                  child: Container(
//                      height: 30.0,
//                      color: Colors.red,
//                      child: ConstrainedBox(
//                        constraints: BoxConstraints.expand(),
//                        child: Stack(
//                          alignment: Alignment.center, //指定未定位或部分定位widget的对齐方式
//                          children: <Widget>[
//                            Container(
//                              child: Text("Hello world",
//                                  style: TextStyle(color: Colors.white)),
//                              color: Colors.red,
//                            ),
//                            Positioned(
//                              left: 18.0,
//                              child: Text("I am Jack"),
//                            ),
//                            Positioned(
//                              top: 18.0,
//                              child: Text("Your friend"),
//                            )
//                          ],
//                        ),
//                      ),
//                  ),
//                ),
//                Expanded(
//                  flex: 1,
//                  child: Container(
//                      height: 30.0,
//                      color: Colors.red,
//                      child: Stack(
//                        alignment: Alignment.center,
//                        fit: StackFit.expand, //未定位widget占满Stack整个空间
//                        children: <Widget>[
//                          Positioned(
//                            left: 18.0,
//                            child: Text("I am Jack"),
//                          ),
//                          Container(
//                            child: Text("Hello world",
//                                style: TextStyle(color: Colors.white)),
//                            color: Colors.red,
//                          ),
//                          Positioned(
//                            top: 18.0,
//                            child: Text("Your friend"),
//                          )
//                        ],
//                      ),
//                  ),
//                ),
//              ],
//            )
//          ],
//        ));
//  }
//}
