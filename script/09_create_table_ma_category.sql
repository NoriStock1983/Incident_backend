CREATE TABLE MA_CATEGORY(
    id serial primary key,
    categorycd varchar(3) NOT NULL,
    categorynm varchar(50) NOT NULL,
    status_id integer NOT NULL,
    class_id integer NOT NULL,
    created_by varchar(8) NOT NULL,
    created_date timestamp NOT NULL,
    updated_by varchar(8) NOT NULL,
    updated_date timestamp NOT NULL,
    update_counter integer NOT NULL,
    foreign key(status_id) references MA_CODE(id),
    foreign key(class_id) references MA_CODE(id)
)