import { createClient } from 'redis';
import { promisify } from 'util';

const client = createClient();
client.on('error', (err) => console.log('Redis client not connected to the server:', err));
client.on('connect', () => console.log('Redis client connected to the server'));

// Promisify the .get function
const getAsync = promisify(client.get).bind(client);

// Function to set key/value pair
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    if (err) {
      console.log(`Error setting value for ${schoolName}:`, err);
    } else {
      console.log(`Reply: ${reply}`);
    }
  });
}

// Async function to retrieve value
async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (err) {
    console.error(`Error retrieving value for ${schoolName}:`, err);
  }
}

// Run the operations
(async () => {
  await setNewSchool('ALX', '100');
  await displaySchoolValue('ALX');
})();

