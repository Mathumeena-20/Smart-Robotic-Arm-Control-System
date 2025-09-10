-- Create Database (if not exists)
CREATE DATABASE robotics_db;

\c robotics_db;

-- -------------------------------------------------------------------
-- Table: robot_state
-- -------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS robot_state (
    id SERIAL PRIMARY KEY,
    joint1_angle FLOAT NOT NULL,
    joint2_angle FLOAT NOT NULL,
    joint3_angle FLOAT NOT NULL,
    grip_status BOOLEAN NOT NULL DEFAULT FALSE,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- -------------------------------------------------------------------
-- Table: telemetry
-- -------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS telemetry (
    id SERIAL PRIMARY KEY,
    temperature FLOAT,
    voltage FLOAT,
    current FLOAT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- -------------------------------------------------------------------
-- Table: users (for authentication if required)
-- -------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS app_users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- -------------------------------------------------------------------
-- Insert Sample Data
-- -------------------------------------------------------------------
INSERT INTO robot_state (joint1_angle, joint2_angle, joint3_angle, grip_status)
VALUES (0.0, 0.0, 0.0, FALSE),
       (45.0, 30.0, 15.0, TRUE);

INSERT INTO telemetry (temperature, voltage, current)
VALUES (36.5, 12.5, 1.2),
       (37.0, 12.7, 1.3);

INSERT INTO app_users (username, password_hash)
VALUES ('admin', '$2b$12$7J8Qy.RbXH6m1e4kE5Fy0O4gF7n.E7z/2o6KHYh8xYV0CkJKZlZ4O'); -- bcrypt hash of 'admin123'
