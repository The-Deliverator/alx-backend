import kue from 'kue';

// Create the queue
const queue = kue.createQueue();

// Job data
const jobData = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
};

// Create the job in the queue
const job = queue.create('push_notification_code', jobData);

// Add job event handlers
job
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    } else {
      console.error('Notification job failed:', err);
    }
  });

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});

