CREATE TABLE users (
    id integer primary key,
    mac text not null,
    phone integer not null,
    dreg date not null,
    dlaccess date not null,
    passkode text not null,
    acode integer not null
);
CREATE TABLE macs (
    id integer primary key,
    uid integer not null,
    mac text not null
);
CREATE TABLE lastAccess (
    mac text not null,
    bdate int not null
    edate int not null
);
