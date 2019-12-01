import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter_state_manager_demo/provider_page.dart';
import 'package:flutter_state_manager_demo/redux_page.dart';
import 'package:flutter_state_manager_demo/scoped_page.dart';

import 'bloc_page.dart';

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
        "bloc": (context) {
          return BlocPage();
        },
        "scoped": (context) {
          return ScopedPage();
        },
        "redux": (context) {
          return ReduxPage();
        },
//        "fish": (context) {
//          return FishPage().buildPage(null);
//        },
        "provider": (context) {
          return ProviderPage();
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
                  Navigator.of(context).pushNamed("bloc");
                },
                child: new Text("bloc")),
            new FlatButton(
                onPressed: () {
                  Navigator.of(context).pushNamed("scoped");
                },
                child: new Text("scoped_model")),
            new FlatButton(
                onPressed: () {
                  Navigator.of(context).pushNamed("redux");
                },
                child: new Text("flutter_redux")),
            new FlatButton(
                onPressed: () {
                  Navigator.of(context).pushNamed("fish");
                },
                child: new Text("fish_redux")),
            new FlatButton(
                onPressed: () {
                  Navigator.of(context).pushNamed("provider");
                },
                child: new Text("provider")),
          ],
        ),
      ),
    );
  }
}
