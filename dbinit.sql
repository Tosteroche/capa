CREATE TABLE users (
    id integer primary key,
    mac text not null,
    phone integer not null,
    dreg date not null,
    dlaccess date not null,
    passkode text,
    acode integer not null
);
