fn main() {
    let x = 5;

    let y = {
        let x = 3;
        x + 1
//        x + 1;
    };

    println!("The value of y is: {}", y);




    fn five() -> i32 {
        5
    }

    let x = five();

    println!("The value of x is: {}", x);
}
