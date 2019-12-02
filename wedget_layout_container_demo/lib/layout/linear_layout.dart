import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class LinearLayout extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    // TODO: implement createState
    return _LinearLayout();
  }
}

class _LinearLayout extends State<LinearLayout> {
  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return Scaffold(
    appBar: AppBar(),
      body: Center(
        child: ListView(
          children: <Widget>[
            Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              verticalDirection: VerticalDirection.up,
              children: <Widget>[
                Text(
                  " hello world ",
                  style: TextStyle(fontSize: 30.0),
                ),
                Text(" I am Jack "),
              ],
            ),

            Divider(
              thickness: 5,
              color: Colors.black,
            ),

            ///实际上，Row和Column都只会在主轴方向占用尽可能大的空间，而纵轴的长度则取决于他们最大子元素的长度。
            ///如果Row里面嵌套Row，或者Column里面再嵌套Column，
            ///那么只有对最外面的Row或Column会占用尽可能大的空间，里面Row或Column所占用的空间为实际大小，
            Column(
              crossAxisAlignment: CrossAxisAlignment.end,
              verticalDirection: VerticalDirection.down,
              mainAxisAlignment: MainAxisAlignment.start,
              mainAxisSize: MainAxisSize.max,
              children: <Widget>[
                Text(
                  " hello world ",
                  style: TextStyle(fontSize: 30.0),
                ),
                Text(" I am Jack "),
              ],
            ),
            Container(
              color: Colors.green,
              child: Padding(
                padding: const EdgeInsets.all(16.0),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  mainAxisSize: MainAxisSize.max, //有效，外层Colum高度为整个屏幕
                  children: <Widget>[
                    Container(
                      color: Colors.red,
                      child: Column(
                        mainAxisSize: MainAxisSize.max, //无效，内层Colum高度为实际高度
                        children: <Widget>[
                          Text("hello world "),
                          Text("I am Jack "),
                        ],
                      ),
                    )
                  ],
                ),
              ),
            ),
//            Container(
//              color: Colors.green,
//              child: Padding(
//                padding: const EdgeInsets.all(16.0),
//                child: Column(
//                  crossAxisAlignment: CrossAxisAlignment.start,
//                  mainAxisSize: MainAxisSize.max, //有效，外层Colum高度为整个屏幕
//                  children: <Widget>[
//                    Expanded(
//                      child: Container(
//                        color: Colors.red,
//                        child: Column(
//                          mainAxisAlignment: MainAxisAlignment.center, //垂直方向居中对齐
//                          children: <Widget>[
//                            Text("hello world "),
//                            Text("I am Jack "),
//                          ],
//                        ),
//                      ),
//                    ),
//                  ],
//                ),
//              ),
//            ),
          ],
        ),
      ),
    );
  }
}
