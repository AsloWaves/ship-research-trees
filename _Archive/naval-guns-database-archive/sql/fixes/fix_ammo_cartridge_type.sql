-- Update Ammunition Cartridge_Type from research file
BEGIN TRANSACTION;

UPDATE Ammunition SET Cartridge_Type = 'Separate' WHERE ID = 12; -- 18" Mark 1 AP
UPDATE Ammunition SET Cartridge_Type = 'Bag' WHERE ID = 14; -- 14" Mark 9 AP
UPDATE Ammunition SET Cartridge_Type = 'Separate' WHERE ID = 29; -- 13" Mark 1 AP
UPDATE Ammunition SET Cartridge_Type = 'Separate' WHERE ID = 30; -- 12" Mark 15 AP
UPDATE Ammunition SET Cartridge_Type = 'Separate' WHERE ID = 32; -- 12" Mark 18 AP
UPDATE Ammunition SET Cartridge_Type = 'Separate' WHERE ID = 33; -- 10" Mark 3 AP
UPDATE Ammunition SET Cartridge_Type = 'Bag' WHERE ID = 34; -- 8" Mark 9 AP
UPDATE Ammunition SET Cartridge_Type = 'Semi-fixed' WHERE ID = 35; -- 8" Mark 12 AP
UPDATE Ammunition SET Cartridge_Type = 'Separate' WHERE ID = 36; -- 8" Mark 16 AP
UPDATE Ammunition SET Cartridge_Type = 'Separate' WHERE ID = 37; -- 8" Mark 71 AP

COMMIT;