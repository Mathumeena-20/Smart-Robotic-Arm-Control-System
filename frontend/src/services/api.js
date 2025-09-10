const API_BASE_URL = 'http://localhost:5000/api'; // Flask backend URL

// Function to send control commands to the robotic arm
export async function sendArmCommand(command) {
  try {
    const response = await fetch(`${API_BASE_URL}/control`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(command),
    });
    return await response.json();
  } catch (error) {
    console.error('Error sending arm command:', error);
    throw error;
  }
}

// Function to fetch real-time telemetry data
export async function getTelemetry() {
  try {
    const response = await fetch(`${API_BASE_URL}/telemetry`);
    if (!response.ok) {
      throw new Error('Failed to fetch telemetry');
    }
    return await response.json();
  } catch (error) {
    console.error('Error fetching telemetry:', error);
    throw error;
  }
}

// Function to fetch robot state
export async function getRobotState() {
  try {
    const response = await fetch(`${API_BASE_URL}/state`);
    if (!response.ok) {
      throw new Error('Failed to fetch robot state');
    }
    return await response.json();
  } catch (error) {
    console.error('Error fetching robot state:', error);
    throw error;
  }
}

// Function to update robot configuration
export async function updateConfiguration(config) {
  try {
    const response = await fetch(`${API_BASE_URL}/config`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(config),
    });
    return await response.json();
  } catch (error) {
    console.error('Error updating configuration:', error);
    throw error;
  }
}
