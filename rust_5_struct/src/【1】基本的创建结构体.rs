struct User {
    username: String,
    email: String,
    sign_in_count: u64,
    active: bool,
}

fn creatUser(email: String, username: String,user2:User)->User{
    User{
        email,
        username,
        active: true,
        sign_in_count: 1,
        ..user2
    }
}
