import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:widget_layout_container_demo/layout/align_widget.dart';
import 'package:widget_layout_container_demo/layout/flex_layout.dart';
import 'package:widget_layout_container_demo/layout/follow_layout.dart';
import 'package:widget_layout_container_demo/layout/linear_layout.dart';
import 'package:widget_layout_container_demo/layout/stack_layout.dart';
import 'package:widget_layout_container_demo/layout_widget.dart';

import 'basic_wedget.dart';
import 'container/clip_wedget.dart';
import 'container/constrainedbox_wedget.dart';
import 'container/container_wedget.dart';
import 'container/decoratebox_wedget.dart';
import 'container/padding_wedget.dart';
import 'container/scaffold_wedget.dart';
import 'container/transform_wedget.dart';
import 'container_widget.dart';
import 'layout/stack_layout2.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "Flutter State Manager",
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(),
      routes: {
        "basic_widget": (context) {
          return BasicWidget();
        },
        "layout_widget": (context) {
          return LayoutWidget();
        },
        "container_widget": (context) {
          return ContainerWidget();
        },

        ///布局
        "linear_layout": (context) {
          return LinearLayout();
        },
        "flex_layout": (context) {
          return FlexLayout();
        },
        "follow_layout": (context) {
          return FollowLayout();
        },
        "stack_layout": (context) {
          return StackLayout();
        },
        "stack_layout2": (context) {
          return StackLayout2();
        },
        "align": (context) {
          return AlignWidget();
        },

        ///容器
        "padding": (context) {
          return PaddingWidget();
        },
        "ConstrainedBox": (context) {
          return ConstrainedboxWidget();
        },
        "DecoratedBox": (context) {
          return DecorateboxWidget();
        },
        "Transform": (context) {
          return TransformWidget();
        },
        "Container": (context) {
          return ContainerWidget2();
        },
        "Scaffold": (context) {
          return ScaffoldWidget();
        },
        "clip": (context) {
          return ClipWidget();
        },
      },
    );
  }
}

class MyHomePage extends StatefulWidget {
  final String title;

  MyHomePage({Key key, this.title}) : super(key: key);

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return Scaffold(
//      appBar: AppBar(
//        title: Text(widget.title),
//      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            new FlatButton(
                onPressed: () {
                  Navigator.of(context).pushNamed("basic_widget");
                },
                child: new Text("基础组件")),
            new FlatButton(
                onPressed: () {
                  Navigator.of(context).pushNamed("layout_widget");
                },
                child: new Text("布局类组件")),
            new FlatButton(
                onPressed: () {
                  Navigator.of(context).pushNamed("container_widget");
                },
                child: new Text("容器类组件")),
          ],
        ),
      ),
    );
  }
}
