import React, { useState } from 'react';

const ArmControl = () => {
  const [base, setBase] = useState(90);
  const [shoulder, setShoulder] = useState(90);
  const [elbow, setElbow] = useState(90);
  const [gripper, setGripper] = useState(0);
  const [status, setStatus] = useState('');

  const handleUpdate = async () => {
    const payload = {
      base_angle: base,
      shoulder_angle: shoulder,
      elbow_angle: elbow,
      gripper_angle: gripper
    };

    try {
      const response = await fetch('http://localhost:5000/api/arm/move', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
      });

      if (response.ok) {
        setStatus('Arm movement command sent successfully!');
      } else {
        setStatus('Failed to send command.');
      }
    } catch (error) {
      console.error('Error:', error);
      setStatus('Error sending command.');
    }
  };

  return (
    <div className="arm-control">
      <h2>Robotic Arm Control</h2>

      <div>
        <label>Base Angle: {base}°</label>
        <input
          type="range"
          min="0"
          max="180"
          value={base}
          onChange={(e) => setBase(parseInt(e.target.value))}
        />
      </div>

      <div>
        <label>Shoulder Angle: {shoulder}°</label>
        <input
          type="range"
          min="0"
          max="180"
          value={shoulder}
          onChange={(e) => setShoulder(parseInt(e.target.value))}
        />
      </div>

      <div>
        <label>Elbow Angle: {elbow}°</label>
        <input
          type="range"
          min="0"
          max="180"
          value={elbow}
          onChange={(e) => setElbow(parseInt(e.target.value))}
        />
      </div>

      <div>
        <label>Gripper: {gripper}°</label>
        <input
          type="range"
          min="0"
          max="90"
          value={gripper}
          onChange={(e) => setGripper(parseInt(e.target.value))}
        />
      </div>

      <button onClick={handleUpdate}>Send Command</button>

      {status && <p>{status}</p>}
    </div>
  );
};

export default ArmControl;
