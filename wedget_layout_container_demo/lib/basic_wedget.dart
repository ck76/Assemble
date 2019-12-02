import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class BasicWidget extends StatefulWidget {
  @override
  State<StatefulWidget> createState() {
    // TODO: implement createState
    return _BasicWidgetState();
  }
}

class _BasicWidgetState extends State<BasicWidget> {
  var _switchSelected = false;

  var _checkboxSelected = false;

  FocusNode focusNode1 = new FocusNode();
  FocusNode focusNode2 = new FocusNode();
  FocusScopeNode focusScopeNode;

  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return Scaffold(
      appBar: AppBar(
        title: Text("基本组件"),
      ),
      body: ListView(
        children: <Widget>[
          Text(
            "Hello world! I'm Jack. " * 4,
            maxLines: 1,
            textAlign: TextAlign.left,
            textScaleFactor: 1.5,
            overflow: TextOverflow.ellipsis,
          ),
          Divider(
            height: 2,
            thickness: 2,
            color: Colors.black,
          ),
          RaisedButton(
            child: Text("normal"),
            onPressed: () {},
          ),
          FlatButton(
            child: Text("normal"),
            onPressed: () {},
          ),
          OutlineButton(
            child: Text("normal"),
            onPressed: () {},
          ),
          IconButton(
            icon: Icon(Icons.thumb_up),
            padding: EdgeInsets.all(30),
            onPressed: () {},
          ),
          RaisedButton.icon(
            icon: Icon(Icons.send),
            label: Text("发送"),
            onPressed: () {},
          ),
          OutlineButton.icon(
            icon: Icon(Icons.add),
            label: Text("添加"),
            onPressed: () {},
          ),
          FlatButton.icon(
            icon: Icon(Icons.info),
            label: Text("详情"),
            onPressed: () {},
          ),
          FlatButton(
            color: Colors.blue,
            highlightColor: Colors.blue[700],
            colorBrightness: Brightness.dark,
            splashColor: Colors.grey,
            child: Text("Submit"),
            shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(20.0)),
            onPressed: () {},
          ),
          Divider(
            height: 2,
            thickness: 2,
            color: Colors.black,
          ),
          Switch(
            value: _switchSelected, //当前状态
            onChanged: (value) {
              //重新构建页面
              setState(() {
                _switchSelected = value;
              });
            },
          ),
          Checkbox(
            value: _checkboxSelected,
            activeColor: Colors.red, //选中时的颜色
            onChanged: (value) {
              setState(() {
                _checkboxSelected = value;
              });
            },
          ),
          Divider(
            height: 2,
            thickness: 2,
            color: Colors.black,
          ),
          TextField(
            autofocus: true,
            decoration: InputDecoration(
                labelText: "用户名",
                hintText: "用户名或邮箱",
                prefixIcon: Icon(Icons.person)),
          ),
          TextField(
            decoration: InputDecoration(
                labelText: "密码",
                hintText: "您的登录密码",
                prefixIcon: Icon(Icons.lock)),
            obscureText: true,
          ),
          Divider(
            height: 2,
            thickness: 2,
            color: Colors.black,
          ),
          TextField(
            autofocus: true,
            focusNode: focusNode1, //关联focusNode1
            decoration: InputDecoration(labelText: "input1"),
          ),
          TextField(
            focusNode: focusNode2, //关联focusNode2
            decoration: InputDecoration(labelText: "input2"),
          ),
          Builder(
            builder: (ctx) {
              return Column(
                children: <Widget>[
                  RaisedButton(
                    child: Text("移动焦点"),
                    onPressed: () {
                      //将焦点从第一个TextField移到第二个TextField
                      // 这是一种写法 FocusScope.of(context).requestFocus(focusNode2);
                      // 这是第二种写法
                      if (null == focusScopeNode) {
                        focusScopeNode = FocusScope.of(context);
                      }
                      focusScopeNode.requestFocus(focusNode2);
                    },
                  ),
                  RaisedButton(
                    child: Text("隐藏键盘"),
                    onPressed: () {
                      // 当所有编辑框都失去焦点时键盘就会收起
                      focusNode1.unfocus();
                      focusNode2.unfocus();
                    },
                  ),
                ],
              );
            },
          ),
          Divider(
            height: 2,
            thickness: 2,
            color: Colors.black,
          ),
          // 模糊进度条(会执行一个动画)
          LinearProgressIndicator(
            backgroundColor: Colors.grey[200],
            valueColor: AlwaysStoppedAnimation(Colors.blue),
          ),
//进度条显示50%
          LinearProgressIndicator(
            backgroundColor: Colors.grey[200],
            valueColor: AlwaysStoppedAnimation(Colors.blue),
            value: .5,
          ),
          Divider(
            height: 2,
            thickness: 2,
            color: Colors.black,
          ),
          // 线性进度条高度指定为3
          SizedBox(
            height: 3,
            child: LinearProgressIndicator(
              backgroundColor: Colors.grey[200],
              valueColor: AlwaysStoppedAnimation(Colors.blue),
              value: .5,
            ),
          ),
// 圆形进度条直径指定为100
          SizedBox(
            height: 100,
            width: 100,
            child: CircularProgressIndicator(
              backgroundColor: Colors.grey[200],
              valueColor: AlwaysStoppedAnimation(Colors.blue),
              value: .7,
            ),
          ),
          // 宽高不等
          SizedBox(
            height: 100,
            width: 130,
            child: CircularProgressIndicator(
              backgroundColor: Colors.grey[200],
              valueColor: AlwaysStoppedAnimation(Colors.blue),
              value: .7,
            ),
          ),
//      Padding(
//        padding: EdgeInsets.all(16),
//        child: LinearProgressIndicator(
//          backgroundColor: Colors.grey[200],
//          valueColor: ColorTween(begin: Colors.grey, end: Colors.blue)
//              .animate(_animationController), // 从灰色变成蓝色
//          value: _animationController.value,
//        ),
//      ),
        ],
      ),
    );
    ;
  }
}
