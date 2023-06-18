const express = require('express');
const fs = require('fs');
const { promisify } = require('util');
const cors = require('cors');

const writeFileAsync = promisify(fs.writeFile);

const app = express();
app.use(cors());
app.use(express.json());

app.post('/create_file', async (req, res) => {
  const { problemName, problemLink } = req.body;
  const fileName = problemName.replace(/\s/g, '_').toLowerCase() + '.py';
  const fileContent = `
"""
LeetCode Problem: ${problemName}
LeetCode Link: ${problemLink}

Problem Description:
[Provide a brief description of the problem]

Solution:
"""

def your_function_name(input_parameters):
    # Your solution code goes here
    pass

# Test cases
# Add test cases to validate your solution
`;

  try {
    await writeFileAsync(`../python_files/${fileName}`, fileContent);
    res.send('Python file created successfully');
  } catch (error) {
    console.error(error);
    res.status(500).send('An error occurred');
  }
});

const port = 5000;
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
