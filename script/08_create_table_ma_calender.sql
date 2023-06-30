CREATE TABLE MA_CALENDER(
    id serial primary key,
    workdate date NOT NULL,
    week varchar(3) NOT NULL,
    workingflg boolean NOT NULL,
    created_by varchar(8) NOT NULL,
    created_date timestamp NOT NULL,
    updated_by varchar(8) NOT NULL,
    updated_date timestamp NOT NULL,
    update_counter integer NOT NULL
)