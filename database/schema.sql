-- Database schema for TODO API
-- Improved: Consolidated and optimized schema

-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS all_tasks_testing_practice 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

USE all_tasks_testing_practice;

-- Tasks table
CREATE TABLE IF NOT EXISTS tasks (
    id_tasks INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    description VARCHAR(500) NOT NULL,
    create_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    due_date DATETIME NULL,
    is_completed TINYINT(1) DEFAULT 0,
    
    -- Indexes for better performance
    INDEX idx_completed (is_completed),
    INDEX idx_created (create_at),
    INDEX idx_due_date (due_date)
);

-- Insert sample data (optional)
INSERT IGNORE INTO tasks (title, description, due_date) VALUES
('Example task 1', 'Description for example task 1', DATE_ADD(NOW(), INTERVAL 7 DAY)),
('Example task 2', 'Description for example task 2', DATE_ADD(NOW(), INTERVAL 3 DAY)),
('Completed task', 'This task is already completed', DATE_ADD(NOW(), INTERVAL 1 DAY));

-- Show table structure
DESCRIBE tasks;