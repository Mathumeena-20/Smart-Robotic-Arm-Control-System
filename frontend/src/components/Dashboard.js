import React, { useEffect, useState } from 'react';

const Dashboard = () => {
  const [robotStatus, setRobotStatus] = useState('Loading...');
  const [lastUpdate, setLastUpdate] = useState('');
  const [sensorData, setSensorData] = useState({});

  useEffect(() => {
    const fetchStatus = async () => {
      try {
        const response = await fetch('http://localhost:5000/api/status');
        if (response.ok) {
          const data = await response.json();
          setRobotStatus(data.status);
          setLastUpdate(new Date(data.timestamp).toLocaleString());
          setSensorData(data.sensors);
        } else {
          setRobotStatus('Failed to load status');
        }
      } catch (error) {
        console.error('Error fetching status:', error);
        setRobotStatus('Error connecting to backend');
      }
    };

    fetchStatus();
    const interval = setInterval(fetchStatus, 5000); // auto-refresh every 5s
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="dashboard">
      <h2>Robotic Arm Dashboard</h2>

      <div className="status-card">
        <h3>Status: {robotStatus}</h3>
        <p>Last Update: {lastUpdate}</p>
      </div>

      <div className="sensor-data">
        <h3>Sensor Data</h3>
        {Object.keys(sensorData).length > 0 ? (
          <ul>
            {Object.entries(sensorData).map(([key, value]) => (
              <li key={key}>
                <strong>{key}:</strong> {value}
              </li>
            ))}
          </ul>
        ) : (
          <p>No sensor data available</p>
        )}
      </div>
    </div>
  );
};

export default Dashboard;
