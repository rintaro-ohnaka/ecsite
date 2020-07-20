-- ECサイトに必要なテーブルをここに記述

CREATE TABLE user_table(
    id INT AUTO_INCREMENT,
    user_name VARCHAR(255),
    password VARCHAR(255),
    created_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
)