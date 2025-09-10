import React, { useEffect, useState } from 'react';

const TelemetryView = () => {
  const [telemetry, setTelemetry] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchTelemetry = async () => {
      try {
        const response = await fetch('http://localhost:5000/api/telemetry');
        if (response.ok) {
          const data = await response.json();
          setTelemetry(data);
          setError('');
        } else {
          setError('Failed to fetch telemetry data');
        }
      } catch (err) {
        console.error('Error fetching telemetry:', err);
        setError('Error connecting to backend');
      }
    };

    fetchTelemetry();
    const interval = setInterval(fetchTelemetry, 3000); // refresh every 3 seconds
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="telemetry-view">
      <h2>Telemetry Data</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}

      {telemetry.length > 0 ? (
        <table>
          <thead>
            <tr>
              <th>Timestamp</th>
              <th>Base Angle</th>
              <th>Shoulder Angle</th>
              <th>Elbow Angle</th>
              <th>Gripper State</th>
            </tr>
          </thead>
          <tbody>
            {telemetry.map((entry, index) => (
              <tr key={index}>
                <td>{new Date(entry.timestamp).toLocaleTimeString()}</td>
                <td>{entry.base_angle}</td>
                <td>{entry.shoulder_angle}</td>
                <td>{entry.elbow_angle}</td>
                <td>{entry.gripper_open ? 'Open' : 'Closed'}</td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p>No telemetry data available</p>
      )}
    </div>
  );
};

export default TelemetryView;
