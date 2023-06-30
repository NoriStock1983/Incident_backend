CREATE TABLE MA_SLA(
    id serial primary key,
    priority_id integer NOT NULL,
    urgency_id integer NOT NULL,
    correspondtime integer NOT NULL,
    status_id integer NOT NULL,
    created_by varchar(8) NOT NULL,
    created_date timestamp NOT NULL,
    updated_by varchar(8) NOT NULL,
    updated_date timestamp NOT NULL,
    update_counter integer NOT NULL,
    foreign key(priority_id) references MA_CODE(id),
    foreign key(urgency_id) references MA_CODE(id),
    foreign key(status_id) references MA_CODE(id)
)