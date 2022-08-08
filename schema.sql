DROP TABLE IF EXISTS ads;

CREATE TABLE ads (
    date DATE NOT NULL,
    slot_id INTEGER NOT NULL,
    device TEXT NOT NULL,
    impressions INTEGER NOT NULL DEFAULT 0,
    PRIMARY KEY (date, slot_id, device)
);