CREATE TABLE MA_FUNCTION(
    id serial primary key,
    functioncd varchar(3) NOT NULL,
    functionnm varchar(50) NOT NULL,
    functionurl varchar(20) NOT NULL,
    status_id integer NOT NULL,
    created_by varchar(8) NOT NULL,
    created_date timestamp NOT NULL,
    updated_by varchar(8) NOT NULL,
    updated_date timestamp NOT NULL,
    update_counter integer NOT NULL,
    foreign key(status_id) references MA_CODE(id)
)