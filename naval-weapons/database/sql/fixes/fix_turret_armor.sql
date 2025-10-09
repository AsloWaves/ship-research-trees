-- Update Turret Armor data from research file
BEGIN TRANSACTION;

UPDATE Turrets SET Armor_Sides_IN = 18.0, Armor_Roof_IN = 10.0 WHERE Turret_ID = 25; -- 14"/50 Mark 4 Triple Turret

COMMIT;