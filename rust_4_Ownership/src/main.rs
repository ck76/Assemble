fn main() {
    let mut s = String::from("hello world");

    let word = first_word(&s);

    s.clear(); // error!

//    println!("the first word is: {}", word);

    let s1 = String::from("foo");
    let result;

    let s2 = String::from("barbaz");
    result = longest(s1.as_str(), s2.as_str());

    println!("result is: {}", result);
}


fn first_word(s: &String) -> &str {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }

    &s[..]
}

///编译失败
///help: this function's return type contains a borrowed value, but the signature does not say whether it is borrowed from `x` or `y`
//fn longestFail(x: &str, y: &str) -> &str {
//    if x.len() > y.len() {
//        return x;
//    }
//    return y;
//}

fn longest<'ck>(x: &'ck str, y: &'ck str) -> &'ck str {
    if x.len() > y.len() {
        return x;
    }
    return y;
}

