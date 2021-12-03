#problem1
create table addresses (name varchar(100), kind varchar(100), city varchar(100), state varchar(100));
  insert into addresses (name, kind, city, state) values ('Mom','home','Fairfax','VA');
  insert into addresses (name, kind, city, state) values ('Connie','home','Lynden','WA');
  insert into addresses (name, kind, city, state) values ('Dad','home','Charlotte','NC');
  insert into addresses (name, kind, city, state) values ('Lynn','home','Los Angeles','CA');
  insert into addresses (name, kind, city, state) values ('Pattie','home','Boston','MA');
  insert into addresses (name, kind, city, state) values ('Allen','work','Needham','MA');
  insert into addresses (name, kind, city, state) values ('Jeff','home','Wellesley','MA');
  insert into addresses (name, kind, city, state) values ('Pat','home','Natick','MA');
  insert into addresses (name, kind, city, state) values ('Matt Damon','home','Boston','MA');
  insert into addresses (name, kind, city, state) values ('Matt Damon','work','Hollywood','CA');
  insert into addresses (name, kind, city, state) values ('Scout','home','Dartmouth','NH');
  insert into addresses (name, kind, city, state) values ('Ron','home','Portland','ME');
  insert into addresses (name, kind, city, state) values ('Fred','home','New Haven','CT');
  insert into addresses (name, kind, city, state) values ('George','home','Providence','RI');
  insert into addresses (name, kind, city, state) values ('Harry','home','Montpelier','VT');
  insert into addresses (name, kind, city, state) values ('Percy','work','Providence','RI');

#problem2
create table phones (name varchar(100), kind varchar(100), phone varchar(100));
  insert into phones (name, kind, phone) values ('Mom','home','7035555681');
  insert into phones (name, kind, phone) values ('Mom','cell','7035551234');
  insert into phones (name, kind, phone) values ('Connie','home','6095551243');
  insert into phones (name, kind, phone) values ('Dad','home','7045553004');
  insert into phones (name, kind, phone) values ('Dad','cell','7045551324');
  insert into phones (name, kind, phone) values ('Dad','other','7045551343');
  insert into phones (name, kind, phone) values ('Lynn','cell','6915551423');
  insert into phones (name, kind, phone) values ('Pattie','home','6175551432');
  insert into phones (name, kind, phone) values ('Allen','home','6175552134');
  insert into phones (name, kind, phone) values ('Jeff','work','7815552314');
  insert into phones (name, kind, phone) values ('Pat','work','7815552341');
  insert into phones (name, kind, phone) values ('Matt Damon','work','6175552341');
  insert into phones (name, kind, phone) values ('Scout','cell','8085553124');
  insert into phones (name, kind, phone) values ('Ron','home','2075551111');
  insert into phones (name, kind, phone) values ('Fred','cell','2035552222');
  insert into phones (name, kind, phone) values ('George','work','7815553333');
  insert into phones (name, kind, phone) values ('George','home','4015554444');
  insert into phones (name, kind, phone) values ('Harry','home','8025558888');
  insert into phones (name, kind, phone) values ('Percy','cell','4015559999');


#problem3

#b 
SELECT count(*), name 
FROM phones
group by name
order by name ASC;

