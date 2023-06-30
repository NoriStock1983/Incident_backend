CREATE TABLE MA_USER(
    id serial primary key,
    usercd varchar(8) NOT NULL,
    user_f_name varchar(50) NOT NULL,
    user_l_name varchar(50) NOT NULL,
    belonged_company_id integer NOT NULL,
    belonged_dept_id integer NOT NULL,
    auth_id  integer NOT NULL,
    status_id integer NOT NULL,
    created_by varchar(8) NOT NULL,
    created_date timestamp NOT NULL,
    updated_by varchar(8) NOT NULL,
    updated_date timestamp NOT NULL,
    update_counter integer NOT NULL,
    foreign key(belonged_company_id) references MA_COMPANY(id),
    foreign key(belonged_dept_id) references MA_DEPT(id),
    foreign key(auth_id) references MA_AUTH(id),
    foreign key(status_id) references MA_CODE(id)
)