fn main() {
    //在 Rust 中，每一个值都属于某一个 数据类型（data type），
    // 这告诉 Rust 它被指定为何种数据，以便明确数据处理方式。
    // 我们将看到两类数据类型子集：标量（scalar）和复合（compound）。
    //
    //记住，Rust 是 静态类型（statically typed）语言，
    // 也就是说在编译时就必须知道所有变量的类型。

    #![allow(unused_variables)]
    let guess: u32 = "42".parse().expect("Not a number!");


}
