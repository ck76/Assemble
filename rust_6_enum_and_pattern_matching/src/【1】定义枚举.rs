enum IpAddrKind {
    V4,
    V6,
}

struct IpAddr {
    kind: IpAddrKind,
    address: String,
}

enum IpAddrEnum {
    V4(String),
    V6(String),
}

enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}

impl Message {
    fn call(&self) {
        // 在这里定义方法体
        println!("Message.call")
    }
}

struct QuitMessage;

// 类单元结构体
struct MoveMessage {
    x: i32,
    y: i32,
}

struct WriteMessage(String);

// 元组结构体
struct ChangeColorMessage(i32, i32, i32); // 元组结构体


fn main() {
    //注意枚举的成员位于其标识符的命名空间中，并使用两个冒号分开。
    // 这么设计的益处是现在 IpAddrKind::V4 和 IpAddrKind::V6 都是 IpAddrKind 类型的。
    let four = IpAddrKind::V4;
    let six = IpAddrKind::V6;

    route(IpAddrKind::V4);
    route(IpAddrKind::V6);
    route(four);
    route(six);

    let home = IpAddr {
        kind: IpAddrKind::V4,
        address: String::from("127.0.0.1"),
    };

    let loopback = IpAddr {
        kind: IpAddrKind::V6,
        address: String::from("::1"),
    };

    let home = IpAddrEnum::V4(String::from("127.0.0.1"));

    let loopback = IpAddrEnum::V6(String::from("::1"));

    let m = Message::Write(String::from("hello"));
    m.call();

    option_fun();
}

fn route(ip_type: IpAddrKind) {}


//Option 枚举和其相对于空值的优势
enum Option<T> {
    Some(T),
    None,
}

fn option_fun() {
    let mut some_number_five = Some(5);
    let mut some_number_ten = Some(10);
    some_number_five = some_number_ten;
    ///错误
//    let sum=some_number_five + some_number_ten;

    let some_string = Some("a string");
    let some_number_null: Option<i32> = Option::Some(33333333);

//如果使用 None 而不是 Some，需要告诉 Rust Option<T> 是什么类型的，
// 因为编译器只通过 None 值无法推断出 Some 成员保存的值的类型。
//    let absent_number_null =Option::None;
    let absent_number: Option<i32> = Option::None;

    /*
    let x: i8 = 5;
    let y: Option<i8> = Option::Some(5);

    let sum = x + y;
    */
}





