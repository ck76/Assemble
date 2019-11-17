///我们也可以定义一个没有任何字段的结构体！
/// 它们被称为 类单元结构体（unit-like structs）
/// 因为它们类似于 ()，即 unit 类型。
/// 类单元结构体常常在你想要在某个类型上实现 trait
/// 但不需要在类型中存储数据的时候发挥作用。
/// 我们将在第十章介绍 trait。

/**
在示例 5-1 中的 User 结构体的定义中，
我们使用了自身拥有所有权的 String 类型
而不是 &str 字符串 slice 类型。
这是一个有意而为之的选择，因为我们想要这个结构体拥有它所有的数据，
为此只要整个结构体是有效的话其数据也是有效的。

可以使结构体存储被其他对象拥有的数据的引用，
不过这么做的话需要用上 生命周期（lifetimes），
这是一个第十章会讨论的 Rust 功能。
生命周期确保结构体引用的数据有效性跟结构体本身保持一致。
如果你尝试在结构体中存储一个引用而不指定生命周期将是无效的，比如这样

struct User {
    username: &str,
    email: &str,
    sign_in_count: u64,
    active: bool,
}

fn main() {
    let user1 = User {
        email: "someone@example.com",
        username: "someusername123",
        active: true,
        sign_in_count: 1,
    };
}

error[E0106]: missing lifetime specifier
 -->
  |
2 |     username: &str,
  |               ^ expected lifetime parameter

error[E0106]: missing lifetime specifier
 -->
  |
3 |     email: &str,
  |            ^ expected lifetime parameter


**/
