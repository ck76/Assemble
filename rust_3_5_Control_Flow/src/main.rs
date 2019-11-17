fn main() {
    let number = 3;

    if number < 5 {
        println!("condition was true");
    } else {
        println!("condition was false");
    }

    if true {}

//    编译错误
//    if 1 { }
//    if 3 { }

    //因为变量必须只有一个类型。
    // **Rust 需要在**编译时就确切的知道 `number` 变量的类型**，
    // 这样它就可以在编译时验证在每处使用的 `number` 变量的类型是有效的。
    let condition = true;

//    let number = if condition {
//        5
//    } else {
//        "six"
//    };


    let mut counter = 0;

    let result = loop {
        counter += 1;

        if counter == 6 {
            continue;
        }
        println!("{}", counter);
        if counter == 10 {
            break counter * 2;
        }
    };

    println!("The result is {}", result);

    println!();

    let a = [10, 20, 30, 40, 50];
    let mut index = 0;

    while index < 5 {
        println!("the value is: {}", a[index]);

        index = index + 1;
    }

    println!();

    for element in a.iter() {
        println!("the value is: {}", element);
    }

    println!();
    /**
    3!
    2!
    1!
    LIFTOFF!!!
    **/
    for number in (1..4) {
        println!("{}!", number);
    }
    println!();
    for number in (1..4).rev() {
        println!("{}!", number);
    }
    println!("LIFTOFF!!!");

}
