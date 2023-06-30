-- テーブル作成
CREATE TABLE MA_COMPANY(
    id serial primary key,
    companycd varchar(4) NOT NULL,
    companynm varchar(50) NOT NULL,
    companynm_short varchar(20) NOT NULL,
    class_id integer NOT NULL,
    status_id integer NOT NULL,
    created_by varchar(8) NOT NULL,
    created_date timestamp NOT NULL,
    updated_by varchar(8) NOT NULL,
    updated_date timestamp NOT NULL,
    update_counter integer NOT NULL,
    foreign key(class_id) references MA_CODE(id),
    foreign key(status_id) references MA_CODE(id)
)