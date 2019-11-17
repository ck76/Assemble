///也可以定义与元组（在第三章讨论过）类似的结构体，
/// 称为 元组结构体（tuple structs）。
/// 元组结构体有着结构体名称提供的含义，但没有具体的字段名，
/// 只有字段的类型。当你想给整个元组取一个名字，
/// 并使元组成为与其他元组不同的类型时，元组结构体是很有用的，
/// 这时像常规结构体那样为每个字段命名就显得多余和形式化了。
//
///定义元组结构体，以 struct 关键字和结构体名开头并后跟元组中的类型。
/// 例如，下面是两个分别叫做 Color 和 Point 元组结构体的定义和用法：

#![allow(unused_variables)]
fn main() {
    struct Color(i32, i32, i32);
    struct Point(i32, i32, i32);

    let black = Color(0, 0, 0);
    let origin = Point(0, 0, 0);
}
