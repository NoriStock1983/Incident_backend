CREATE TABLE MA_DEPT(
    id serial primary key,
    companyid integer NOT NULL,
    deptcd varchar(4) NOT NULL,
    deptnm varchar(50) NOT NULL,
    deptnm_short varchar(20) NOT NULL,
    status_id integer NOT NULL,
    created_by varchar(8) NOT NULL,
    created_date timestamp NOT NULL,
    updated_by varchar(8) NOT NULL,
    updated_date timestamp NOT NULL,
    update_counter integer NOT NULL,
    foreign key(companyid) references MA_COMPANY(id),
    foreign key(status_id) references MA_CODE(id)
)