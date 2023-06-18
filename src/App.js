import React, { useState } from 'react';
import axios from 'axios';
import { Button, Form } from 'react-bootstrap';

function App() {
  const [problemName, setProblemName] = useState('');
  const [problemLink, setProblemLink] = useState('');

  const createPythonFile = async () => {
    const response = await axios.post('http://localhost:5000/create_file', {
      problemName,
      problemLink,
    });
    console.log(response.data);
  };

  return (
    <div className="container mt-4">
      <h1>LeetCode Automation</h1>
      <Form>
        <Form.Group controlId="problemName">
          <Form.Label>Problem Name</Form.Label>
          <Form.Control
            type="text"
            placeholder="Enter the problem name"
            value={problemName}
            onChange={(e) => setProblemName(e.target.value)}
          />
        </Form.Group>
        <Form.Group controlId="problemLink">
          <Form.Label>Problem Link</Form.Label>
          <Form.Control
            type="text"
            placeholder="Enter the problem link"
            value={problemLink}
            onChange={(e) => setProblemLink(e.target.value)}
          />
        </Form.Group>
        <Button variant="primary" onClick={createPythonFile}>
          Create Python File
        </Button>
      </Form>
    </div>
  );
}

export default App;
