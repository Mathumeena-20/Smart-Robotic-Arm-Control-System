-- Create Database (only if running outside Docker auto init)
-- CREATE DATABASE robotics_db;

-- Switch to robotics_db (only if running manually)
-- \c robotics_db;

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
-- Table: app_users
-- -------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS app_users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- -------------------------------------------------------------------
-- Insert Default User (admin)
-- -------------------------------------------------------------------
INSERT INTO app_users (username, password_hash)
VALUES ('admin', '$2b$12$7J8Qy.RbXH6m1e4kE5Fy0O4gF7n.E7z/2o6KHYh8xYV0CkJKZlZ4O')
ON CONFLICT (username) DO NOTHING;

-- -------------------------------------------------------------------
-- Insert Sample Robot State
-- -------------------------------------------------------------------
INSERT INTO robot_state (joint1_angle, joint2_angle, joint3_angle, grip_status)
VALUES (0.0, 0.0, 0.0, FALSE)
ON CONFLICT DO NOTHING;

-- -------------------------------------------------------------------
-- Insert Sample Telemetry
-- -------------------------------------------------------------------
INSERT INTO telemetry (temperature, voltage, current)
VALUES (36.5, 12.5, 1.2)
ON CONFLICT DO NOTHING;
