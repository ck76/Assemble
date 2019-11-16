//猜猜看

use std::cmp::Ordering;
//标准库io
use std::io as cout;
//Rng 是一个 trait，它定义了随机数生成器应实现的方法，
// 想使用这些方法的话，此 trait 必须在作用域中。
// 第十章会详细介绍 trait。
use rand::Rng;


//默认情况下，Rust 将 prelude 模块中少量的类型引入到每个程序的作用域中。
// 如果需要的类型不在 prelude 中，你必须使用 use 语句显式地将其引入作用域。

fn main() {
    println!("请猜数字！");

    loop {

        //rand::thread_rng 函数提供实际使用的随机数生成器：
        // 它位于当前执行线程的本地环境中，并从操作系统获取 seed。接下来，
        // 调用随机数生成器的 gen_range 方法。
        // 这个方法由刚才引入到作用域的 Rng trait 定义。
        // gen_range 方法获取两个数字作为参数，并生成一个范围在两者之间的随机数。
        // 它包含下限但不包含上限，所以需要指定 1 和 101 来请求一个 1 和 100 之间的数。
        let secret_number = rand::thread_rng()
            .gen_range(1, 101);

        println!("{}", secret_number);

        //创建一个储存用户输入的地方
        //注意这是一个 let 语句，用来创建 变量

        //::new 那一行的 :: 语法表明 new 是 String 类型的一个 关联函数（associated function）。
        // 关联函数是针对类型实现的，在这个例子中是 String，而不是 String 的某个特定实例。
        // 一些语言中把它称为 静态方法（static method）
        let mut guess = String::new();

        cout::stdin()
            .read_line(&mut guess)
            .expect("读取失败");

        //32 位无符号数字 u32；64 位数字 i64 等等。Rust 默认使用 i32，
        let guess: u32 = match guess
            .trim()
            .parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        //这行代码新建了一个叫做 foo 的变量并把它绑定到值 bar 上。在 Rust 中，
        // 变量默认是不可变的。
        //let foo = bar;
        // let foo = 5; // 不可变
        // let mut bar = 5; // 可变

        //& 表示这个参数是一个 引用（reference），
        // 它允许多处代码访问同一处数据，而无需在内存中多次拷贝。
        // 引用是一个复杂的特性，Rust 的一个主要优势就是安全而简单的操纵引用。
        // 完成当前程序并不需要了解如此多细节。
        // 现在，我们只需知道它像变量一样，默认是不可变的。
        // 因此，需要写成 &mut guess 来使其可变，而不是 &guess。（第四章会更全面的解释引用。）

        println!("你猜的是：{}", guess);

        //一个 match 表达式由 分支（arms） 构成。
        // 一个分支包含一个 模式（pattern）和表达式开头的值与分支模式相匹配时应该执行的代码。R
        match guess.cmp(&secret_number) {
            Ordering::Less => println!("太小"),
            Ordering::Greater => println!("太大!"),
            Ordering::Equal => {
                println!("你赢了!");
                break;
            }
        }
    }
}
