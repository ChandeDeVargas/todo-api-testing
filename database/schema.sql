-- Database schema for TODO API
-- Used for testing and development

CREATE TABLE IF NOT EXISTS tasks (
    id_tasks INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    description VARCHAR(500) NOT NULL,
    create_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    due_date DATETIME,
    is_completed TINYINT(1) DEFAULT 0
);