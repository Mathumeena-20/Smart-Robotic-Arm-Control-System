import React, { useState } from "react";
import axios from "axios";

function App() {
  const [direction, setDirection] = useState("");
  const [speed, setSpeed] = useState(50);

  const sendCommand = () => {
    axios.post("http://localhost:5000/api/robot/move", {
      direction,
      speed
    }).then(res => alert(res.data.status));
  };

  return (
    <div>
      <h1>Robotic Arm Control</h1>
      <input placeholder="Direction" value={direction} onChange={(e) => setDirection(e.target.value)} />
      <input type="number" value={speed} onChange={(e) => setSpeed(e.target.value)} />
      <button onClick={sendCommand}>Move</button>
    </div>
  );
}

export default App;
