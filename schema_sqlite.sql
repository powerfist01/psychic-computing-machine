CREATE TABLE `details` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `created_at` TIMESTAMP NOT NULL DEFAULT (strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime')),
  `updated_at` TIMESTAMP NOT NULL DEFAULT (strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime')),
  `category` INTEGER,
  `description` VARCHAR,
  `quantity` INTEGER,
  `amount` INTEGER
);