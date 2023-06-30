CREATE TABLE MA_AUTH(
    id serial primary key,
    authcd varchar(3) NOT NULL,
    authnm varchar(50) NOT NULL,
    status_id integer NOT NULL,
    created_by varchar(8) NOT NULL,
    created_date timestamp NOT NULL,
    updated_by varchar(8) NOT NULL,
    updated_date timestamp NOT NULL,
    update_counter integer NOT NULL,
    foreign key(status_id) references MA_CODE(id)
)