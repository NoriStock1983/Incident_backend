-- テーブル作成
CREATE TABLE MA_CODE(
    id serial primary key,
    code_1 varchar(4) NOT NULL,
    code_2 varchar(2) NOT NULL,
    code_nm_1 varchar(50) NOT NULL,
    code_nm_2 varchar(50) NOT NULL,
    Active_flg boolean NOT NULL,
    created_by varchar(8) NOT NULL,
    created_date timestamp NOT NULL,
    updated_by varchar(8) NOT NULL,
    updated_date timestamp NOT NULL,
    update_counter integer NOT NULL
)