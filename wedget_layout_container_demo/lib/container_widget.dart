import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class ContainerWidget extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    // TODO: implement createState
    return _ContainerState();
  }
}

class _ContainerState extends State<ContainerWidget> {
  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return Scaffold(
      appBar: AppBar(),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            new FlatButton(
                onPressed: () {
                  Navigator.of(context).pushNamed("padding");
                },
                child: new Text("填充（Padding）")),
            new FlatButton(
                onPressed: () {
                  Navigator.of(context).pushNamed("ConstrainedBox");
                },
                child: new Text("尺寸限制类容器（ConstrainedBox等）")),
            new FlatButton(
                onPressed: () {
                  Navigator.of(context).pushNamed("DecoratedBox");
                },
                child: new Text("装饰容器（DecoratedBox）")),
            new FlatButton(
                onPressed: () {
                  Navigator.of(context).pushNamed("Transform");
                },
                child: new Text("变换（Transform）")),
            new FlatButton(
                onPressed: () {
                  Navigator.of(context).pushNamed("Container");
                },
                child: new Text("Container容器")),
            new FlatButton(
                onPressed: () {
                  Navigator.of(context).pushNamed("Scaffold");
                },
                child: new Text("Scaffold、TabBar、底部导航")),
            new FlatButton(
                onPressed: () {
                  Navigator.of(context).pushNamed("clip");
                },
                child: new Text("剪裁（Clip）")),
          ],
        ),
      ),
    );
  }
}
