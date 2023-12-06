drop schema if exists `iterator-db`;
create schema if not exists `iterator-db`;
use `iterator-db`;

drop table if exists interator;

create table interator (
    state int DEFAULT 0
);

insert into interator (state) values (0);
insert into interator (state) values (1);
insert into interator (state) values (2);
insert into interator (state) values (3);

#-----------------------------------#
#       USER RIGHTS MANAGEMENT      #
#-----------------------------------#
CREATE USER 'userIterator'@'%' IDENTIFIED BY 'qwerty1234';

GRANT ALL PRIVILEGES ON `iterator-db`.* TO 'userIterator'@'%' WITH GRANT OPTION;

FLUSH PRIVILEGES;
