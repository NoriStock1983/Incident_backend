CREATE TABLE MA_SUBCATEGORY(
    id serial primary key,
    category_id integer NOT NULL,
    subcategorycd varchar(3) NOT NULL,
    subcategorynm varchar(50) NOT NULL,
    status_id integer NOT NULL,
    class_id integer NOT NULL,
    created_by varchar(8) NOT NULL,
    created_date timestamp NOT NULL,
    updated_by varchar(8) NOT NULL,
    updated_date timestamp NOT NULL,
    update_counter integer NOT NULL,
    foreign key(category_id) references MA_CATEGORY(id),
    foreign key(status_id) references MA_CODE(id),
    foreign key(class_id) references MA_CODE(id)
)