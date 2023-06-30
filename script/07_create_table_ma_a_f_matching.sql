CREATE TABLE MA_A_F_MATCHING(
    id serial primary key,
    authid integer NOT NULL,
    functionid integer NOT NULL,
    created_by varchar(8) NOT NULL,
    created_date timestamp NOT NULL,
    updated_by varchar(8) NOT NULL,
    updated_date timestamp NOT NULL,
    update_counter integer NOT NULL,
    foreign key(authid) references MA_AUTH(id),
    foreign key(functionid) references MA_FUNCTION(id)
)