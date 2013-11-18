-- psql -d footieviz-dev -U Eric -W < postgres.delete_tables.sql

DELETE FROM Fixtures;
DELETE FROM FixturesHistory;
DELETE FROM EventsExplain;
DELETE FROM Players;
DELETE FROM SeasonsHistory;	
DELETE FROM News;